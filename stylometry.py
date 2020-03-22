import statistics
from keyPressed import *
from jsonDatetimeReader import *

class Stylometry(object):
    def __init__(self, data):
        self.__dict__         = data
        self.datatype         = "stylometry"
        self.uid              = self.__dict__["uid"]
        self.weekday          = self.__dict__["weekDay"]        
        if "list" in self.__dict__:
            self.list             = self.extract_key_pressed_list(self.__dict__["list"])
            self.interval_list    = self.extract_interval_key_pressed_list(self.list)
        else:
            self.list             = []
            self.interval_list    = []
        self.dttime_collected = JsonDatetimeReader.json_datetime_reader(self.__dict__["dateTimeCollected"])
        self.mean             = 0
        if len(self.interval_list) > 0:
            self.mean = statistics.mean(self.interval_list)

    def __str__(self):
        line = "'" + str(self.uid) + "'" + "," + str(self.dttime_collected) + "," + str(self.weekday) + "," + "'" + str(self.datatype) + "'" + "," + str(self.median)
        for i in self.list:
            line += "," + str(i)
        return line
    
    def extract_key_pressed_list(self, list):
        key_pressed_list = []

        for key_pressed in list:
            key_pressed_list.append(KeyPressed(key_pressed))

        return key_pressed_list

    def extract_interval_key_pressed_list(self, list):
        interval_list = []

        for key_pressed_obj in list:
            interval_list.append(key_pressed_obj.intervalBetweenKeyPress)

        return interval_list