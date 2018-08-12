from Handler.MyBaseRequestHandler import MyBaseRequestHandler
from CookieUtility import CookieUtility
from OperationResult import OperationResult
from Model.CookieClass import CookieClass
import json


class LoginRequestHandler(MyBaseRequestHandler):

    def Execute(self):
            cred = json.loads(self.Body)
            x = self.GetDBConnection().cursor()
            sql = 'select * from `dbo.schema`.`dbo.Users` where name=\'' + cred['name']+'\' and password=\''+cred['credential']+'\';'
            x.execute(sql)
            ret = x.fetchall()
            o = CookieClass(ret[0][1],'now')
            cookie = CookieUtility.CreateCookie(o.ToJson())
            return OperationResult(200, '{"cookie":"' + cookie+'"}')
