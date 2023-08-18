import json
from chatbot.user_model import JobSeekerProfile
from typing import List, Optional
import os


def get_user_profile(username: str) -> Optional[JobSeekerProfile]:
    if not os.path.exists(f"database/data/{username}.json"):
        return None
    with open(f"database/data/{username}.json", "r") as f:
        data = json.load(f)
        return JobSeekerProfile(**data)


def store_user_profile(username: str, profile: JobSeekerProfile) -> None:
    with open(f"database/data/{username}.json", "w") as f:
        f.write(profile.json())
