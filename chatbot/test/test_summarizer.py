import unittest
from chatbot.test.data import valid_data
from chatbot.test.incomplete_education import incomplete_education, incomplete_education_json
from chatbot.test.incomplete_work_experience import incomplete_work_experience, incomplete_work_experience_json
from chatbot.test.invalid_desired_job_type import invliad_desired_job_type, invliad_desired_job_type_json

from chatbot.summarizer import Summarizer
from chatbot.user_model import JobSeekerProfile, SCHEMA
from dotenv import load_dotenv
load_dotenv()
import pydantic

class TestSummarizer(unittest.TestCase):
    def test_summarize_valid_data(self):
        s = Summarizer(SCHEMA)
        result = s.reply(valid_data)
        self.assertIsInstance(result, dict)
        JobSeekerProfile(**result)

    def test_summarize_incomplete_education(self):
        s = Summarizer(SCHEMA)
        result = s.reply(incomplete_education)
        # self.assertEqual(incomplete_education_json, result)

        JobSeekerProfile(**result)

    def test_summarize_incomplete_work_experience(self):
        s = Summarizer(SCHEMA)
        result = s.reply(incomplete_work_experience)
        # self.assertEqual(incomplete_work_experience_json, result)
        # Generated jsons differ sometimes from call to call, so we can't compare them

        JobSeekerProfile(**result)

    def test_summarize_invalid_desired_job_type(self):
        s = Summarizer(SCHEMA)
        result = s.reply(invliad_desired_job_type)
        # self.assertEqual(invliad_desired_job_type_json, result)

        JobSeekerProfile(**result)
