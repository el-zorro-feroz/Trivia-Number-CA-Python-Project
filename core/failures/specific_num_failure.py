from core.failure import Failure


class NotEnteredFailure(Failure):
    error_message = "The number is not entered"


class LowerThenNullFailure(Failure):
    error_message = "The specified number is less than 0"
