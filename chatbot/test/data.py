# Data for unit tests

input_data = """
My name is Jane Smith, and I'm actively seeking new opportunities. You can reach me at jane.smith@example.com or call me at (123) 456-7890.

Education:

Bachelor's Degree in Computer Science from University of Tech, graduated in 2019.
Master's Degree in Artificial Intelligence from AI Institute, graduated in 2021.
Work Experience:

Software Engineer at TechCorp from January 2020 to June 2021. Responsible for developing and maintaining web applications.
Data Scientist at DataWorld from July 2021 to present. Analyzing large datasets and creating predictive models.
Skills:

Programming: Python, Java, C++
Machine Learning
Data Analysis
Certifications:

Certified Python Programmer, issued by Python Institute in June 2018, expires in June 2023.
Machine Learning Specialist, issued by AI Association in January 2020.
Languages:

English: Native
Spanish: Fluent
French: Intermediate
I'm interested in Full-time positions in the Software Development industry, preferably in New York City.
My LinkedIn profile can be found at https://www.linkedin.com/in/janesmith,
and my online portfolio is at http://www.janesmithportfolio.com.
You can also download my resume from http://www.janesmithresume.com.
"""


expected_result = {
    "full_name": "Jane Smith",
    "contact_information": {
        "email": "jane.smith@example.com",
        "phone_number": "(123) 456-7890",
    },
    "education": [
        {
            "degree": "Bachelor's Degree",
            "field_of_study": "Computer Science",
            "institution": "University of Tech",
            "graduation_year": 2019,
        },
        {
            "degree": "Master's Degree",
            "field_of_study": "Artificial Intelligence",
            "institution": "AI Institute",
            "graduation_year": 2021,
        },
    ],
    "work_experience": [
        {
            "job_title": "Software Engineer",
            "company": "TechCorp",
            "start_date": "January 2020",
            "end_date": "June 2021",
            "responsibilities": "Developing and maintaining web applications",
        },
        {
            "job_title": "Data Scientist",
            "company": "DataWorld",
            "start_date": "July 2021",
            "end_date": "present",
            "responsibilities": "Analyzing large datasets and creating predictive models",
        },
    ],
    "skills": ["Python", "Java", "C++", "Machine Learning", "Data Analysis"],
    "certifications": [
        {
            "certification_name": "Certified Python Programmer",
            "issuing_organization": "Python Institute",
            "date_issued": "June 2018",
            "expiration_date": "June 2023",
        },
        {
            "certification_name": "Machine Learning Specialist",
            "issuing_organization": "AI Association",
            "date_issued": "January 2020",
        },
    ],
    "languages": [
        {"language": "English", "proficiency_level": "Native"},
        {"language": "Spanish", "proficiency_level": "Fluent"},
        {"language": "French", "proficiency_level": "Intermediate"},
    ],
    "desired_job_location": "New York City",
    "desired_job_type": "Full-time",
    "desired_industry": "Software Development",
    "portfolio_link": "http://www.janesmithportfolio.com",
    "linkedin_profile": "https://www.linkedin.com/in/janesmith",
    "resume_link": "http://www.janesmithresume.com",
}

chatbot_conversation ="""
yes
What is your first name?
doru
What is your middle name? Answer N/A if you don't have one.
N/A
What is your last name?
Irimescu
What is your email address?
doru.irimescu@gmail.com
What is your phone number?
+358466162925
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
When did you end your employment at this company? Please provide the date in the format YYYY-MM-DD. If you are still working there, please write N/A.
N/A
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
Does the certification have an expiration date? If yes, please provide the date in the format YYYY-MM-DD. If it does not expire, please write N/A.
N/A
What is your desired job location?
Helsinki
What type of job are you looking for? The possible options are: Full-time, Part-time, Contract, Temporary, Internship.
Full-time
What industry are you interested in?
ICT
What is the link to your portfolio? Answer N/A if you don't have one.
N/A
What is the link to your LinkedIn profile? Answer N/A if you don't have one.
https://www.linkedin.com/in/doru-stefan-irimescu/
What is the link to your resume? Answer N/A if you don't have one.
"""

import json
incomplete_content='{\n  "first_name": "doru",\n  "middle_name": "N/A",\n  "last_name": "Irimescu",\n  "contact_information": {\n    "email": "doru.irimescu@gmail.com",\n    "phone_number": "+358466162925"\n  },\n  "education": [\n    {\n      "degree": "Msc",\n      "field_of_study": "automation and electrical engineering",\n      "institution": "Aalto University",\n      "graduation_year": 2020\n    }\n  ],\n  "languages": [\n    {\n      "language": "Romanian",\n      "proficiency_level": "Native"\n    },\n    {\n      "language": "English",\n      "proficiency_level": "Fluent"\n    },\n    {\n      "language": "Finnish",\n      "proficiency_level": "Basic"\n    }\n  ],\n  "work_experience": [\n    {\n      "job_title": "software engineer",\n      "company": "jobly",\n      "start_date": "2023-08-01",\n      "end_date": "N/A",\n      "responsibilities": "software engineer"\n    },\n    {\n      "job_title": "no other experience"\n    }\n  ],\n  "skills": [\n    "c++",\n    "python"\n  ],\n  "certifications": [\n    {\n      "certification_name": "Project manager certificate",\n      "issuing_organization": "Aalto university",\n      "date_issued": "2020-01-01",\n      "expiration_date": "N/A"\n    }\n  ],\n  "desired_job_location": "Helsinki",\n  "desired_job_type": "Full-time",\n  "desired_industry": "ICT",\n  "portfolio_link": "N/A",\n  "linkedin_profile": "https://www.linkedin.com/in/doru-stefan-irimescu/",\n  "resume_link": "N/A"\n}'
incomplete_content_json = json.loads(incomplete_content)
