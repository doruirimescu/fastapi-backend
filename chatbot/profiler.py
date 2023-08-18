
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


class Profiler:
    def __init__(self) -> None:
        self.llm=ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
        self.system_message = SystemMessage(content=PROFILER_SYSTEM_PROMPT(SCHEMA))
        self.history = ChatMessageHistory()
        self.history.add_message(self.system_message)

    def profiler_reply(self):
        reply = self.llm(self.history.messages)
        reply_text = reply.content
        if reply_text == "stop":
            return False
        self.history.add_ai_message(reply_text)
        return reply_text

    def jobseeker_reply(self, reply_text: str) -> bool:
        self.history.add_user_message(reply_text)
        return reply_text

    def get_history(self) -> ChatMessageHistory:
        return self.history

    def get_history_string(self) -> str:
        inp = ""
        for msg in self.get_history().messages[1:-1]:
            text = msg.content
            inp += text
            inp += "\n"
        return inp

#TODO: store and retrieve converstation state from database
# When the profile is complete, the user should be able to say "stop" to end the conversation
# p = Profiler()
# while True:
#     r = p.profiler_reply()
#     if not r:
#         break
#     print(f"Profiler: {r}")
#     reply_text = input("User: ")
#     if reply_text == "stop":
#         break
#     r = p.jobseeker_reply()
#     if not r:
#         break
# # Dump chat messages to file
# with open("chat_history.txt", "w") as f:
#     for msg in p.get_history():
#         f.write(f"{msg.content}\n")

# inp = ""
# for msg in p.get_history()[1:]:
#     text = msg.content
#     inp +=text
#     inp += "\n"

# from chatbot.summarizer import gather_data_sync
# result = gather_data_sync(inp, SCHEMA)
# print(result)

#TODO: should we store the result in a database?
