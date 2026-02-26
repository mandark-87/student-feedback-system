# 🎓 Faculty Performance Analytics System

A secure full-stack web application built using Flask that collects student feedback and generates faculty performance analytics through an interactive admin dashboard.

---

## 🚀 Features

✅ Student Registration & Login  
✅ Secure Password Hashing  
✅ Feedback Submission System  
✅ Admin Login  
✅ Faculty-wise Performance Analytics  
✅ Overall Average Rating Calculation  
✅ CSV Report Export  
✅ Interactive Charts (Chart.js)

---

## 🛠 Tech Stack

- Python (Flask)
- SQLite
- HTML5
- CSS3
- Jinja2 Templates
- Chart.js
- Werkzeug (Password Hashing)

---

## 📂 Project Structure
student-feedback-system/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── static/
│ ├── style.css
│
├── templates/
│ ├── admin_login.html
│ ├── student_login.html
│ ├── student_register.html
│ ├── feedback.html
│ ├── analytics.html
│
└── database.db

---
---

## 📸 Screenshots

### 🏠 Home Page
![Home](https://github.com/user-attachments/assets/677dbec9-a146-495e-923a-6b6e4a6a445f)

### 👨‍🎓 Student Registration
![Register](https://github.com/user-attachments/assets/a64e6a2c-a9ae-41f3-b9ba-6d2dd508e5ab)

### 🔐 Student Login
![Login](https://github.com/user-attachments/assets/e3c434cc-7b34-417e-b692-a76165d4093b)

### 📝 Feedback Form
![Feedback](https://github.com/user-attachments/assets/808f6e36-9900-4f68-b0c1-97befc02a207)

### 📊 Analytics Dashboard
![Analytics](https://github.com/user-attachments/assets/bbfd0c60-a3b2-4570-b5e0-e218a9b12249)

### 📈 Chart Visualization
![Charts](https://github.com/user-attachments/assets/d3945de5-306b-45a0-8550-4bbf1d26b292)

### 📁 CSV Export
![CSV](https://github.com/user-attachments/assets/5cc5416c-f0de-40ac-8a8f-1e53ec9f6547)

### 📋 Faculty Table View
![Table](https://github.com/user-attachments/assets/710c5dc3-e504-4f08-97bd-9641a09b2273)

### ⭐ Overall Rating Display
![Overall](https://github.com/user-attachments/assets/f72d3ebc-6311-45ac-ac8f-c2f9f73773c1)

---

## 🔐 Security Implementation

Passwords are securely hashed using Werkzeug:

```python
from werkzeug.security import generate_password_hash, check_password_hash
📊 Analytics Dashboard

The admin dashboard displays:

Faculty Name

Subject

Total Feedback Count

Average Rating

Overall Rating

Bar Chart Visualization

CSV Export Option

▶️ How To Run Locally
1️⃣ Clone Repository
git clone https://github.com/mandark-87/student-feedback-system.git
cd student-feedback-system
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run Application
python app.py

Open in browser:

http://127.0.0.1:5000
📈 Future Improvements

Role-based authentication

JWT implementation

MySQL/PostgreSQL integration

Email notification system

Advanced data visualization

Deployment on cloud (Render/AWS)
👨‍💻 Author

Mandar Ramchandra Kulkarni
BCA Graduate | Full Stack Developer
GitHub: https://github.com/mandark-87

Location: Karnataka, India
⭐ If You Like This Project

Give it a star on GitHub!


---

# ✅ After Pasting

Run:

```bash
git add README.md
git commit -m "Added professional README"
git push

---

SCREENSHOTS
<img width="1920" height="1023" alt="Image" src="https://github.com/user-attachments/assets/677dbec9-a146-495e-923a-6b6e4a6a445f" />
<img width="1920" height="1027" alt="Image" src="https://github.com/user-attachments/assets/a64e6a2c-a9ae-41f3-b9ba-6d2dd508e5ab" />
<img width="1920" height="1029" alt="Image" src="https://github.com/user-attachments/assets/e3c434cc-7b34-417e-b692-a76165d4093b" />
<img width="1920" height="1024" alt="Image" src="https://github.com/user-attachments/assets/808f6e36-9900-4f68-b0c1-97befc02a207" />
<img width="1229" height="910" alt="Image" src="https://github.com/user-attachments/assets/bbfd0c60-a3b2-4570-b5e0-e218a9b12249" />
<img width="1194" height="864" alt="Image" src="https://github.com/user-attachments/assets/d3945de5-306b-45a0-8550-4bbf1d26b292" />
<img width="1920" height="1023" alt="Image" src="https://github.com/user-attachments/assets/5cc5416c-f0de-40ac-8a8f-1e53ec9f6547" />
<img width="1920" height="1026" alt="Image" src="https://github.com/user-attachments/assets/710c5dc3-e504-4f08-97bd-9641a09b2273" />
<img width="1920" height="1018" alt="Image" src="https://github.com/user-attachments/assets/f72d3ebc-6311-45ac-ac8f-c2f9f73773c1" />
