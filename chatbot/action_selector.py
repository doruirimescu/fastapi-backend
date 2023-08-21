
from langchain.chat_models import ChatOpenAI
from chatbot.prompt import ACTION_SELECTOR_PROMPT
from langchain.schema import (
    SystemMessage,
    HumanMessage
    )
from langchain.memory import ChatMessageHistory


class ActionSelector:
    def __init__(self, enum) -> None:
        self.llm=ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
        self.system_message = SystemMessage(content=ACTION_SELECTOR_PROMPT(enum))
        self.history = ChatMessageHistory()
        self.history.add_message(self.system_message)

    def reply(self, input: ChatMessageHistory) -> str:
        for i in input.messages:
            self.history.add_message(i)
        reply_text = self.llm.predict_messages(self.history.messages).content

        for i in range(len(input.messages)):
            self.history.messages.pop()
        return reply_text
