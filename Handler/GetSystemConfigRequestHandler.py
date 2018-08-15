from Handler.MyBaseRequestHandler import MyBaseRequestHandler
from OperationResult import OperationResult


class GetSystemConfigRequestHandler(MyBaseRequestHandler):

    def Execute(self):
        x = self.GetDBConnection().cursor()
        sql = 'select * from `dbo.schema`.`dbo.SystemConfigurations`'
        x.execute(sql)
        ret = x.fetchall()
        hardDate = '';
        env = '';
        if len(ret) > 0:
            index = 0
            while index < len(ret):
                if ret[index][0] == 'Date':
                    hardDate = ret[index][1]
                elif ret[index][0] == 'Environment':
                    env = ret[index][1]
                index = index + 1
            return OperationResult(200, '{"Date":"'+hardDate+'","Env":"'+env+'"}')
        return OperationResult(500, 'nothing')