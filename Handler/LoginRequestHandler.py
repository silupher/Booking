from Handler.MyBaseRequestHandler import MyBaseRequestHandler
from CookieUtility import CookieUtility
from OperationResult import OperationResult
from Model.CookieClass import CookieClass


class LoginRequestHandler(MyBaseRequestHandler):

    def Execute(self):
            o = CookieClass('yuqingz','now')
            cookie = CookieUtility.CreateCookie(o.ToJson())
            return OperationResult(200, '{"cookie":"' + cookie+'"}')
