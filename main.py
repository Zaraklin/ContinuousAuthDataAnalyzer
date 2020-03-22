import json
import os
import datetime
import statistics
from anonymousUser import *
from appList import *
from callLogList import *
from gps import *
from stylometry import *
from line import *

def write_output_file(filename, lines_list):
    first = True
    f = open(filename, "w")
    for l in lines_list:
        if first == True:
            first = False
            f.write("%s\n" % (l.header_v(version, dtype_except)))
        
        line_temp = l.str_v(version, dtype_except)
        if line_temp != "":
            f.write("%s\n" % (line_temp))
    f.close()

an_users           = []
app_list_data      = []
call_log_list_data = []
gps_data           = []
stylometry_data    = []

print("current dir: " + os.getcwd())
print("*"*50)

with open('ContinuousAuthDataAnalyzer\data\continuousauthcollector-export.json', 'r') as f:
    full_data = json.load(f)

for first_level_key in full_data:
    # Load AnonymousUser list
    if first_level_key == 'anonymousUAC':        
        for second_level_key in full_data[first_level_key]:
            an_users.append(AnonymousUser(full_data[first_level_key][second_level_key]))
    else:
        print("Listing %s keys" % first_level_key)
        for second_level_key in full_data[first_level_key]:
            key_counter = 0          
            for third_level_key in full_data[first_level_key][second_level_key]:                
                key_counter +=1
                if first_level_key == 'appListData':
                    app_list_data.append(AppList(full_data[first_level_key][second_level_key][third_level_key]))
                elif first_level_key == 'callLogData':
                    call_log_list_data.append(CallLogList(full_data[first_level_key][second_level_key][third_level_key]))
                elif first_level_key == 'gpsData':
                    gps_data.append(GPS(full_data[first_level_key][second_level_key][third_level_key]))
                elif first_level_key == 'stylometryData':
                    stylometry_data.append(Stylometry(full_data[first_level_key][second_level_key][third_level_key]))
            print("Total keys: %d" % key_counter)

print("*"*50)
listQtdUserPerGeneration(an_users)

# Make User Dict
dict_an_users = {}
for an_user in an_users:
    dict_an_users[an_user.uid] = an_user

# Discover the bigger app list
bigger   = 0
aux_list = []
for app_list in app_list_data:
    aux_list.append(len(app_list.full_list))
    if len(app_list.full_list) > bigger:
        bigger = len(app_list.full_list)

print("*"*50)
print("Bigger app_list: %d" % (bigger))
print("Median app_list: %d" % (statistics.median(aux_list)))

# Discover the bigger call_log list
bigger   = 0
aux_list = []
for call_list in call_log_list_data:
    aux_list.append(len(call_list.full_list))
    if len(call_list.full_list) > bigger:
        bigger = len(call_list.full_list)

print("Bigger call_list: %d" % (bigger))
print("Median call_list: %d" % (statistics.median(aux_list)))

data = []
#data.append(an_users          )
data.append(app_list_data     )
data.append(call_log_list_data)
data.append(gps_data          )
data.append(stylometry_data   )

# Print line objects
lines = {}
for d in data:
    for d2 in d:
        value = None
        key   = str(d2.dttime_collected) + "_" + d2.uid
        if key in lines:
            value = lines[key]
        else:
            value = Line(d2.uid, d2.dttime_collected, d2.weekday)
        
        if (d2.datatype == "app"):
            value.set_app_data(d2)
        elif(d2.datatype == "call_log"):
            value.set_call_log_data(d2)        
        elif(d2.datatype == "location"):
            value.set_location_data(d2)        
        elif(d2.datatype == "stylometry"):
            value.set_stylometry_data(d2)
        
        lines[key] = value

lines_array      = []
lines_Xgen_array = []
lines_Ygen_array = []
lines_Zgen_array = []

for l in lines:
    lines_array.append(lines[l])

    age_aux = dict_an_users[lines[l].uid].age
    curr_date = datetime.datetime.now().year
    if curr_date - age_aux <= 1980:
        lines_Xgen_array.append(lines[l])
    elif curr_date - age_aux > 1980 and curr_date - age_aux <= 1995:
        lines_Ygen_array.append(lines[l])
    elif curr_date - age_aux > 1995 and curr_date - age_aux <= 2003:
        lines_Zgen_array.append(lines[l])

lines_array.sort()
lines_Xgen_array.sort()
lines_Ygen_array.sort()
lines_Zgen_array.sort()

# Params
version = 6
# datatype_except_list = ["", "location", "stylometry", "app", "call_log"]
datatype_except_list = ["", "location", "app", "call_log"]

for dtype_except in datatype_except_list:    
    arq_prefix = "ContinuousAuthDataAnalyzer\output\\v" + str(version) + "_" + dtype_except

    write_output_file(arq_prefix + "_contauth_data_second_full.csv", lines_array)
    write_output_file(arq_prefix + "_contauth_data_second_Xgen.csv", lines_Xgen_array)
    write_output_file(arq_prefix + "_contauth_data_second_Ygen.csv", lines_Ygen_array)
    write_output_file(arq_prefix + "_contauth_data_second_Zgen.csv", lines_Zgen_array)