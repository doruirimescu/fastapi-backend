SCHEMA = {
    "properties": {
        "full_name": {"type": "string"},
        "contact_information": {
            "type": "object",
            "properties": {
                "email": {"type": "string", "format": "email"},
                "phone_number": {"type": "string"}
            },
            "required": ["email"]
        },
        "education": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "degree": {"type": "string"},
                    "field_of_study": {"type": "string"},
                    "institution": {"type": "string"},
                    "graduation_year": {"type": "integer"}
                }
            }
        },
        "work_experience": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "job_title": {"type": "string"},
                    "company": {"type": "string"},
                    "start_date": {"type": "string", "format": "date"},
                    "end_date": {"type": "string", "format": "date"},
                    "responsibilities": {"type": "string"}
                }
            }
        },
        "skills": {
            "type": "array",
            "items": {"type": "string"}
        },
        "certifications": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "certification_name": {"type": "string"},
                    "issuing_organization": {"type": "string"},
                    "date_issued": {"type": "string", "format": "date"},
                    "expiration_date": {"type": "string", "format": "date"}
                }
            }
        },
        "languages": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "language": {"type": "string"},
                    "proficiency_level": {"type": "string"} # e.g. "Native", "Fluent", "Intermediate", "Basic"
                }
            }
        },
        "desired_job_location": {"type": "string"},
        "desired_job_type": {"type": "string"}, # e.g. "Full-time", "Part-time", "Contract", "Temporary"
        "desired_industry": {"type": "string"},
        "portfolio_link": {"type": "string", "format": "uri"},
        "linkedin_profile": {"type": "string", "format": "uri"},
        "resume_link": {"type": "string", "format": "uri"}
    },
    "required": ["full_name", "contact_information", "education", "work_experience"]
}
