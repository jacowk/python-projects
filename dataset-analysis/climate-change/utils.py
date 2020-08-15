from datetime import datetime

def scrub_decimal(value):
    if len(value) > 0:
        return float(value)
    else:
        return float(0.0)

def format_date(value):
    if len(value) > 0:
        Date = datetime.strptime(value, '%Y-%m-%d')
        Date = datetime.strftime(Date, '%Y-%m-%d')
    else:
        Date = datetime.strptime('1100-01-01', '%Y-%m-%d')
        Date = datetime.strftime(Date, '%Y-%m-%d')
    return Date

def is_month(date, month):
    if date.split("-")[1] == month:
        return True
    else:
        return False

def convert_farenheit_to_celsius(value):
    step1 = float(value) - 32
    step2 = step1 * 5
    step3 = step2 / 9
    return step3

def get_filename(filepath):
    values = filepath.split("/")
    return values[len(values) - 1]
