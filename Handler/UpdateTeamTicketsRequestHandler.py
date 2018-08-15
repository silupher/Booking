from Handler.MyBaseRequestHandler import MyBaseRequestHandler
from OperationResult import OperationResult
import json
import datetime


class UpdateTeamTicketsRequestHandler(MyBaseRequestHandler):

    def Execute(self):
        data = json.loads(self.Body)
        teamId = data['data']['teamId']
        tickets = data['data']['tickets']
        con = self.GetDBConnection()
        x = con.cursor()
        isProd = 1
        hardMonth=''
        sql = 'select * from `dbo.schema`.`dbo.SystemConfigurations`'
        x.execute(sql)
        ret = x.fetchall()
        env = ''
        if len(ret) > 0:
            index = 0
            while index < len(ret):
                if ret[index][0] == 'Environment' and ret[index][1] != 'Production':
                    isProd = 0
                elif ret[index][0] == 'Date':
                    hardMonth = ret[index][1]
                index = index + 1
        if isProd == 1:
            hardMonth = datetime.datetime.now().year + datetime.datetime.now().month+datetime.datetime.now().day
        sql = 'select * from `dbo.schema`.`dbo.Users` where name=\'' + self.User + '\''
        x.execute(sql)
        ret = x.fetchall()
        uid = ret[0][0]
        sql = 'select TeamId from `dbo.schema`.`dbo.TeamMemberships` where UserId=\'' + str(uid) + '\' and RoleId=\'2\''
        x.execute(sql)
        ret = x.fetchall()
        sql = 'select * from `dbo.schema`.`dbo.Teams` where Id='+ str(ret[0][0])
        x.execute(sql)
        ret = x.fetchall()
        index = 0
        hasPermission = 0
        while index < len(ret):
            if teamId != str(ret[index][0]):
                index = index + 1
                continue
            if int(hardMonth[6:]) > 5:
                return OperationResult(500, 'Locked from 5th every month')
            hasPermission = 1
            break
        if hasPermission == 1:
            sql = 'update `dbo.schema`.`dbo.Tickets` set Tickets='+str(tickets)+' where TeamId=\'' + teamId + '\' and Month=\''+hardMonth[:6]+'\''
            x.execute(sql)
            ret = x.fetchall()
            con.commit()
            return OperationResult(200,'')
        else:
            return OperationResult(500, 'no permission')