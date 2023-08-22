from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage
from langchain.memory import ChatMessageHistory
import json
from chatbot.prompt import SUMMARIZER_SYSTEM_PROMPT, SUMMARIZER_SYSTEM_PROMPT_2
from dotenv import load_dotenv
load_dotenv()

class Summarizer:
    def __init__(self, schema) -> None:
        self.llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
        system_message = SystemMessage(content=SUMMARIZER_SYSTEM_PROMPT_2(schema))
        self.history = ChatMessageHistory()
        self.history.add_message(system_message)

    # Run chain
    async def areply(self, input: str):
        self.history.add_user_message(input)
        result = await self.llm.apredict_messages(self.history.messages)
        return json.loads(result.content)

    def reply(self, input: str):
        input = input.lower()
        print(input)
        self.history.add_user_message(input)
        result_text = self.llm.predict_messages(self.history.messages).content.lower()
        print(json.dumps(json.loads(result_text), indent=4))
        return json.loads(result_text)
