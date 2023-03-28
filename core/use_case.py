#   Title: Trivia-Number-CA-Python-Project
#   Author: Savin, V
#   Date: 2023
#   Code version: 1.0.1.1
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


from abc import ABC, abstractmethod
from core.failure import Failure


class UseCaseRequest(ABC):
    """ ABC UseCase Request """

    """ 
    Used for declarin` UseCase Request parameters in Subclasses 
    
    For Example: Request Class for parameters for changin` Name by User ID 
    
    class ChangeUsernameUseCaseRequest(UseCaseRequest):
        id: uuid = None  # User ID who`ll have replaced Name
        name: str = None  # new Name for User
    
    """


class UseCaseResponse(ABC):
    """ ABC UseCase Response """

    """
    Used for receivin` UseCase Response (Results)
    
    For Example: Response Class for result of changin` Name by User ID 
    
    class ChangeUsernameUseCaseResponse(UseCaseResponse):
        data: User = None  # Here we change Type for data variable we need to get by UseCase
        
    """

    data: object = None
    error: Failure = None

    @property
    def is_success(self):
        """ Checkin` for the success of the response. Can be overridden for specific tests """
        return self.error is None or self.data is not None


class UseCase(ABC):
    """ ABC UseCase """

    """
    Used for creatin` request and retrievin` some data or error handle 
    
    For example: UseCase for change Username by them ID
    
    class ChangeUsernameUseCase(UseCase):
        server_repository: ServerRepository = SC02ServerRepository()  # Declarin` our server repository
        
        def call(self, request: UseCaseRequest) -> UseCaseResponse:
            _response: ChangeUsernameUseCaseResponse = None  # Declarin` variable for future server response
            
            if request.id is not Null:  # Doin` validation test for User ID 
                _data = self.server_repository.change_username(id = request.id, name = request.name)
                # Makin` repository request and gettin` some data from it
                
                if _data is not Null:  # Doin` validation test for retrieved data and settin` data in UseCase Response 
                    _response.data = _data
                else:  # Settin` Response Error if data is`t valid
                    _response.error = ServerFailure()
                    
            else:  # Same for server response data validation, if User ID isn`t valid, sendin` correct error in response
                _response = ChangeUsernameUseCaseResponse()
                _response.error = InvalidIDFailure()
                
            return _response  # Sendin` final result of UseCase
    """

    @abstractmethod
    def call(self, request: UseCaseRequest) -> UseCaseResponse:
        """ Base UseCase Method. Must be overriden for declarin` UseCase logic """
        return NotImplemented

