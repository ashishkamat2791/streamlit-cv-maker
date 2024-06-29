from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import pandas as pd

app = FastAPI()

# Define Pydantic models
class WorkExperience(BaseModel):
    company_name: str
    from_date: str
    to_date: str
    skills_used: str
    summary_of_experience: str
    designation: str

class EducationalBackground(BaseModel):
    name: str
    type: str
    university_or_board_name: str
    year_of_completion: str
    is_ongoing: str

class Project(BaseModel):
    name_of_project: str
    summary: str
    skills_used: str
    duration: str
    year: str

class Certification(BaseModel):
    name: str
    summary: str
    year: int

# Load data from CSV
work_experience_df = pd.read_csv("data/Work-Experience.csv")
educational_background_df = pd.read_csv("data/Educational-background.csv")
projects_df = pd.read_csv("data/Projects.csv")
certifications_df = pd.read_csv("data/Certifications.csv")

# Endpoints to fetch data
@app.get("/work-experience", response_model=List[WorkExperience])
def get_work_experience():
    return work_experience_df.to_dict(orient="records")

@app.get("/educational-background", response_model=List[EducationalBackground])
def get_educational_background():
    return educational_background_df.to_dict(orient="records")

@app.get("/projects", response_model=List[Project])
def get_projects():
    return projects_df.to_dict(orient="records")

@app.get("/certifications", response_model=List[Certification])
def get_certifications():
    return certifications_df.to_dict(orient="records")