import datetime

class CallLog(object):
    def __init__(self, data):
        self.__dict__        = data
        self.datetime_millis = self.__dict__["datetime"]
        self.datetime_call   = datetime.datetime.fromtimestamp(int(self.datetime_millis) / 1000)
        self.direction       = self.__dict__["direction"]
        self.duration        = self.__dict__["duration"]
        self.number          = self.__dict__["number"]

    def __str__(self):
        return str(self.number) + "," + str(self.direction) + "," + str(self.duration) + "," + str(self.datetime_call)

    def __int__(self):
        return int(self.datetime_call)

    def __lt__(self, other):
        return self.datetime_call < other.datetime_call

    def __le__(self, other):
        return self.datetime_call <= other.datetime_call

    def __gt__(self, other):
        return self.datetime_call > other.datetime_call

    def __ge__(self, other):
        return self.datetime_call > other.datetime_call

    def __eq__(self, other):
        return self.datetime_call == other.datetime_call

    def __ne__(self, other):
        return self.datetime_call != other.datetime_call