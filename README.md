)

🎓 University Admission API (FastAPI)

A backend REST API built using FastAPI that simulates a real-world university admission system with strong validation, business rules, and clean API design.

🚀 Features

Path, Query & Body parameter usage (industry-style)

Strong input validation using Pydantic

Custom field validators (email, phone, password, name)

Conditional admission rules (quota, entrance exam, hostel)

Proper HTTP error handling

Beginner-friendly but industry-structured

🛠 Tech Stack

Python 3.10+

FastAPI

Pydantic

Uvicorn

📂 Project Structure
university-admission-api/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore

▶️ How to Run the Project

1️⃣ Clone the repository

git clone https://github.com/your-username/university-admission-api.git


2️⃣ Install dependencies

pip install -r requirements.txt


3️⃣ Run the server

uvicorn main:app --reload


4️⃣ Open API Docs

Swagger UI → http://127.0.0.1:8000/docs

ReDoc → http://127.0.0.1:8000/redoc

📌 Sample Endpoint
POST /admission/{university_id}/{course_id}


Query Parameters

academic_year

quota

mode

hostel_required

entrance_exam

Request Body

name

email

password

age

phone

marks

address

gender

category

🧠 Learning Outcome

This project helped me understand:

Real-world backend API design

Validation vs business rules

Clean request handling

HTTP status codes

FastAPI best practices

🙌 Author

Prabhat Shinde
IT Student | FastAPI Backend Learner
🇮🇳 India