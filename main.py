#!venv/bin/python3
# -*- coding: cp950 -*-
import datetime
import math

date_time_now = datetime.datetime.today() # get date and time for "now"

def numberToIntList(number):
    """ Converts an int into a list containing the integer digits """
    
    int_list = [int(i) for i in str(number)]
    return int_list


def IntListToStringList(int_list):
    """ Converts a list with ints into a list containing the Chinese character of the digits """

    switcher = {
        0: "�s".encode('cp950').strip(),
        1: "��".encode('cp950').strip(),
        2: "�L".encode('cp950').strip(),
        3: "?".encode('cp950').strip(),
        4: "�v".encode('cp950').strip(),
        5: "��".encode('cp950').strip(),
        6: "��".encode('cp950').strip(),
        7: "�m".encode('cp950').strip(),
        8: "��".encode('cp950').strip(),
        9: "�h".encode('cp950').strip()
    }

    char_list = [switcher.get(i).decode('cp950') for i in int_list]
    return char_list


def convertYear(int_year):
    """ Changing year from number to Chinese e.g. 2020 to �L�s�L�s """

    year_int_list = numberToIntList(int_year)
    year_str_list = IntListToStringList(year_int_list)
    year_string = ''.join(year_str_list).strip()
    return year_string
    

def convertMonDayHr(int_datetime):
    """ Changing all numbers of month/day/hour into Chinese e.g. 999 to �h�ըh�B�h"""
    
    datetime_int_list = numberToIntList(int_datetime)
    mondayhr_str_list = IntListToStringList(datetime_int_list)
    
    if int_datetime < 10:
        return mondayhr_str_list[0]
    elif int_datetime == 10:
        mondayhr_string = "�B"
        return mondayhr_string
    elif int_datetime < 20:
        mondayhr_string = "�B" + mondayhr_str_list[1]
        return mondayhr_string
    elif int_datetime < 100:
        if int_datetime % 10 != 0:
            mondayhr_string = mondayhr_str_list[0] + "�B" + mondayhr_str_list[1]
            return mondayhr_string
        else:
            mondayhr_string = mondayhr_str_list[0] + "�B"
            return mondayhr_string


def convertMinSecMicro(int_datetime):
    """ Changing all numbers of minute/second/ms into Chinese e.g. 999 to �h�ըh�B�h"""
    
    time_int_list = numberToIntList(int_datetime)
    time_str_list = IntListToStringList(time_int_list)

    if int_datetime < 10:                           # 1 digit
        time_string = "�s" + time_str_list[0]
        return time_string
    elif int_datetime < 100:                        # 2 digit
        if int_datetime == 10:                          #10
            time_string = "�B"
            return time_string
        elif int_datetime < 20:                          #11-19
            time_string = "�B" + time_str_list[1]
            return time_string
        elif int_datetime % 10 == 0:                   #ends in 0
            time_string = time_str_list[0] + "�B"
            return time_string
        else:                                              #all other
            time_string = time_str_list[0] + "�B" + time_str_list[1]
            return time_string
    elif int_datetime < 1000:                       # 3 digit
        if int_datetime % 100 == 0: #hundreds
            time_string = time_str_list[0] + "��"
            return time_string
        elif int_datetime % 100 < 10: # x0x
            time_string = time_str_list[0] + "�չs" + time_str_list[-1]
            return time_string
        elif int_datetime % 10 == 0: # xx0
            time_string = time_str_list[0] + "��" + time_str_list[1] + "�B"
            return time_string
        else:
            time_string = time_str_list[0] + "��" + time_str_list[1] + "�B" + time_str_list[2]
            return time_string


year = convertYear(date_time_now.year)
month = convertMonDayHr(date_time_now.month)
day = convertMonDayHr(date_time_now.day)
hr = convertMonDayHr(date_time_now.hour)
mins = convertMinSecMicro(date_time_now.minute)
sec = convertMinSecMicro(date_time_now.second)
ms = convertMinSecMicro(date_time_now.microsecond//1000) # this is converted from microsends to milliseconds

print(date_time_now)
print(year+"�~"+month+"��"+day+"��"+hr+"��"+mins+"��"+sec+"��"+ms+"�@��")
