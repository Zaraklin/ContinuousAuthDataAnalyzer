class Line:
    def __init__(self, uid, dttime_collected, weekday):
        self.uid              = uid
        self.dttime_collected = dttime_collected
        self.weekday          = weekday
        # app data
        self.app_list         = ""
        # call_log data
        self.call_log_list    = ""
        # location data
        self.latitude         = 0
        self.longitude        = 0
        self.altitude         = 0
        self.speed            = 0
        # stylometry data
        self.mean             = 0

    def __repr__(self):
        return str(self)

    def __str__(self):   
        str_return = self.str_v(2, "")
        return str_return

    def __int__(self):
        return self.dttime_collected

    def __lt__(self, other):
        return self.dttime_collected < other.dttime_collected

    def __le__(self, other):
        return self.dttime_collected <= other.dttime_collected

    def __gt__(self, other):
        return self.dttime_collected > other.dttime_collected

    def __ge__(self, other):
        return self.dttime_collected > other.dttime_collected

    def __eq__(self, other):
        return self.dttime_collected == other.dttime_collected

    def __ne__(self, other):
        return self.dttime_collected != other.dttime_collected

    def datatype_except(self, datatype, datatype_except, data):
        if datatype_except != datatype:
            return data
        else:
            return ""

    def header_v(self, version, datatype_except):
        if version == 1:
            return self.header_v1(datatype_except)
        elif version == 2:
            return self.header_v2(datatype_except)
        elif version == 3:
            return self.header_v3(datatype_except)
        elif version == 4:
            return self.header_v4(datatype_except)
        elif version == 5:
            return self.header_v5(datatype_except)
        elif version == 6:
            return self.header_v6(datatype_except)
        else:
            return ""

    def str_v(self, version, datatype_except):
        if version == 1:
            return self.str_v1(datatype_except)
        elif version == 2:
            return self.str_v2(datatype_except)
        elif version == 3:
            return self.str_v3(datatype_except)
        elif version == 4:
            return self.str_v4(datatype_except)
        elif version == 5:
            return self.str_v5(datatype_except)
        elif version == 6:
            return self.str_v6(datatype_except)
        else:
            return ""

    def header_v1(self, datatype_except):
        header      = "uid,dttime_collected,weekday,"
        header     += self.datatype_except("location", datatype_except, "latitude,longitude,altitude,speed,")
        header     += self.datatype_except("stylometry", datatype_except, "mean,")
        
        header_app  = ""
        header_call = ""

        for i in range(13):
            header_app  += "app_list_"+str(i+1)+","
        for i in range(20):            
            header_call += "call_log_list_"+str(i+1)+","

        header += self.datatype_except("app", datatype_except, header_app)
        header += self.datatype_except("call_log", datatype_except, header_call)
        
        return header.strip(",")

    def str_v1(self, datatype_except):
        str_return  = ""
        str_return += "'" + str(self.uid) + "'" + "," + str(self.dttime_collected) + "," + str(self.weekday) + ","
        str_aux     = ""
        
        str_return += self.datatype_except("location", datatype_except, (str(self.latitude) + "," + str(self.longitude) + "," + str(self.altitude) + "," + str(self.speed) + ","))
        str_return += self.datatype_except("stylometry", datatype_except, (str(self.mean) + ","))
                
        if self.app_list != "":
            str_aux = self.app_list + ","
        else:
            str_aux = ("?,"*13) # App        
        str_return += self.datatype_except("app", datatype_except, str_aux)
        
        if self.call_log_list != "":
            str_aux = self.call_log_list
        else:
            str_aux = ("?,"*20) # Call Log
        str_return += self.datatype_except("call_log", datatype_except, str_aux)

        str_return = str_return.strip(",")        
        return str_return

    def header_v2(self, datatype_except):        
        header      = "uid,dttime_collected,weekday,"
        header     += "data_type,"
        header     += self.datatype_except("location", datatype_except, "latitude,longitude,altitude,speed,")
        header     += self.datatype_except("stylometry", datatype_except, "mean,")
        
        header_app  = ""
        header_call = ""
        for i in range(13):
            header_app  += "app_list_"+str(i+1)+","
        for i in range(20):            
            header_call += "call_log_list_"+str(i+1)+","

        header += self.datatype_except("app", datatype_except, header_app)
        header += self.datatype_except("call_log", datatype_except, header_call)
        
        return header.strip(",")

    def str_v2(self, datatype_except):
        str_return = ""
        str_aux    = ""      
        str_prefix = "'" + str(self.uid) + "'" + "," + str(self.dttime_collected) + "," + str(self.weekday) + ","
        
        if (self.latitude != 0 or self.longitude != 0 or self.altitude != 0 or self.speed != 0) and self.datatype_except("location", datatype_except,"try") != "":
            str_aux  = ""
            str_aux += self.datatype_except("location", datatype_except, (str_prefix + "location,"))
            str_aux += self.datatype_except("location", datatype_except, (str(self.latitude) + "," + str(self.longitude) + "," + str(self.altitude) + "," + str(self.speed) + ","))
            str_aux += self.datatype_except("stylometry", datatype_except, ("?,"*1))  # Stylometry
            str_aux += self.datatype_except("app", datatype_except, ("?,"*13)) # App
            str_aux += self.datatype_except("call_log", datatype_except, ("?,"*20)) # Call Log
            str_return += str_aux.strip(",")

        if self.mean != 0 and self.datatype_except("stylometry", datatype_except,"try") != "":
            if str_return != "":
                str_return += "\n"
            
            str_aux  = ""
            str_aux += self.datatype_except("stylometry", datatype_except, (str_prefix + "stylometry,"))
            str_aux += self.datatype_except("location", datatype_except, ("?,"*4)) # Location
            str_aux += self.datatype_except("stylometry", datatype_except, (str(self.mean) + ","))
            str_aux += self.datatype_except("app", datatype_except, ("?,"*13)) # App
            str_aux += self.datatype_except("call_log", datatype_except, ("?,"*20)) # Call Log
            str_return += str_aux.strip(",")
        
        if self.app_list != "" and self.datatype_except("app", datatype_except,"try") != "":
            if str_return != "":
                str_return += "\n"
            
            str_aux  = ""
            str_aux += self.datatype_except("app", datatype_except, (str_prefix + "app,"))
            str_aux += self.datatype_except("location", datatype_except, ("?,"*4)) # Location
            str_aux += self.datatype_except("stylometry", datatype_except, ("?,"*1))  # Stylometry
            str_aux += self.datatype_except("app", datatype_except, (self.app_list + ","))
            str_aux += self.datatype_except("call_log", datatype_except, ("?,"*20)) # Call Log
            str_return += str_aux.strip(",")
        
        if self.call_log_list != "" and self.datatype_except("call_log", datatype_except,"try") != "":
            if str_return != "":
                str_return += "\n"
            
            str_aux  = ""
            str_aux += self.datatype_except("call_log", datatype_except, (str_prefix + "call_log,"))
            str_aux += self.datatype_except("location", datatype_except, ("?,"*4)) # Location
            str_aux += self.datatype_except("stylometry", datatype_except, ("?,"*1))  # Stylometry
            str_aux += self.datatype_except("app", datatype_except, ("?,"*13)) # App           
            str_aux += self.datatype_except("call_log", datatype_except, self.call_log_list)
            str_return += str_aux.strip(",")
        
        str_return = str_return.strip(",")
        return str_return

    def header_v3(self, datatype_except):
        header      = "uid,dt_collected,time_collected,weekday,"
        header     += self.datatype_except("location", datatype_except, "latitude,longitude,altitude,speed,")
        header     += self.datatype_except("stylometry", datatype_except, "mean,")
        
        header_app  = ""
        header_call = ""
        for i in range(13):
            header_app  += "app_list_"+str(i+1)+","
        for i in range(20):            
            header_call += "call_log_list_"+str(i+1)+","

        header += self.datatype_except("app", datatype_except, header_app)
        header += self.datatype_except("call_log", datatype_except, header_call)
        
        return header.strip(",")

    def str_v3(self, datatype_except):
        str_return  = ""
        str_return += "'" + str(self.uid) + "'" + "," + str(self.dttime_collected.date()) + "," + str(self.dttime_collected.time()) + "," + str(self.weekday) + ","
        str_aux     = ""
        
        str_return += self.datatype_except("location", datatype_except, (str(self.latitude) + "," + str(self.longitude) + "," + str(self.altitude) + "," + str(self.speed) + ","))
        str_return += self.datatype_except("stylometry", datatype_except, (str(self.mean) + ","))
                
        if self.app_list != "":
            str_aux = self.app_list + ","
        else:
            str_aux = ("?,"*13) # App        
        str_return += self.datatype_except("app", datatype_except, str_aux)
        
        if self.call_log_list != "":
            str_aux = self.call_log_list
        else:
            str_aux = ("?,"*20) # Call Log
        str_return += self.datatype_except("call_log", datatype_except, str_aux)

        str_return = str_return.strip(",")        
        return str_return

    def header_v4(self, datatype_except):
        header      = "uid,time_collected,weekday,"
        header     += self.datatype_except("location", datatype_except, "latitude,longitude,altitude,speed,")
        header     += self.datatype_except("stylometry", datatype_except, "mean,")
        
        header_app  = ""
        header_call = ""
        for i in range(13):
            header_app  += "app_list_"+str(i+1)+","
        for i in range(20):            
            header_call += "call_log_list_"+str(i+1)+","

        header += self.datatype_except("app", datatype_except, header_app)
        header += self.datatype_except("call_log", datatype_except, header_call)
        
        return header.strip(",")

    def str_v4(self, datatype_except):
        str_return  = ""
        str_return += "'" + str(self.uid) + "'" + "," + str(self.dttime_collected.time()) + "," + str(self.weekday) + ","
        str_aux     = ""
        
        str_return += self.datatype_except("location", datatype_except, (str(self.latitude) + "," + str(self.longitude) + "," + str(self.altitude) + "," + str(self.speed) + ","))
        str_return += self.datatype_except("stylometry", datatype_except, (str(self.mean) + ","))
                
        if self.app_list != "":
            str_aux = self.app_list + ","
        else:
            str_aux = ("?,"*13) # App        
        str_return += self.datatype_except("app", datatype_except, str_aux)
        
        if self.call_log_list != "":
            str_aux = self.call_log_list
        else:
            str_aux = ("?,"*20) # Call Log
        str_return += self.datatype_except("call_log", datatype_except, str_aux)

        str_return = str_return.strip(",")        
        return str_return

    def header_v5(self, datatype_except):        
        header      = "uid,dt_collected,time_collected,weekday,"
        header     += "data_type,"
        header     += self.datatype_except("location", datatype_except, "latitude,longitude,altitude,speed,")
        header     += self.datatype_except("stylometry", datatype_except, "mean,")
        
        header_app  = ""
        header_call = ""
        for i in range(13):
            header_app  += "app_list_"+str(i+1)+","
        for i in range(20):            
            header_call += "call_log_list_"+str(i+1)+","

        header += self.datatype_except("app", datatype_except, header_app)
        header += self.datatype_except("call_log", datatype_except, header_call)
        
        return header.strip(",")

    def str_v5(self, datatype_except):
        str_return = ""
        str_aux    = ""      
        str_prefix = "'" + str(self.uid) + "'" + "," + str(self.dttime_collected.date()) + "," + str(self.dttime_collected.time()) + "," + str(self.weekday) + ","
        
        if (self.latitude != 0 or self.longitude != 0 or self.altitude != 0 or self.speed != 0) and self.datatype_except("location", datatype_except,"try") != "":
            str_aux  = ""
            str_aux += self.datatype_except("location", datatype_except, (str_prefix + "location,"))
            str_aux += self.datatype_except("location", datatype_except, (str(self.latitude) + "," + str(self.longitude) + "," + str(self.altitude) + "," + str(self.speed) + ","))
            str_aux += self.datatype_except("stylometry", datatype_except, ("?,"*1))  # Stylometry
            str_aux += self.datatype_except("app", datatype_except, ("?,"*13)) # App
            str_aux += self.datatype_except("call_log", datatype_except, ("?,"*20)) # Call Log
            str_return += str_aux.strip(",")

        if self.mean != 0 and self.datatype_except("stylometry", datatype_except,"try") != "":
            if str_return != "":
                str_return += "\n"
            
            str_aux  = ""
            str_aux += self.datatype_except("stylometry", datatype_except, (str_prefix + "stylometry,"))
            str_aux += self.datatype_except("location", datatype_except, ("?,"*4)) # Location
            str_aux += self.datatype_except("stylometry", datatype_except, (str(self.mean) + ","))
            str_aux += self.datatype_except("app", datatype_except, ("?,"*13)) # App
            str_aux += self.datatype_except("call_log", datatype_except, ("?,"*20)) # Call Log
            str_return += str_aux.strip(",")
        
        if self.app_list != "" and self.datatype_except("app", datatype_except,"try") != "":
            if str_return != "":
                str_return += "\n"
            
            str_aux  = ""
            str_aux += self.datatype_except("app", datatype_except, (str_prefix + "app,"))
            str_aux += self.datatype_except("location", datatype_except, ("?,"*4)) # Location
            str_aux += self.datatype_except("stylometry", datatype_except, ("?,"*1))  # Stylometry
            str_aux += self.datatype_except("app", datatype_except, (self.app_list + ","))
            str_aux += self.datatype_except("call_log", datatype_except, ("?,"*20)) # Call Log
            str_return += str_aux.strip(",")
        
        if self.call_log_list != "" and self.datatype_except("call_log", datatype_except,"try") != "":
            if str_return != "":
                str_return += "\n"
            
            str_aux  = ""
            str_aux += self.datatype_except("call_log", datatype_except, (str_prefix + "call_log,"))
            str_aux += self.datatype_except("location", datatype_except, ("?,"*4)) # Location
            str_aux += self.datatype_except("stylometry", datatype_except, ("?,"*1))  # Stylometry
            str_aux += self.datatype_except("app", datatype_except, ("?,"*13)) # App           
            str_aux += self.datatype_except("call_log", datatype_except, self.call_log_list)
            str_return += str_aux.strip(",")
        
        str_return = str_return.strip(",")
        return str_return

    def header_v6(self, datatype_except):        
        header      = "uid,dt_collected,time_collected,weekday,"
        header     += "data_type,"
        header     += self.datatype_except("location", datatype_except, "latitude,longitude,altitude,speed,")
        
        header_app  = ""
        header_call = ""
        for i in range(13):
            header_app  += "app_list_"+str(i+1)+","
        for i in range(20):            
            header_call += "call_log_list_"+str(i+1)+","

        header += self.datatype_except("app", datatype_except, header_app)
        header += self.datatype_except("call_log", datatype_except, header_call)
        
        return header.strip(",")

    def str_v6(self, datatype_except):
        str_return = ""
        str_aux    = ""      
        str_prefix = "'" + str(self.uid) + "'" + "," + str(self.dttime_collected.date()) + "," + str(self.dttime_collected.time()) + "," + str(self.weekday) + ","
        
        if (self.latitude != 0 or self.longitude != 0 or self.altitude != 0 or self.speed != 0) and self.datatype_except("location", datatype_except,"try") != "":
            str_aux  = ""
            str_aux += self.datatype_except("location", datatype_except, (str_prefix + "location,"))
            str_aux += self.datatype_except("location", datatype_except, (str(self.latitude) + "," + str(self.longitude) + "," + str(self.altitude) + "," + str(self.speed) + ","))
            str_aux += self.datatype_except("app", datatype_except, ("?,"*13)) # App
            str_aux += self.datatype_except("call_log", datatype_except, ("?,"*20)) # Call Log
            str_return += str_aux.strip(",")

        if self.app_list != "" and self.datatype_except("app", datatype_except,"try") != "":
            if str_return != "":
                str_return += "\n"
            
            str_aux  = ""
            str_aux += self.datatype_except("app", datatype_except, (str_prefix + "app,"))
            str_aux += self.datatype_except("location", datatype_except, ("?,"*4)) # Location
            str_aux += self.datatype_except("app", datatype_except, (self.app_list + ","))
            str_aux += self.datatype_except("call_log", datatype_except, ("?,"*20)) # Call Log
            str_return += str_aux.strip(",")
        
        if self.call_log_list != "" and self.datatype_except("call_log", datatype_except,"try") != "":
            if str_return != "":
                str_return += "\n"
            
            str_aux  = ""
            str_aux += self.datatype_except("call_log", datatype_except, (str_prefix + "call_log,"))
            str_aux += self.datatype_except("location", datatype_except, ("?,"*4)) # Location
            str_aux += self.datatype_except("app", datatype_except, ("?,"*13)) # App           
            str_aux += self.datatype_except("call_log", datatype_except, self.call_log_list)
            str_return += str_aux.strip(",")
        
        str_return = str_return.strip(",")
        return str_return

    def set_app_data(self, data):
        self.app_list = data.str_app_list()

    def set_call_log_data(self, data):
        self.call_log_list = data.str_call_log_list()

    def set_location_data(self, data):
        self.latitude         = data.latitude 
        self.longitude        = data.longitude
        self.altitude         = data.altitude 
        self.speed            = data.speed    

    def set_stylometry_data(self, data):
        self.mean           = data.mean
