from typing import List, Optional
from pydantic import BaseModel, EmailStr, HttpUrl
from enum import Enum
import json


class ContactInformation(BaseModel):
    email: EmailStr
    phone_number: str


class Education(BaseModel):
    degree: str
    field_of_study: str
    institution: str
    graduation_year: int


class WorkExperience(BaseModel):
    job_title: str
    company: str
    start_date: str
    end_date: str
    responsibilities: str


class Certification(BaseModel):
    certification_name: str
    issuing_organization: str
    date_issued: str
    expiration_date: Optional[str]


class ProfficiencyLevel(str, Enum):
    NATIVE = "Native"
    FLUENT = "Fluent"
    INTERMEDIATE = "Intermediate"
    BASIC = "Basic"


class Language(BaseModel):
    language: str
    proficiency_level: ProfficiencyLevel


class DesiredJobType(str, Enum):
    FULL_TIME = "Full-time"
    PART_TIME = "Part-time"
    CONTRACT = "Contract"
    TEMPORARY = "Temporary"
    INTERNSHIP = "Internship"


class JobSeekerProfile(BaseModel):
    # This datastructure is used to store the user's profile information
    full_name: str
    contact_information: ContactInformation
    education: List[Education]
    work_experience: List[WorkExperience]
    skills: List[str]
    certifications: List[Certification]
    languages: List[Language]
    desired_job_location: str
    desired_job_type: DesiredJobType
    desired_industry: str
    portfolio_link: HttpUrl
    linkedin_profile: HttpUrl
    resume_link: HttpUrl


# TO BE ADDED FOR COVER LETTER GENERATION:
class PersonalStatement(BaseModel):
    career_goals: str
    interests: str
    seeking_position: str  # Description of the type of position they are seeking


class Achievement(BaseModel):
    title: str
    description: str


class CareerChangeExplanation(BaseModel):
    reason: str
    aligns_with_goals: str  # How the change aligns with career goals


class CustomSection(BaseModel):
    section_title: str
    content: str | List[Achievement] | CareerChangeExplanation


SCHEMA = JobSeekerProfile.schema()
SCHEMA = json.dumps(SCHEMA, indent=4)
