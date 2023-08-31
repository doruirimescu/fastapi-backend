from typing import List, Optional
from pydantic import BaseModel, EmailStr, HttpUrl, Field, validator, root_validator
from enum import Enum
from datetime import date

#TODO: Add validators
# https://python.langchain.com/docs/modules/model_io/output_parsers/pydantic


class Unanswered(BaseModel):
    # To be used for fields that have not been answered
    pass

def is_unanswered(value):
    return value == Unanswered()

class ContactInformation(BaseModel):
    email: EmailStr | Unanswered
    phone_number: str | Unanswered


class Education(BaseModel):
    degree: str | Unanswered
    field_of_study: str | Unanswered
    institution: str | Unanswered
    graduation_year: int | Unanswered


class WorkExperience(BaseModel):
    job_title: str | Unanswered
    company: str | Unanswered
    start_date: date | Unanswered = Field(
        json_schema_extra={
            'title': 'Start date of this work position',
            'description': 'The start date of this work position. Format: YYYY-MM-DD',
            'examples': ['YYYYY-MM-DD'],
        },
        default=Unanswered(),
    )
    end_date: Optional[date] = Field(
        json_schema_extra={
            'title': 'End date of this work position',
            'description': 'The end date of this work position. Format: YYYY-MM-DD. If you are still working here, write n/a. ',
            'examples': ['YYYYY-MM-DD', 'n/a'],
        })
    responsibilities: str

    @validator('end_date', pre=True)
    def validate_end_date(cls, value):
        return None if value == "n/a" else value


class Certification(BaseModel):
    certification_name: str | Unanswered = Unanswered()
    issuing_organization: str | Unanswered = Unanswered()
    date_issued: str | Unanswered = Unanswered()
    expiration_date: Optional[date | Unanswered] = Field(
        json_schema_extra={
            'title': 'Expiration date of this certification',
            'description': 'The expiration date of this certification. Format: YYYY-MM-DD. If it does not expire, write n/a.',
            'examples': ['YYYYY-MM-DD', 'n/a'],
        },
        default=Unanswered(),
    )

    @validator('expiration_date', pre=True)
    def validate_expiration_date(cls, value):
        return None if value == "n/a" else value

class ProfficiencyLevel(str, Enum):
    NATIVE = "native"
    FLUENT = "fluent"
    INTERMEDIATE = "intermediate"
    BASIC = "basic"


class Language(BaseModel):
    language: str | Unanswered = Field(
        json_schema_extra={
            'title': 'Language',
            'description': 'The language you speak',
            'examples': ['English'],
        },
        default=Unanswered(),
    )
    proficiency_level: ProfficiencyLevel = Field(
        json_schema_extra={
            'title': 'Language profficency level',
            'description': (
                f'The profficency level of the language you speak. '
                f'Only allowed values are the ones defined in the enum type.',
            ),
            'examples': ['fluent'],
        }
    )


class DesiredJobType(str, Enum):
    FULL_TIME = "full-time"
    PART_TIME = "part-time"
    CONTRACT = "contract"
    TEMPORARY = "temporary"
    INTERNSHIP = "internship"


def has_required_fields(data: dict, model) -> bool:
    for field_name, field in model.__fields__.items():
        if data.get(field_name) is None:
            return False
    return True


class JobSeekerProfile(BaseModel):
    # This datastructure is used to store the user's profile information
    first_name: str | Unanswered = Field(description="What is your first name ?", default=Unanswered())
    middle_name: Optional[str] = Field(description="What is your middle name ? Answer n/a if you don't have one")
    last_name: str | Unanswered = Field(description="What is your last name ?", default=Unanswered())
    contact_information: ContactInformation | Unanswered = Field(default=Unanswered())
    education: List[Education] = Field(
        json_schema_extra={
            'title': 'Education',
            'description': 'List of all your education experiences (Bsc, Msc, etc)',
        }
    )
    languages: List[Language]
    work_experience: List[WorkExperience] = Field(
        json_schema_extra={
            'title': 'Work experience',
            'description': 'List of all your work experiences',
        }
    )
    skills: List[str]
    certifications: List[Certification]
    desired_job_location: str
    desired_job_type: DesiredJobType
    desired_industry: str
    portfolio_link: Optional[str] = Field(
        json_schema_extra={
            'title': 'Link to your portfolio',
            'description': 'What is the link to your portfolio ? Answer n/a if you don\'t have one',
            'examples': ['https://www.example.com', 'n/a'],
        }
    )

    linkedin_profile: Optional[str] = Field(
        json_schema_extra={
            'title': 'Link to your linkedin profile',
            'description': 'What is the link to your portfolio ? Answer n/a if you don\'t have one',
            'examples': ['https://www.linkedin.com/in/name-name/', 'n/a'],
        }
    )
    resume_link: Optional[str] = Field(
        json_schema_extra={
            'title': 'Link to your resume profile',
            'description': 'What is the link to your resume ? Answer n/a if you don\'t have one',
            'examples': ['https://www.example.com', 'n/a'],
        }
    )

    @validator('middle_name', pre=True)
    def validate_middle_name(cls, value):
        return None if value == "n/a" else value

    @validator('portfolio_link', pre=True)
    def validate_portfolio_link(cls, value):
        return None if value == "n/a" else value

    @validator('linkedin_profile', pre=True)
    def validate_linkedin_profile(cls, value):
        return None if value == "n/a" else value

    @validator('resume_link', pre=True)
    def validate_resume_link(cls, value):
        return None if value == "n/a" else value

    @validator('certifications', pre=True)
    def validate_certifications(cls, value):
        certs = [
            c
            for c in value
            if c.get("certification_name") != ''
            and c.get("issuing_organization") != ''
            and c.get("date_issued") != ''
        ]
        return certs

    @root_validator(pre=True)
    def discard_incomplete_work_experience(cls, values):
        work_experiences = values.get("work_experience", [])
        complete_work_experiences = [we for we in work_experiences if has_required_fields(we, WorkExperience)]
        values["work_experience"] = complete_work_experiences
        return values

    @root_validator(pre=True)
    def discard_incomplete_education(cls, values):
        educations = values.get("education", [])
        complete_educations = [e for e in educations if has_required_fields(e, Education)]
        values["education"] = complete_educations
        return values

    @root_validator(pre=True)
    def discard_incomplete_certifications(cls, values):
        certifications = values.get("certifications", [])
        complete_certifications = [c for c in certifications if has_required_fields(c, Certification)]
        values["certifications"] = complete_certifications
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
