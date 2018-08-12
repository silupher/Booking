import json


class CookieClass:
    def __init__(self, who, time):
        self.User = who
        self.LoginTime = time


    def ToJson(self):
        return '{"User":"'+self.User+'", "LoginTime":"'+self.LoginTime+'"}'


    def FromJson(text):
        p = lambda:None
        p.__dict__ = json.loads(text)
        return CookieClass(p.__dict__['User'], p.__dict__['LoginTime'])

