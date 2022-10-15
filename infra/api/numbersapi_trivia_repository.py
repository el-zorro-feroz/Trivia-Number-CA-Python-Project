# NumbersapiTriviaRepository(TriviaRepository)
# UR JOB: Implement Data Source Repository logic (based on numbersapi.com API)
#
# Use http://numbersapi.com/random?json to get random Trivia
# Json Example for this one placed in infra.api.response_examples.random_trivia_response.json
#
# Use http://numbersapi.com/{{number}}?json to get {{number}} specific Trivia
# Json Example for this one placed in infra.api.response_examples.concrete_trivia_response.json
#
# Don`t forget about some errors, like unsupported numbers
# As shown here infra.api.response_examples.bad_trivia_response.json
#
# All requests already processed in Postman (use it for understanding)
# https://app.getpostman.com/join-team?invite_code=b848af27d4d52f3b69f20e5ea88e0fec&target_code=4812c86918ad8e061948e320cebfb42b
#
import requests
import json
from core.entities.trivia_number import TriviaNumber
from core.repositories.trivia_repository import TriviaRepository


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


