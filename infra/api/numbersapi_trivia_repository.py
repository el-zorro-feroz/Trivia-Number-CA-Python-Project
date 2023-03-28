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


class NumbersapiTriviaRepository(TriviaRepository):
    url = "http://numbersapi.com/"

    def get_concrete_num_meaning(self, num: int) -> TriviaNumber:
        req = requests.get(url=self.url+str(num)+"?json")
        json_req = json.loads(req.text)
        trv_num = TriviaNumber()
        trv_num.num = json_req["number"]
        trv_num.meaning = json_req["text"]
        return trv_num

    def get_random_num_meaning(self) -> TriviaNumber:
        req = requests.get(url=self.url+"random?json")
        json_req = json.loads(req.text)
        trv_num = TriviaNumber()
        trv_num.num = json_req["number"]
        trv_num.meaning = json_req["text"]
        return trv_num

