import json

invliad_desired_job_type = """
yes
What is your first name?
doru
What is your middle name? Answer n/a if you don"t have one.
stefan
What is your last name?
irimescu
What is your email address?
doru.irimescu@gmail.com
What is your phone number?
+358 466162925
What is the highest degree you have obtained?
Msc
What is your field of study?
Automation and Electrical Engineering
What is the name of the institution where you obtained your degree?
Aalto University
What year did you graduate?
2020
What languages do you speak? Please provide the language and your proficiency level (Native, Fluent, Intermediate, Basic).
Romanian - Native, English - Fluent, Finnish - Basic
Please provide your work experience. For each work experience, include the job title, company, start date, end date, and responsibilities.
software engineer at jobly, starting at 2023-01-01, currently working there, responsibilities: software engineering
Please provide any additional work experience you have. If you don"t have any more work experience, please respond with "n/a".
n/a
What skills do you possess? Please list them separated by commas.
c++, python
Please provide any certifications you have obtained. For each certification, include the certification name, issuing organization, date issued, and expiration date (if applicable). If a certification does not expire, please write "n/a" for the expiration date.
Project manager, issued by Aalto University, date issued 2020-01-01, n/a
What is your desired job location?
helsinki
What type of job are you looking for? The possible options are Full-time, Part-time, Contract, Temporary, and Internship.
fulltime
What industry are you interested in?
ICT
What is the link to your portfolio? Answer n/a if you don"t have one.
https://github.com/doruirimescu/activity/tree/master/Portfolio
What is the link to your LinkedIn profile? Answer n/a if you don"t have one.
https://www.linkedin.com/in/doru-stefan-irimescu/
What is the link to your resume? Answer n/a if you don"t have one.
https://github.com/doruirimescu/activity/blob/master/Doru-Stefan%20Irimescu.pdf
"""

invliad_desired_job_type_json = json.loads("""
{
    "first_name": "doru",
    "middle_name": "stefan",
    "last_name": "irimescu",
    "contact_information": {
        "email": "doru.irimescu@gmail.com",
        "phone_number": "+358 466162925"
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
            "start_date": "2023-01-01",
            "end_date": "n/a",
            "responsibilities": "software engineering"
        }
    ],
    "skills": [
        "c++",
        "python"
    ],
    "certifications": [
        {
            "certification_name": "project manager",
            "issuing_organization": "aalto university",
            "date_issued": "2020-01-01",
            "expiration_date": "n/a"
        }
    ],
    "desired_job_location": "helsinki",
    "desired_job_type": "full-time",
    "desired_industry": "ict",
    "portfolio_link": "https://github.com/doruirimescu/activity/tree/master/portfolio",
    "linkedin_profile": "https://www.linkedin.com/in/doru-stefan-irimescu/",
    "resume_link": "https://github.com/doruirimescu/activity/blob/master/doru-stefan%20irimescu.pdf"
}
"""
)
