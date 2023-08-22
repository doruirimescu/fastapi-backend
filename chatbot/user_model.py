from typing import List, Optional
from pydantic import BaseModel, EmailStr, HttpUrl, Field, validator, root_validator
from enum import Enum
from datetime import date

#TODO: Add validators
# https://python.langchain.com/docs/modules/model_io/output_parsers/pydantic

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
    start_date: date = Field(
        json_schema_extra={
            'title': 'Start date of this work position',
            'description': 'The start date of this work position. Format: YYYY-MM-DD',
            'examples': ['YYYYY-MM-DD'],
        }
    )
    end_date: Optional[date] = Field(
        json_schema_extra={
            'title': 'End date of this work position',
            'description': 'The end date of this work position. Format: YYYY-MM-DD. If you are still working here, write N/A. ',
            'examples': ['YYYYY-MM-DD', 'N/A'],
        })
    responsibilities: str

    @validator('end_date', pre=True)
    def validate_end_date(cls, value):
        return None if value == "N/A" else value


class Certification(BaseModel):
    certification_name: str
    issuing_organization: str
    date_issued: str
    expiration_date: Optional[date] = Field(
        json_schema_extra={
            'title': 'Expiration date of this certification',
            'description': 'The expiration date of this certification. Format: YYYY-MM-DD. If it does not expire, write N/A.',
            'examples': ['YYYYY-MM-DD', 'N/A'],
        }
    )

    @validator('expiration_date', pre=True)
    def validate_expiration_date(cls, value):
        return None if value == "N/A" else value


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


def has_required_fields(data: dict, model) -> bool:
    for field_name, field in model.__fields__.items():
        if data.get(field_name) is None:
            return False
    return True


class JobSeekerProfile(BaseModel):
    # This datastructure is used to store the user's profile information
    first_name: str = Field(description="What is your first name ?")
    middle_name: Optional[str] = Field(description="What is your middle name ? Answer N/A if you don't have one")
    last_name: str = Field(description="What is your last name ?")
    contact_information: ContactInformation
    education: List[Education]
    languages: List[Language]
    work_experience: List[WorkExperience]
    skills: List[str]
    certifications: List[Certification]
    desired_job_location: str
    desired_job_type: DesiredJobType
    desired_industry: str
    portfolio_link: Optional[str] = Field(
        json_schema_extra={
            'title': 'Link to your portfolio',
            'description': 'What is the link to your portfolio ? Answer N/A if you don\'t have one',
            'examples': ['https://www.example.com', 'N/A'],
        }
    )

    linkedin_profile: Optional[str] = Field(
        json_schema_extra={
            'title': 'Link to your linkedin profile',
            'description': 'What is the link to your portfolio ? Answer N/A if you don\'t have one',
            'examples': ['https://www.linkedin.com/in/name-name/', 'N/A'],
        }
    )
    resume_link: Optional[str] = Field(
        json_schema_extra={
            'title': 'Link to your resume profile',
            'description': 'What is the link to your resume ? Answer N/A if you don\'t have one',
            'examples': ['https://www.example.com', 'N/A'],
        }
    )

    @validator('middle_name', pre=True)
    def validate_middle_name(cls, value):
        return None if value == "N/A" else value

    @validator('portfolio_link', pre=True)
    def validate_portfolio_link(cls, value):
        return None if value == "N/A" else value

    @validator('linkedin_profile', pre=True)
    def validate_linkedin_profile(cls, value):
        return None if value == "N/A" else value

    @validator('resume_link', pre=True)
    def validate_resume_link(cls, value):
        return None if value == "N/A" else value

    @validator('certifications', pre=True)
    def validate_certifications(cls, value):
        certs = [
            c
            for c in value
            if c.get("certification_name") is not ''
            and c.get("issuing_organization") is not ''
            and c.get("date_issued") is not ''
        ]
        return certs

    @root_validator(pre=True)
    def discard_incomplete_work_experience(cls, values):
        work_experiences = values.get("work_experience", [])
        complete_work_experiences = [we for we in work_experiences if has_required_fields(we, WorkExperience)]
        if complete_work_experiences:
            values["work_experience"] = complete_work_experiences
        else:
            values.pop("work_experience", None)
        return values

    @root_validator(pre=True)
    def discard_incomplete_education(cls, values):
        educations = values.get("education", [])
        complete_educations = [e for e in educations if has_required_fields(e, Education)]
        if complete_educations:
            values["education"] = complete_educations
        else:
            values.pop("education", None)
        return values

    @root_validator(pre=True)
    def discard_incomplete_certifications(cls, values):
        print("DISCARDING INCOMPLETE CERTIFICATIONS")
        certifications = values.get("certifications", [])
        complete_certifications = [c for c in certifications if has_required_fields(c, Certification)]
        if complete_certifications:
            values["certifications"] = complete_certifications
        else:
            values.pop("certifications", None)
        return values



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
