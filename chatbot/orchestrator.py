
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
    PARSING_NEXT_ACTION = "parsing_action"
    SUMMARIZING_PROFILE = "summarizing_profile"
    GENERATING_CV = "generating_cv"
    SCRAPING = "scraping"
    UPDATING_CV = "updating_cv"
    STOP = "stop"

def action_to_state(action: UserAction) -> CurrentState:
    if action == UserAction.CREATE_PROFILE:
        return CurrentState.PROFILING
    elif action == UserAction.FIND_JOB:
        return CurrentState.SCRAPING
    elif action == UserAction.UPDATE_PROFILE:
        return CurrentState.UPDATING_CV
    elif action == UserAction.SEEK_JOB:
        return CurrentState.SCRAPING
    elif action == UserAction.STOP:
        return CurrentState.STOP
    else:
        raise ValueError(f"Unknown action: {action}")

class Orchestrator:
    def __init__(self, username: str) -> None:
        self.username = username
        self.profiler = Profiler(SCHEMA)
        self.action_selector = ActionSelector(UserAction)
        self.summarizer = Summarizer(SCHEMA)
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

    def orchestrate(self, user_input: Optional[str]) -> Tuple[str, bool]:
        # Should first validate the user input
        print(f"--- CURRENT STATE {self.current_state} ---")
        print(f"--- USER INPUT {user_input} ---")
        if self.current_state == CurrentState.INTRODUCING:
            self.current_state = CurrentState.PARSING_NEXT_ACTION
            return self.introduction(), False

        if self.current_state == CurrentState.PARSING_NEXT_ACTION:
            next_action = self.action_selector.reply(user_input)
            self.current_state = action_to_state(next_action)

        #TODO: switch bsed on current state

        # Then, call the profiler for now
        if self.current_state == CurrentState.PROFILING:
            if user_input == "stop":
                try:
                    profiler_chat_history = self.profiler.get_history_string()
                    json_data = self.summarizer.reply(profiler_chat_history)
                    print(f"--- JSON DATA: {json_data}")
                    jobseeker_profile = JobSeekerProfile(**json_data)
                    print(f"--- jobseeker_profile {jobseeker_profile}")
                    with open("result.json", "w") as f:
                        f.write(jobseeker_profile.json())
                    self.current_state = CurrentState.STOP
                    return "Jobseeker profile created successfully.", True
                except Exception as e:
                    print(f"--- ERROR: {e}")
                    self.current_state = CurrentState.INTRODUCING
                return "Error creating jobseeker profile. Please try again.", True
            else:
                return self.profiler.reply(user_input), False
        return "Profile is complete", True
