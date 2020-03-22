from jsonDatetimeReader import *

class GPS(object):
    def __init__(self, data):
        self.__dict__         = data
        self.datatype         = "location"
        self.uid              = self.__dict__["uid"]
        self.weekday          = self.__dict__["weekDay"]
        self.latitude         = self.__dict__["latitude"]
        self.longitude        = self.__dict__["longitude"]
        self.altitude         = self.__dict__["altitude"]
        self.speed            = self.__dict__["speed"]
        self.dttime_collected = JsonDatetimeReader.json_datetime_reader(self.__dict__["dateTimeCollected"])

    def __str__(self):
        return "'" + str(self.uid) + "'" + "," + str(self.dttime_collected) + "," + str(self.weekday) + "," + "'" + str(self.datatype) + "'" + "," + str(self.latitude) + "," + str(self.longitude) + "," + str(self.altitude) + "," + str(self.speed)