import json

incomplete_education = """
yes
What is your first name?
doru
What is your middle name? Answer N/A if you don't have one.
N/A
What is your last name?
irimescu
What is your email address?
doru.irimescu@xmail.com
What is your phone number?
+358 666666666
What is the highest degree you have obtained?
Msc
What is your field of study?
Automation and Electrical Engineering
What is the name of the institution where you obtained your degree?
Aalto University
What year did you graduate?
2020
Please provide information about your language skills.

What is the first language you are proficient in?
Romanian
What is your proficiency level in Romanian? Possible values are: Native, Fluent, Intermediate, Basic.
Native
What is the next language you are proficient in?
English
What is your proficiency level in English? Possible values are: Native, Fluent, Intermediate, Basic.
Fluent
What is the next language you are proficient in?
no more
Please provide information about your work experience.

What is your job title in your most recent work experience?
software engineer
What is the name of the company you worked for in your most recent work experience?
joblys
What was the start date of your most recent work experience? Please provide the date in the format YYYY-MM-DD.
2023-08-01
What was the end date of your most recent work experience? If you are still working there, please write N/A.
N/A
What were your responsibilities in your most recent work experience?
write software for this product
Please provide information about your skills.

What is one of your skills?
c++, python
What is another one of your skills?
c++, python
What is another one of your skills?
no more
Please provide information about your certifications.

What is the name of your certification?
no certifications
What is your desired job location?
helsinki
What type of job are you looking for? Possible values are: Full-time, Part-time, Contract, Temporary, Internship.
Full-time
What industry are you interested in?
ict
What is the link to your portfolio? Answer N/A if you don't have one.
https://github.com/doruirimescu/activity/blob/master/Doru-Stefan%20Irimescu.pdf
What is the link to your LinkedIn profile? Answer N/A if you don't have one.
https://www.linkedin.com/in/doru-stefan-irimescu/
What is the link to your resume? Answer N/A if you don't have one.
https://github.com/doruirimescu/activity/blob/master/Doru-Stefan%20Irimescu.pdf
"""

incomplete_education_json = json.loads("""
{
    "first_name": "doru",
    "middle_name": "n/a",
    "last_name": "irimescu",
    "contact_information": {
        "email": "doru.irimescu@xmail.com",
        "phone_number": "+358 666666666"
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
        }
    ],
    "work_experience": [
        {
            "job_title": "software engineer",
            "company": "joblys",
            "start_date": "2023-08-01",
            "end_date": "n/a",
            "responsibilities": "write software for this product"
        }
    ],
    "skills": [
        "c++, python"
    ],
    "certifications": [
        {
            "certification_name": "no certifications"
        }
    ],
    "desired_job_location": "helsinki",
    "desired_job_type": "full-time",
    "desired_industry": "ict",
    "portfolio_link": "https://github.com/doruirimescu/activity/blob/master/doru-stefan%20irimescu.pdf",
    "linkedin_profile": "https://www.linkedin.com/in/doru-stefan-irimescu/",
    "resume_link": "https://github.com/doruirimescu/activity/blob/master/doru-stefan%20irimescu.pdf"
}
"""
)
