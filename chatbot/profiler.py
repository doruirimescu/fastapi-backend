
from langchain.chat_models import ChatOpenAI
from chatbot.prompt import PROFILER_SYSTEM_PROMPT
from langchain.schema import (
    SystemMessage,
    HumanMessage
    )
from langchain.memory import ChatMessageHistory
from typing import Optional
from dotenv import load_dotenv

load_dotenv()


class Profiler:
    def __init__(self, schema) -> None:
        self.llm=ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
        self.system_message = SystemMessage(content=PROFILER_SYSTEM_PROMPT(schema))
        self.history = ChatMessageHistory()
        self.history.add_message(self.system_message)

    def reply(self, input: str) -> Optional[str]:
        input = input.lower()
        self.history.add_user_message(input)
        reply = self.llm(self.history.messages)
        reply_text = reply.content
        if reply_text == "stop":
            return False
        self.history.add_ai_message(reply_text)
        return reply_text

    def get_history(self) -> ChatMessageHistory:
        return self.history

    def get_history_string(self) -> str:
        inp = ""
        print(self.get_history().messages)
        for msg in self.get_history().messages[1:-1]:
            text = msg.content
            inp += text
            inp += "\n"
        return inp
