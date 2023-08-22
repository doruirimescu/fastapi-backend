
from chatbot.user_model import SCHEMA, JobSeekerProfile
from chatbot.database.wrapper import get_user_profile, store_user_profile
from chatbot.profiler import Profiler
from chatbot.summarizer import Summarizer

from chatbot.action_selector import ActionSelector
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
)


class UserAction(str, Enum):
    INTRODUCE = "introduce"
    CREATE_PROFILE = "create_profile"
    FIND_JOB = "find_job"
    UPDATE_PROFILE = "update_profile"
    UPDATE_CV = "update_cv"
    SEEK_JOB = "seek_job"
    GENERATE = "generate_cv"
    STOP = "stop"


class CurrentState(str, Enum):
    INTRODUCE = "introduce"
    CREATE_PROFILE = "create_profile"
    FIND_JOB = "find_job"
    UPDATE_PROFILE = "update_profile"
    UPDATE_CV = "update_cv"
    SEEK_JOB = "seek_job"
    GENERATE = "generate_cv"
    STOP = "stop"
    PARSE_NEXT_ACTION = "parse_next_action"


class Orchestrator:
    def __init__(self, username: str) -> None:
        self.username = username
        self.profiler = Profiler(SCHEMA)
        self.action_selector = ActionSelector(UserAction)
        self.summarizer = Summarizer(SCHEMA)
        self.history, self.llm = self._construct_llm()
        self.current_state = CurrentState.INTRODUCE

    def _construct_llm(self):
        llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
        system_message = SystemMessage(content=ORCHESTRATOR_SYSTEM_PROMPT())
        history = ChatMessageHistory()
        history.add_message(system_message)
        return history, llm

    def introduction(self) -> str:
        print("Generating intro message")
        does_user_profile_exist = get_user_profile(self.username)
        self.history.add_user_message(ORCHESTRATOR_INTRO_PROMPT(does_user_profile_exist))
        return self.llm.predict_messages(self.history.messages).content

    def reply(self, user_input: Optional[str]) -> Tuple[str, bool]:
        # Should first validate the user input
        print(f"--- CURRENT STATE {self.current_state} ---")
        print(f"--- USER INPUT {user_input} ---")

        if self.current_state == CurrentState.PARSE_NEXT_ACTION:
            self.history.add_user_message(user_input)
            next_action = self.action_selector.reply(self.history)
            self.current_state = CurrentState(next_action)

        if self.current_state == CurrentState.INTRODUCE:
            self.current_state = CurrentState.PARSE_NEXT_ACTION
            return self.introduction(), False

        #TODO: switch bsed on current state

        # Then, call the profiler for now
        if self.current_state == CurrentState.CREATE_PROFILE:
            if user_input == "stop":
                return self.summarize_profile()
            else:
                bot_reply = self.profiler.reply(user_input)
                if "your profile is complete" in bot_reply.lower():
                    print("Summarizing profile")
                    return self.summarize_profile()
                return bot_reply, False
        return "Unknown action", True

    def summarize_profile(self):
        profiler_chat_history = self.profiler.get_history_string()
        json_data = self.summarizer.reply(profiler_chat_history)
        print(f"--- JSON DATA: {json_data}")
        try:
            jobseeker_profile = JobSeekerProfile(**json_data)
            print(f"--- jobseeker_profile {jobseeker_profile}")
            with open("result.json", "w") as f:
                f.write(jobseeker_profile.json())
            self.current_state = CurrentState.STOP
            return "Jobseeker profile created successfully.", True
        except Exception as e:
            print(f"--- ERROR: {e}")
            inp = f"Error creating jobseeker profile: {e} \n"
            inp = f"Explain the error \n"
            inp += f"Ask the relevant questions again. \n"
            inp += f"Reply with 'stop' when the questions are answered."
            return self.profiler.reply(inp), False
