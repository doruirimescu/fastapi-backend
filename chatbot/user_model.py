from typing import List, Optional
from pydantic import BaseModel, EmailStr, HttpUrl, Field, validator
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
    start_date: date
    end_date: Optional[date] = Field(json_schema_extra={
            'title': 'End date of this work position',
            'description': 'The end date of this work position. If you are still working here, write N/A.',
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
    expiration_date: Optional[date]


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
    portfolio_link: Optional[str] = Field(description="What is the link to your portfolio ? Answer N/A if you don't have one")
    linkedin_profile: Optional[str] = Field(description="What is the link to your linkedin profile ? Answer N/A if you don't have one")
    resume_link: Optional[str] = Field(description="What is the link to your resume ? Answer N/A if you don't have one")

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
