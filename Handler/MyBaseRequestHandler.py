from OperationResult import OperationResult
import pymysql


class MyBaseRequestHandler:
    def __init__(self, who, body):
        self.Body = body
        self.User = who

    def Execute(self):
        return OperationResult()

    def GetDBConnection(self):
        return pymysql.connect('localhost','testuser','Password01!','dbo.schema')

