import json

incomplete_work_experience = """
yes
What is your first name?
doru
What is your middle name? Answer n/a if you don't have one.
n/a
What is your last name?
Irimescu
What is your email address?
doru.irimescu@hotmail.com
What is your phone number?
+358666666666
What is the highest degree you have obtained?
Msc
What is your field of study?
automation and electrical engineering
What is the name of the institution where you obtained your degree?
Aalto University
What year did you graduate?
2020
Please provide information about your language skills.

What is your first language and proficiency level?
Romanian is my native language
What other languages do you speak and what is your proficiency level in each?
English, Finnish
What is your proficiency level in English?
Fluent
What is your proficiency level in Finnish?
basic
Please provide information about your work experience.

What is your job title?
software engineer
What is the name of the company you work for?
jobly
When did you start working at this company? Please provide the date in the format YYYY-MM-DD.
2023-08-01
When did you end your employment at this company? Please provide the date in the format YYYY-MM-DD. If you are still working there, please write n/a.
n/a
What were your responsibilities in this role?
software engineer
Please provide information about any other work experience you have.

What is your job title?
no other experience
Please provide information about your skills.

What are your skills? Please separate each skill with a comma.
c++, python
Please provide information about any certifications you have.

What is the name of the certification you obtained?
Project manager certificate
Who issued the certification?
Aalto university
When was the certification issued? Please provide the date in the format YYYY-MM-DD.
2020-01-01
Does the certification have an expiration date? If yes, please provide the date in the format YYYY-MM-DD. If it does not expire, please write n/a.
n/a
What is your desired job location?
Helsinki
What type of job are you looking for? The possible options are: Full-time, Part-time, Contract, Temporary, Internship.
Full-time
What industry are you interested in?
ICT
What is the link to your portfolio? Answer n/a if you don't have one.
n/a
What is the link to your LinkedIn profile? Answer n/a if you don't have one.
https://www.linkedin.com/in/doru-stefan-irimescu/
What is the link to your resume? Answer n/a if you don't have one.
"""

incomplete_work_experience_json = json.loads(
"""
{
    "first_name": "doru",
    "middle_name": "n/a",
    "last_name": "irimescu",
    "contact_information": {
        "email": "doru.irimescu@hotmail.com",
        "phone_number": "+358666666666"
    },
    "education": [
        {
            "degree": "msc",
            "field_of_study": "automation and electrical engineering",
            "institution": "aalto university",
            "graduation_year": 2020
        }
    ],
    "languages": [
        {
            "language": "romanian",
            "proficiency_level": "native"
        },
        {
            "language": "english",
            "proficiency_level": "fluent"
        },
        {
            "language": "finnish",
            "proficiency_level": "basic"
        }
    ],
    "work_experience": [
        {
            "job_title": "software engineer",
            "company": "jobly",
            "start_date": "2023-08-01",
            "end_date": "n/a",
            "responsibilities": "software engineer"
        }
    ],
    "skills": [
        "c++",
        "python"
    ],
    "certifications": [
        {
            "certification_name": "project manager certificate",
            "issuing_organization": "aalto university",
            "date_issued": "2020-01-01",
            "expiration_date": "n/a"
        }
    ],
    "desired_job_location": "helsinki",
    "desired_job_type": "full-time",
    "desired_industry": "ict",
    "portfolio_link": "n/a",
    "linkedin_profile": "https://www.linkedin.com/in/doru-stefan-irimescu/",
    "resume_link": "n/a"
}
"""
)
from chatbot.user_model import JobSeekerProfile, SCHEMA
JobSeekerProfile(**incomplete_work_experience_json)
