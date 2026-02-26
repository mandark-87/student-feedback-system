from pymongo import MongoClient
from flask import redirect
from flask import Flask, render_template, request,redirect, url_for, session
import sqlite3
import os

mongo_client = MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["student_feedback"]

feedback_col = mongo_db["feedback"]

app = Flask(__name__)

def add_test_student():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO student (regno, password) VALUES (?, ?)",
        ("22BCA001", "123")
    )
    conn.commit()
    conn.close()
    print("student added")


def init_db():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS admin (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS student (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        regno TEXT,
        password TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS faculty (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        subject TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS feedback (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        faculty_id INTEGER,
        rating INTEGER
    )
    """)

    # Insert admin only once
    cur.execute(
        "INSERT OR IGNORE INTO admin (id, username, password) VALUES (1,'admin','admin')"
    )

    conn.commit()
    


@app.route("/")
def home():
    return "Student Feedback System Running"

@app.route('/dashboard')
def dashboard():
    import sqlite3

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Total feedback count
    cursor.execute("SELECT COUNT(*) FROM feedback")
    total_feedback = cursor.fetchone()[0]

    # Overall average rating
    cursor.execute("SELECT AVG(rating) FROM feedback")
    avg = cursor.fetchone()[0]
    overall_avg = round(avg, 2) if avg else 0

    # Faculty statistics using JOIN
    cursor.execute("""
        SELECT f.name, f.subject,
               COUNT(fe.id),
               ROUND(AVG(fe.rating), 2)
        FROM feedback fe
        JOIN faculty f ON fe.faculty_id = f.id
        GROUP BY f.id
    """)

    faculty_stats = cursor.fetchall()

    faculty_names = [f[0] for f in faculty_stats]
    faculty_ratings = [f[3] for f in faculty_stats]

    conn.close()

    return render_template(
        "dashboard.html",
        total_feedback=total_feedback,
        faculty_count=len(faculty_stats),
        overall_avg=overall_avg,
        faculty_stats=faculty_stats,
        faculty_names=faculty_names,
        faculty_ratings=faculty_ratings
    )

@app.route("/admin", methods=["GET", "POST"])
def admin_login():
    error = None

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("database.db")
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM admin WHERE username=? AND password=?",
            (username, password)
        )

        admin = cur.fetchone()
        conn.close()

        if admin:
            return redirect("/report")
        else:
            error = "Invalid Username or Password"

    return render_template("admin_login.html", error=error)

@app.route("/student", methods=["GET", "POST"])
def student_login():
    error = None
    if request.method == "POST":
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM student WHERE regno=? AND password=?",
            (request.form["regno"], request.form["password"])
        )
        student = cur.fetchone()
        conn.close()

        if student:
            return redirect("/feedback")   # 🔥 IMPORTANT FIX
        else:
            error = "Invalid Register Number or Password"

    return render_template("student_login.html", error=error)

@app.route("/register", methods=["GET", "POST"])
def register():
    error = None
    success = None

    if request.method == "POST":
        regno = request.form["regno"]
        password = request.form["password"]

        conn = sqlite3.connect("database.db")
        cur = conn.cursor()

        # Check if student already exists
        cur.execute("SELECT * FROM student WHERE regno=?", (regno,))
        existing_student = cur.fetchone()

        if existing_student:
            error = "Register Number already exists!"
        else:
            cur.execute(
                "INSERT INTO student (regno, password) VALUES (?, ?)",
                (regno, password)
            )
            conn.commit()
            success = "Registration successful! Please login."

        conn.close()

    return render_template("student_register.html", error=error, success=success)

@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    # fetch faculty list
    cur.execute("SELECT * FROM faculty")
    faculty = cur.fetchall()

    message = None

    if request.method == "POST":
        faculty_id = request.form["faculty_id"]
        rating = request.form["rating"]

        cur.execute(
            "INSERT INTO feedback (student_id, faculty_id, rating) VALUES (?,?,?)",
            (1, faculty_id, rating)
        )
        conn.commit()
        message = "Feedback Submitted Successfully"

    # 🔴 THIS PART WAS MISSING
    cur.execute("""
        SELECT faculty.name, faculty.subject, feedback.rating
        FROM feedback
        JOIN faculty ON faculty.id = feedback.faculty_id
    """)
    feedback_list = cur.fetchall()

    conn.close()

    return render_template(
        "feedback.html",
        faculty=faculty,
        feedback_list=feedback_list,
        message=message
    )
@app.route("/feedback", methods=["POST"])
def submit_feedback():
    feedback = {
        "student_id": request.form["student_id"],  # from SQL
        "course": request.form["course"],
        "rating": int(request.form["rating"]),
        "comment": request.form["comment"]
    }

    feedback_col.insert_one(feedback)
    return "Feedback Submitted Successfully"

@app.route("/logout")
def logout():
    session.clear()        # remove login session
    return redirect(url_for("student"))


@app.route("/report")
def report():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute("""
        SELECT feedback.id, faculty.name, faculty.subject, feedback.rating
        FROM feedback, faculty
        WHERE feedback.faculty_id = faculty.id
    """)

    reports = cur.fetchall()
    conn.close()

    return render_template("report.html", reports=reports)


    reports = cur.fetchall()
    conn.close()

    return render_template("report.html", reports=reports)
@app.route("/analytics")
def analytics():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    # ===== SQL LOGIC (CORE OF ANALYTICS) =====
    cur.execute("""
        SELECT 
            faculty.name,
            faculty.subject,
            COUNT(feedback.id) AS total_feedback,
            ROUND(AVG(feedback.rating), 2) AS avg_rating
        FROM feedback
        JOIN faculty ON feedback.faculty_id = faculty.id
        GROUP BY faculty.id
    """)
    faculty_stats = cur.fetchall()

    # Overall average rating
    cur.execute("SELECT ROUND(AVG(rating), 2) FROM feedback")
    overall_avg = cur.fetchone()[0]

    conn.close()

    return render_template(
        "analytics.html",
        faculty_stats=faculty_stats,
        overall_avg=overall_avg
    )




if __name__ == "__main__":
    init_db()
    app.run(debug=True, use_reloader=False)
