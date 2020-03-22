import datetime

class JsonDatetimeReader:
    @staticmethod
    def json_datetime_reader(datetime_collected):
        dttime = None
        # dttime = datetime.datetime(datetime_collected["year"], datetime_collected["monthOfYear"], datetime_collected["dayOfMonth"], datetime_collected["hourOfDay"], datetime_collected["minuteOfHour"], datetime_collected["secondOfMinute"], datetime_collected["millisOfSecond"])
        dttime = datetime.datetime(datetime_collected["year"], datetime_collected["monthOfYear"], datetime_collected["dayOfMonth"], datetime_collected["hourOfDay"], datetime_collected["minuteOfHour"], datetime_collected["secondOfMinute"])
        # dttime = datetime.datetime(datetime_collected["year"], datetime_collected["monthOfYear"], datetime_collected["dayOfMonth"], datetime_collected["hourOfDay"], datetime_collected["minuteOfHour"])
        return dttime
