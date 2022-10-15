# SpecificTriviaUseCase(UseCase)
# UR JOB: Create UseCase for retrievin` specific Trivia Numbers
from core.use_case import UseCaseRequest, UseCaseResponse, UseCase
from core.entities.trivia_number import TriviaNumber
from core.repositories.trivia_repository import TriviaRepository
from core.failures.specific_num_failure import LowerThenNullFailure, NotEnteredFailure
from core.failures.num_parc_failure import NumParsFailure
from infra.api.numbersapi_trivia_repository import NumbersapiTriviaRepository


class SpecificTrvUseCaseRequest(UseCaseRequest):
    num: int = None


class SpecificTrvUseCaseResponse(UseCaseResponse):
    data: TriviaNumber


class SpecificTrvUseCase(UseCase):
    def call(self, request: SpecificTrvUseCaseRequest) -> SpecificTrvUseCaseResponse:
        _repository: TriviaRepository = NumbersapiTriviaRepository()
        _response = SpecificTrvUseCaseResponse()

        if request.num is None:
            _response.error = NotEnteredFailure()
        elif request.num >= 0:
            _response.data = _repository.get_concrete_num_meaning(request.num)
            if _response.data is None:
                _response.error = NumParsFailure()
        else:
            _response.error = LowerThenNullFailure()

        return _response

