
from langchain.chat_models import ChatOpenAI
from chatbot.prompt import PROFILER_SYSTEM_PROMPT
from langchain.schema import (
    SystemMessage,
    HumanMessage
    )
from chatbot.user_model import SCHEMA
from langchain.memory import ChatMessageHistory
from dotenv import load_dotenv

load_dotenv()


llm=ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

system_message = SystemMessage(content=PROFILER_SYSTEM_PROMPT)
history = ChatMessageHistory()
history.add_message(system_message)


def profiler_reply():
    reply = llm(history.messages)
    reply_text = reply.content
    if reply_text == "stop":
        return False
    history.add_ai_message(reply_text)
    return reply_text


def jobseeker_reply() -> bool:
    reply_text = input("User: ")
    if reply_text == "stop":
        return False
    history.add_user_message(reply_text)
    return reply_text

#TODO: store and retrieve converstation state from database
# When the profile is complete, the user should be able to say "stop" to end the conversation

while True:
    r = profiler_reply()
    if not r:
        break
    print(f"Profiler: {r}")
    r = jobseeker_reply()
    if not r:
        break
# Dump chat messages to file
with open("chat_history.txt", "w") as f:
    for msg in history.messages:
        f.write(f"{msg.content}\n")

inp = ""
for msg in history.messages[1:]:
    text = msg.content
    inp +=text
    inp += "\n"

from chatbot.summarizer import gather_data_sync
result = gather_data_sync(inp, SCHEMA)
print(result)

#TODO: should we store the result in a database?
