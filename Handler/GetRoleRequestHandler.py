from Handler.MyBaseRequestHandler import MyBaseRequestHandler
from OperationResult import OperationResult


class GetRoleRequestHandler(MyBaseRequestHandler):

    def Execute(self):
        x = self.GetDBConnection().cursor()
        sql = 'select * from `dbo.schema`.`dbo.Users` where name=\'' + self.User + '\''
        x.execute(sql)
        ret = x.fetchall()
        uid = ret[0][0]
        sql = 'select * from `dbo.schema`.`dbo.AdminUsers` where UserId=\'' + str(uid) + '\''
        x.execute(sql)
        ret = x.fetchall()
        if len(ret) > 0:
            return OperationResult(200,'{"role":"Admin"}')
        else:
            sql = 'select * from `dbo.schema`.`dbo.TeamMemberships` where UserId=\'' + str(uid) + '\''
            x.execute(sql)
            ret = x.fetchall()
            if len(ret) > 0:
                if ret[0][3] == 2:
                    return OperationResult(200,'{"role":"TeamLeader"}')
                elif ret[0][3] == 1:
                    return OperationResult(200,'{"role":"TeamMember"}')
                else:
                    return OperationResult(500, 'unknown user role')
        return OperationResult(500, 'user not found')