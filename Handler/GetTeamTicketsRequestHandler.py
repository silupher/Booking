from Handler.MyBaseRequestHandler import MyBaseRequestHandler
from OperationResult import OperationResult
import datetime
import json


class GetTeamTicketsRequestHandler(MyBaseRequestHandler):

    def Execute(self):
        x = self.GetDBConnection().cursor()
        data = json.loads(self.Body)['data']
        teamId=''
        if data != '' and data['teamId'] != None:
            teamId = data['teamId']
        isProd = 1
        hardMonth=''
        sql = 'select * from `dbo.schema`.`dbo.SystemConfigurations`'
        x.execute(sql)
        ret = x.fetchall()
        env = '';
        if len(ret) > 0:
            index = 0
            while index < len(ret):
                if ret[index][0] == 'Environment' and ret[index][1] != 'Production':
                    isProd = 0
                elif ret[index][0] == 'Date':
                    hardMonth = ret[index][1][:6]
                index = index + 1
        if isProd == 1:
            hardMonth = datetime.datetime.now().year + datetime.datetime.now().month
        isAdmin = 0
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
            if teamId != '' and str(ret[index][0]) != teamId:
                index = index + 1
                continue
            tickSql = 'select Tickets from `dbo.schema`.`dbo.Tickets` where TeamId=\'' + str(ret[index][0]) + '\' and Month=\'' +hardMonth+ '\''
            x.execute(tickSql)
            tickRet = x.fetchall()
            output = output + '{"id":"'+str(ret[index][0])+'", "team":"' + ret[index][1] + '", "tickets":"'+str(tickRet[0][0])+'"}'
            if index is not (len(ret) - 1) and teamId == '':
                output = output + ','
            index = index + 1
        output = output + ']'
        return OperationResult(200,output)