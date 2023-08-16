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

# from chatbot.user_model import JobSeekerProfile
# # Use result to create a JobSeekerProfile object
# profile = JobSeekerProfile(**expected_result)
# print(profile)
