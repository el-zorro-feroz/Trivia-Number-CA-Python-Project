# TriviaRepository
# UR JOB: Create Repository Interface for future Data Sources
from abc import abstractmethod, ABC
from requests import get
from core.entities.trivia_number import TriviaNumber


class TriviaRepository:

    @abstractmethod
    def get_concrete_num_meaning(self) -> TriviaNumber:
        return NotImplemented

    @abstractmethod
    def get_random_num_meaning(self) -> TriviaNumber:
        return NotImplemented
