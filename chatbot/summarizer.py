from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage
from langchain.memory import ChatMessageHistory
from dotenv import load_dotenv
from typing import Tuple
import json
from chatbot.prompt import SUMMARIZER_SYSTEM_PROMPT

load_dotenv()


def construct_llm(inp: str, schema: dict) -> Tuple[ChatMessageHistory, ChatOpenAI]:
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    system_message = SystemMessage(content=SUMMARIZER_SYSTEM_PROMPT(schema))
    history = ChatMessageHistory()
    history.add_message(system_message)
    history.add_user_message(inp)
    return history, llm

# Run chain
async def gather_data_async(inp: str, schema):
    history, llm = construct_llm(inp, schema)
    result = await llm.apredict_messages(history.messages)
    return json.loads(result.content)


def gather_data_sync(inp: str, schema):
    history, llm = construct_llm(inp, schema)
    result = llm.predict_messages(history.messages)
    return json.loads(result.content)

"""Example usage"""
# from chatbot.user_model import SCHEMA, JobSeekerProfile
# from chatbot.test.data import input_data
# result = gather_data_sync(input_data, SCHEMA)
# print(result)


# profile_json = JobSeekerProfile(**result)
# # dump pydantic to file
# with open("result.json", "w") as f:
#     f.write(profile_json.json())

# TODO: store the result in a database
