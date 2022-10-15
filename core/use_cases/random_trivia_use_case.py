# RandomTriviaUseCase(UseCase)
# UR JOB: Create UseCase for retrievin` random Trivia Numbers
from core.use_case import UseCaseRequest, UseCaseResponse, UseCase
from core.entities.trivia_number import TriviaNumber
from core.repositories.trivia_repository import TriviaRepository
from core.failures.num_parc_failure import NumParsFailure


class RndTriviaNumUseCaseRequest(UseCaseRequest):
    pass


class RndTriviaNumUseCaseResponse(UseCaseResponse):
    data: TriviaNumber


class RndTriviaNumUseCase(UseCase):
    def call(self, request: RndTriviaNumUseCaseRequest) -> RndTriviaNumUseCaseResponse:
        _response = RndTriviaNumUseCaseResponse()
        _repository: TriviaRepository = None

        rnd_entity: TriviaNumber = _repository.get_random_num_meaning()
        _response.data = rnd_entity

        if rnd_entity is None:
            _response.error = NumParsFailure()

        return _response


