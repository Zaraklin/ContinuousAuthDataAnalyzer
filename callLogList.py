from callLog import *
from jsonDatetimeReader import *

class CallLogList(object):
    def __init__(self, data):
        self.__dict__         = data
        self.max_list_len     = 20
        self.datatype         = "call_log"
        self.uid              = self.__dict__["uid"]
        self.weekday          = self.__dict__["weekDay"]        
        if "list" in self.__dict__:
            dict_list      = self.__dict__["list"]
            self.list      = self.extract_call_log_list(dict_list, self.max_list_len)
            self.full_list = self.extract_call_log_list(dict_list)
        else:
            self.list      = []
            self.full_list = []
        self.dttime_collected = JsonDatetimeReader.json_datetime_reader(self.__dict__["dateTimeCollected"])

    def __str__(self):
        line = "'" + str(self.uid) + "'" +  "," + str(self.dttime_collected) + "," + str(self.weekday) + "," + "'" + str(self.datatype) + "'"
        for i in self.list:
            line += "," + str(i)
        return line

    def extract_call_log_list(self, list, max_list=0):
        call_log_list = []
        call_list     = []
        counter       = 0       

        for call_log in list:            
            call_list.append(CallLog(call_log))

        call_list.sort(reverse=True)
        for call_log in call_list:
            if (max_list != 0):
                if (counter < max_list):
                    counter+=1
                else:
                    break
            call_log_list.append(call_log)

        return call_log_list

    def str_call_log_list(self):
        str_list = ""
        
        for call_log in self.list:
            str_list += "," + str(call_log.number) + "#" + str(call_log.direction) + "#" + str(call_log.duration) + "#" + str(call_log.datetime_call)
        
        if len(self.list) < 20:
            str_list += ",?"*(20 - len(self.list))  

        str_list = str_list.lstrip(",")
        
        return str_list