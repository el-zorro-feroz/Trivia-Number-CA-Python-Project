from core.failure import Failure


class NotEnteredFailure(Failure):
    error_message = "Хорошее число не введено, давай по новой"


class LowerThenNullFailure(Failure):
    error_message = "Миша, всё плохо, давай по новой, число меньше 0"
