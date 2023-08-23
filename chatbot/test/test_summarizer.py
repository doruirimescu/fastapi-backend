import unittest
from chatbot.test.data import valid_data
from chatbot.test.incomplete_education import incomplete_education
from chatbot.test.incomplete_work_experience import incomplete_work_experience
from chatbot.test.invalid_desired_job_type import invliad_desired_job_type

from chatbot.summarizer import Summarizer
from chatbot.user_model import JobSeekerProfile, SCHEMA
import pytest
from dotenv import load_dotenv
load_dotenv()

#TODO: dump generated JobSeekerProfile into jsons, and use them to test the summarizer
class TestSummarizer(unittest.TestCase):
    @pytest.mark.timeout(60)
    def test_summarize_valid_data(self):
        s = Summarizer(SCHEMA)
        result = s.reply(valid_data)
        self.assertIsInstance(result, dict)
        JobSeekerProfile(**result)

    @pytest.mark.timeout(60)
    def test_summarize_incomplete_education(self):
        s = Summarizer(SCHEMA)
        result = s.reply(incomplete_education)

        JobSeekerProfile(**result)

    @pytest.mark.timeout(60)
    def test_summarize_incomplete_work_experience(self):
        s = Summarizer(SCHEMA)
        result = s.reply(incomplete_work_experience)

        JobSeekerProfile(**result)

    @pytest.mark.timeout(60)
    def test_summarize_invalid_desired_job_type(self):
        s = Summarizer(SCHEMA)
        result = s.reply(invliad_desired_job_type)

        JobSeekerProfile(**result)
