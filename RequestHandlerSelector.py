from Handler.LoginRequestHandler import LoginRequestHandler
from CookieUtility import CookieUtility
from Model.CookieClass import CookieClass
import re


def CreateRequestHandler(queryPath, method, body, cookie):
    strs = re.split(r'[/()\]]', queryPath)
    if strs[0] == 'login' and method == 'POST':
        return LoginRequestHandler(None, body)

    if cookie is None:
        raise Exception('no cookie for non-login operation')

    parsedCookie = CookieClass.FromJson(CookieUtility.ParseCookie(cookie))

    raise Exception('Unsupported operation')

