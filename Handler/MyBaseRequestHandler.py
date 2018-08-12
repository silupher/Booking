from OperationResult import OperationResult


class MyBaseRequestHandler:
    def __init__(self, who, body):
        self.Body = body
        self.User = who

    def Execute(self):
        return OperationResult()
