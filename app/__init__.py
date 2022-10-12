from app.controllers.test_controller import TestController


def run():
    _controller = TestController()

    _controller.trivia_use_case_test()
    _controller.concrete_trivia_use_case_test(4)
