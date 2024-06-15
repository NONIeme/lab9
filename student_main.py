import re

def task1(string):
    return bool(re.match(r'^[a-zA-Z0-9]+$', string))

def task2(string):
    return bool(re.search(r'[A-Z]', string))

def task3(string):
    return bool(re.match(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', string))

def task4(string):
    return bool(re.match(r'^([01]?[0-9]|2[0-3]):([0-5]?[0-9]):([0-5]?[0-9])$', string))

def task5(string):
    return bool(re.match(r'^\d{5}(-\d{4})?$', string))

def task6(string):
    return bool(re.match(r'^[a-z0-9_-]{6,12}$', string))

def task7(string):
    return bool(re.match(r'^(4|5|6)\d{3}-?\d{4}-?\d{4}-?\d{4}$', string))

def task8(string):
    return bool(re.match(r'^\d{3}-\d{2}-\d{4}$', string))

def task9(string):
    return bool(re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%])[A-Za-z\d@#$%]{8,}$', string))

def task10(string):
    return bool(re.match(r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$', string))
