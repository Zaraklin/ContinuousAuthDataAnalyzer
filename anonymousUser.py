import json
import datetime

class AnonymousUser(object):
    def __init__(self, data):
        self.__dict__ = data
        self.age      = self.__dict__["age"]
        self.uid      = self.__dict__["uid"]

    def __str__(self):
        return "'" + str(self.uid) + "'" + "," + str(self.age)

def listQtdUserPerGeneration(an_user_list):
    x_gen_counter = 0
    y_gen_counter = 0
    z_gen_counter = 0
    other_gen_counter = 0

    for an_user in an_user_list:
        age_aux = an_user.__dict__['age']
        curr_date = datetime.datetime.now().year
        if curr_date - age_aux <= 1980:
            x_gen_counter += 1
        elif curr_date - age_aux > 1980 and curr_date - age_aux <= 1995:
            y_gen_counter += 1
        elif curr_date - age_aux > 1995 and curr_date - age_aux <= 2003:
            z_gen_counter += 1
        else:
            other_gen_counter += 1

    print("%d participantes" % len(an_user_list))
    print("Geracao X      : %d" % (x_gen_counter))
    print("Geracao Y      : %d" % (y_gen_counter))
    print("Geracao Z      : %d" % (z_gen_counter))
    print("Outras geracoes: %d" % (other_gen_counter))