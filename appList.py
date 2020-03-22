from app import *
from jsonDatetimeReader import *

class AppList(object):
    def __init__(self, data):
        self.__dict__         = data
        self.max_list_len     = 13
        self.datatype         = "app"
        self.uid              = self.__dict__["uid"]
        self.weekday          = self.__dict__["weekDay"]        
        if "list" in self.__dict__:
            dict_list      = self.__dict__["list"]
            self.list      = self.extract_app_list(dict_list, self.max_list_len)
            self.full_list = self.extract_app_list(dict_list)
        else:
            self.list      = []
            self.full_list = []
        self.dttime_collected = JsonDatetimeReader.json_datetime_reader(self.__dict__["dateTimeCollected"])        

    def __str__(self):
        line = "'" + str(self.uid) + "'" + "," + str(self.dttime_collected) + "," + str(self.weekday) + "," + "'" + str(self.datatype) + "'"
        for i in self.list:
            line += "," + str(i)
        return line
    
    def extract_app_list(self, list, max_list=0):
        app_list = []
        counter  = 0

        for app in list:
            if (max_list != 0):
                if (counter < max_list):
                    counter+=1
                else:
                    break
            app_list.append(App(app))

        return app_list

    def str_app_list(self):
        str_list = ""        

        for app in self.list:            
            str_list += "," + str(app)

        if len(self.list) < self.max_list_len:
            str_list += ",?"*(self.max_list_len - len(self.list))            

        str_list = str_list.lstrip(",")

        return str_list

    def __int__(self):
        return len(self.list)

    def __lt__(self, other):
        return len(self.list) < len(other.list)

    def __le__(self, other):
        return len(self.list) <= len(other.list)

    def __gt__(self, other):
        return len(self.list) > len(other.list)

    def __ge__(self, other):
        return len(self.list) > len(other.list)

    def __eq__(self, other):
        return len(self.list) == len(other.list)

    def __ne__(self, other):
        return len(self.list) != len(other.list)