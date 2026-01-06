from fastapi import FastAPI,Query, Path, Body, HTTPException
from pydantic import BaseModel,EmailStr, field_validator,Field
import re



app=FastAPI()

class AdmissionForm(BaseModel):
    name: str = Field(..., min_length=3)
    email: EmailStr
    password: str = Field(..., min_length=8)
    age: int = Field(..., ge=17, le=30)
    phone: str
    marks: float = Field(..., ge=0, le=100)
    address: str = Field(..., min_length=5)
    gender: str
    category: str
    

    #validators

    @field_validator("name")
    @classmethod
    def validate_name(cls, v):
        if not re.fullmatch(r"[A-Za-z ]+", v):
            raise ValueError("Name must contain only alphabets and spaces")
        return v

    



    @field_validator("password")
    @classmethod

    def validate_password(cls,v):
        if not re.search(r"[A-Z]",v):
            raise ValueError("Password must contain uppercase letter")
        if not re.search(r"[a-z]",v):
            raise ValueError("Password must contain lowercase letter")
        if not re.search(r"[0-9]",v):
            raise ValueError("Password must contain number")              
        if not re.search(r"[ !@#$%^&*]",v):
            raise ValueError("Password must contain special character")
        return v
    


    @field_validator("phone")
    @classmethod
    def validate_phone(cls, v):
        if not re.fullmatch(r"\d{10}", v):
            raise ValueError("Phone number must be exactly 10 digits")
        return v

        

       




    
    



@app.post("/admission/{university_id}/{course_id}")
def submit_admission(
    university_id: int = Path(..., gt=0),
    course_id: int = Path(..., gt=0),
    academic_year: int = Query(..., ge=2024),
    quota: str = Query("general"),
    mode: str = Query("online"),
    hostel_required: bool = Query(False),
    entrance_exam: bool = Query(True),
    student: AdmissionForm = Body(...)

):
    

    min_marks = 60
    if quota.lower() in ["sc", "st"]:
        min_marks = 50

    if student.marks < min_marks:
        raise HTTPException(
            status_code=400,
            detail=f"Minimum {min_marks}% marks required for admission"
        )
    

    if not entrance_exam and quota.lower() != "management":
        raise HTTPException(
            status_code=400,
            detail="Non-entrance admissions allowed only under management quota"
        )
    

    if hostel_required and not student.gender:
        raise HTTPException(
            status_code=400,
            detail="Gender is required for hostel allocation"
        )




    return {
        "status": "Application Submitted",
        "university_id": university_id,
        "course_id": course_id,
        "academic_year": academic_year,
        "mode": mode,
        "quota": quota,
        "hostel_required": hostel_required,
        "student_details": {
            "name": student.name,
            "email": student.email,
            "marks": student.marks,
            "category": student.category
        }
    }









