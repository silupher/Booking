from Handler.MyBaseRequestHandler import MyBaseRequestHandler
from CookieUtility import CookieUtility
from OperationResult import OperationResult
from Model.CookieClass import CookieClass
import json
import hashlib


class LoginRequestHandler(MyBaseRequestHandler):

    def Execute(self):
            cred = json.loads(self.Body)
            x = self.GetDBConnection().cursor()
            credHash = hashlib.md5(cred['credential'].encode()).hexdigest()
            sql = 'select * from `dbo.schema`.`dbo.Users` where name=\'' + cred['name']+'\' and password=\''+credHash+'\';'
            x.execute(sql)
            ret = x.fetchall()
            o = CookieClass(ret[0][1],'now')
            cookie = CookieUtility.CreateCookie(o.ToJson())
            return OperationResult(200, '{"cookie":"' + cookie+'"}')
