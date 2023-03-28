#   Title: Trivia-Number-CA-Python-Project
#   Author: Savin, V
#   Date: 2023
#   Code version: 1.0.1
#   Type: source code
#   Web address: https://github.com/pocket-red-fox
#   License: MIT License
#   
#   Copyright (c) 2023, Savin, V
#   
#   Permission is hereby granted, free of charge, to any person obtaining a copy of
#   this software and associated documentation files (the "Software"), to deal in
#   the Software without restriction, including without limitation the rights to
#   use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
#   of the Software, and to permit persons to whom the Software is furnished to do
#   so, subject to the following conditions:
#   
#   The above copyright notice and this permission notice shall be included in
#   all copies or substantial portions of the Software.
#   
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#   THE SOFTWARE.


from core.use_case import UseCaseRequest, UseCaseResponse, UseCase
from core.entities.trivia_number import TriviaNumber
from core.repositories.trivia_repository import TriviaRepository
from core.failures.num_parc_failure import NumParsFailure
from infra.api.numbersapi_trivia_repository import NumbersapiTriviaRepository


class RndTriviaNumUseCaseRequest(UseCaseRequest):
    pass


class RndTriviaNumUseCaseResponse(UseCaseResponse):
    data: TriviaNumber


class RndTriviaNumUseCase(UseCase):
    def call(self, request: RndTriviaNumUseCaseRequest) -> RndTriviaNumUseCaseResponse:
        _response = RndTriviaNumUseCaseResponse()
        _repository: TriviaRepository = NumbersapiTriviaRepository()

        rnd_entity: TriviaNumber = _repository.get_random_num_meaning()
        _response.data = rnd_entity

        if rnd_entity is None:
            _response.error = NumParsFailure()

        return _response

