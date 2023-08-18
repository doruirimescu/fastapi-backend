from chatbot.summarizer import gather_data_sync
from chatbot.user_model import SCHEMA, JobSeekerProfile
from chatbot.profiler import Profiler
from chatbot.database.wrapper import get_user_profile, store_user_profile
from typing import Optional, Tuple

from langchain.chat_models import ChatOpenAI
from langchain.memory import ChatMessageHistory
from langchain.schema import (
    SystemMessage,
    HumanMessage
)
from enum import Enum
from chatbot.prompt import (
    ORCHESTRATOR_SYSTEM_PROMPT,
    ORCHESTRATOR_INTRO_PROMPT,
    ORCHESTRATOR_PARSE_ACTION_PROMPT
)

class UserAction(str, Enum):
    CREATE_PROFILE = "create_profile"
    FIND_JOB = "find_job"
    UPDATE_PROFILE = "update_profile"
    SEEK_JOB = "seek_job"
    STOP = "stop"


class CurrentState(str, Enum):
    INTRODUCING = "introducing"
    #SANITIZING_INPUT = "sanitizing_input"
    #SANITIZING_FAILED = "sanitizing_failed"
    PROFILING = "profiling"
    SUMMARIZING_PROFILE = "summarizing_profile"
    GENERATING_CV = "generating_cv"
    SCRAPING = "scraping"
    UPDATING_CV = "updating_cv"
    STOP = "stop"


class Orchestrator:
    def __init__(self, username: str) -> None:
        self.username = username
        self.profiler = Profiler()
        self.is_profile_complete = False
        self.is_profile_data_gathered = False
        self.has_user_stopped = False

        self.history, self.llm = self._construct_llm()
        self.current_state = CurrentState.INTRODUCING

    def _construct_llm(self):
        llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
        system_message = SystemMessage(content=ORCHESTRATOR_SYSTEM_PROMPT())
        history = ChatMessageHistory()
        history.add_message(system_message)
        return history, llm

    def introduction(self) -> str:
        print("Generating intro message")
        self.history.add_user_message(ORCHESTRATOR_INTRO_PROMPT())
        return self.llm.predict_messages(self.history.messages).content

    def parse_user_action(self, user_input: str) -> UserAction:
        system_message = SystemMessage(content=ORCHESTRATOR_PARSE_ACTION_PROMPT(UserAction))
        self.history.add_message(system_message)
        self.history.add_user_message(user_input)
        return UserAction(self.llm.predict_messages(self.history.messages).content)

    def orchestrate(self, user_input: Optional[str]) -> Tuple[str, bool]:
        # Should first validate the user input

        if self.current_state == CurrentState.INTRODUCING:
            return self.introduction(user_input)


        # Then, call the profiler for now
        if not self.is_profile_data_gathered:
            if not user_input:
                profiler_reply = self.profiler.profiler_reply()
                if profiler_reply is False:
                    self.is_profile_complete = True
                return profiler_reply, False
            elif user_input == "stop":
                self.has_user_stopped = True
                json_data = gather_data_sync(self.profiler.get_history_string(), SCHEMA)
                print(f"--- JSON DATA: {json_data}")
                jobseeker_profile = JobSeekerProfile(**json_data)
                print(f"--- jobseeker_profile {jobseeker_profile}")
                with open("result.json", "w") as f:
                    f.write(jobseeker_profile.json())
                return "Jobseeker profile created successfully.", True
            else:
                print(f"Calling jobseeker_reply with input: {user_input}")
                self.profiler.jobseeker_reply(user_input)
                return self.profiler.profiler_reply(), False
        return "Profile is complete", True

# o = Orchestrator("test_user")
# print(o.parse_user_action("Hello, I am new here. LEt's seek for a job ?"))

# bot_reply, should_stop = o.orchestrate(None)
# print(f"AI: {bot_reply}")
# while not should_stop:
#     user_input = input("User: ")
#     bot_reply, should_continue = o.orchestrate(user_input)
#     print(f"AI: {bot_reply}")
