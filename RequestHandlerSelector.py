from Handler.LoginRequestHandler import LoginRequestHandler
from Handler.GetTeamsRequestHandler import GetTeamsRequestHandler
from Handler.GetRoleRequestHandler import GetRoleRequestHandler
from Handler.GetSystemConfigRequestHandler import GetSystemConfigRequestHandler
from Handler.GetTeamTicketsRequestHandler import GetTeamTicketsRequestHandler
from Handler.UpdateTeamTicketsRequestHandler import UpdateTeamTicketsRequestHandler
from CookieUtility import CookieUtility
from Model.CookieClass import CookieClass
import re
import json


def CreateRequestHandler(queryPath, method, body, cookie):
    strs = re.split(r'[/()\]]', queryPath)
    if strs[0] == 'login' and method == 'POST':
        return LoginRequestHandler(None, body)

    # if cookie is None:
    #     raise Exception('no cookie for non-login operation')

    if body is None:
        raise Exception('no body for operation detail')

    opDetail = json.loads(body)

    cookie = opDetail['cookie']

    data = opDetail['data']

    operation = opDetail['operation']

    parsedCookie = CookieClass.FromJson(CookieUtility.ParseCookie(cookie))

    user = parsedCookie.User

    if strs[0] == 'teams' and operation == 'get':
        return GetTeamsRequestHandler(user, None)
    elif strs[0] == 'role' and operation == 'get':
        return GetRoleRequestHandler(user, None)
    elif strs[0] == 'tickets' and operation == 'get':
        return GetTeamTicketsRequestHandler(user, body)
    elif strs[0] == 'updatetickets' and operation == 'post':
        return UpdateTeamTicketsRequestHandler(user, body)
    elif strs[0] == 'sys' and operation == 'get':
        return GetSystemConfigRequestHandler(user, None)

    raise Exception('Unsupported operation')

