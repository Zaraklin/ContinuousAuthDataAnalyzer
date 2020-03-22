class App(object):
    def __init__(self, data):
        self.__dict__ = data
        self.appName  = self.__dict__["appName"]

    def __str__(self):
        return str(self.appName)
