from core.failure import Failure


class NetworkFailure(Failure):
    error_message = "Server Not Response"


class ServerFailure(Failure):
    error_message = "Response was interrupted by Server"
