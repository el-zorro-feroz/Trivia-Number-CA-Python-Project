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

