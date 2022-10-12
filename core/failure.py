from abc import ABC


class Failure(ABC):
    """ ABC Failure. Used for separation of different fails """

    error_message: str = None
    