# UR JOB: Write Abstract UseCase logic for ur UseCases
# Use comments as an abstract example
# Try to run app and get valid tests


class TestController:
    # random_trivia_use_case = UseCase()
    # specific_trivia_use_case = UseCase()

    def trivia_use_case_test(self):
        print("Random Trivia Number Test \n")

        # _request: UseCaseRequest = UseCaseRequest()
        # _response: UseCaseResponse = self.random_trivia_use_case.call(request=_request)
        #
        # if _response.is_success:
        #     print(f"Random Trivia: {_response.data}")
        # else:
        #     print(f"Smth wrong with random Trivia number request")

    def concrete_trivia_use_case_test(self, number):
        print(f"Trivia Number {number} Test \n")

        # _request: UseCaseRequest = UseCaseRequest()
        # _response: UseCaseResponse = self.specific_trivia_use_case.call(request=_request)
        #
        # if _response.is_success:
        #     print(f"Trivia for number {number}: {_response.data}")
        # else:
        #     print(f"Smth wrong with Trivia number request")
