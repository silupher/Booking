from Handler.MyBaseRequestHandler import MyBaseRequestHandler
from OperationResult import OperationResult


class GetTeamsRequestHandler(MyBaseRequestHandler):

    def Execute(self):
        x = self.GetDBConnection().cursor()
        sql = 'select * from `dbo.schema`.`dbo.Users` where name=\'' + self.User + '\''
        x.execute(sql)
        ret = x.fetchall()
        uid = ret[0][0]
        sql = 'select * from `dbo.schema`.`dbo.AdminUsers` where UserId=\'' + str(uid) + '\''
        x.execute(sql)
        ret = x.fetchall()
        output = '['
        if len(ret) > 0:
            sql = 'select * from `dbo.schema`.`dbo.Teams`'
            x.execute(sql)
            ret = x.fetchall()

        else:
            sql = 'select TeamId from `dbo.schema`.`dbo.TeamMemberships` where UserId=\'' + str(uid) + '\''
            x.execute(sql)
            ret = x.fetchall()
            sql = 'select * from `dbo.schema`.`dbo.Teams` where Id='+ str(ret[0][0])
            x.execute(sql)
            ret = x.fetchall()
        index = 0
        while index < len(ret):
            output = output + '{"id":"'+str(ret[index][0])+'", "name":"' + ret[index][1] + '"}'
            if index is not (len(ret) - 1):
                output = output + ','
            index = index + 1
        output = output + ']'
        return OperationResult(200,output)