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


