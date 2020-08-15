from datetime import datetime

def format_date(value):
    if len(value) > 0:
        Date = datetime.strptime(value, '%m/%d/%Y %H:%M:%S %p')
    else:
        Date = datetime.strptime('01/01/1970 00:00:00 AM', '%m/%d/%Y %H:%M:%S %p')
    return Date

def format_boolean(value):
    if len(value) > 0:
        if value == "Y":
            return True
    return False

def format_integer(value):
    if len(value) > 0:
        return int(value)
    return 0

def format_geo(value):
    value = value.replace("\n", "")
    value = value.replace(",", "|")
    return value

def format_race(value):
    return value.replace(",", "")

def format_single_quote(value):
    return value.replace("\'", "")