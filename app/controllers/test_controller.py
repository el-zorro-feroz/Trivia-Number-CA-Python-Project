from core.use_cases.random_trivia_use_case import RndTriviaNumUseCase, RndTriviaNumUseCaseResponse, RndTriviaNumUseCaseRequest
from core.use_cases.specific_trivia_use_case import SpecificTrvUseCase, SpecificTrvUseCaseResponse, SpecificTrvUseCaseRequest


class TestController:
    random_trivia_use_case = RndTriviaNumUseCase()
    specific_trivia_use_case = SpecificTrvUseCase()

    def trivia_use_case_test(self):
        print("\nRandom Trivia Number Test ")

        _request = RndTriviaNumUseCaseRequest()
        _response: RndTriviaNumUseCaseResponse = self.random_trivia_use_case.call(request=_request)

        if _response.is_success:
            print(f"Random Trivia: {_response.data.meaning}\n")
        else:
            print(f"Smth wrong with random Trivia number request")

    def concrete_trivia_use_case_test(self, number):
        print(f"Trivia Number {number} Test ")

        _request = SpecificTrvUseCaseRequest()
        _request.num = number
        _response: SpecificTrvUseCaseResponse = self.specific_trivia_use_case.call(request=_request)

        if _response.is_success:
            print(f"Trivia for number {number}: {_response.data.meaning}")
        else:
            print(f"Smth wrong with Trivia number request")
