import datetime


def numberToStringList(number):
    """ Converts an int into a list containing the Chinese character of the digits """

    int_list = [int(i) for i in str(number)]

    switcher = {
        0: "零",
        1: "壹",
        2: "貳",
        3: "叁",
        4: "肆",
        5: "伍",
        6: "陸",
        7: "柒",
        8: "捌",
        9: "玖"
    }

    char_list = [switcher.get(i) for i in int_list]
    return char_list


def convertYear(int_year):
    """ Changing year from number to Chinese e.g. 2020 to 貳零貳零 """

    year_str_list = numberToStringList(int_year)
    year_string = ''.join(year_str_list).strip()
    return year_string
    

def convertMonDayHr(int_datetime):
    """ Changing all numbers of month/day/hour into Chinese e.g. 999 to 玖佰玖拾玖 """
    
    mondayhr_str_list = numberToStringList(int_datetime)
    
    if int_datetime < 10:
        return mondayhr_str_list[0]
    elif int_datetime == 10:
        mondayhr_string = "拾"
    elif int_datetime < 20:
        mondayhr_string = "拾" + mondayhr_str_list[1]
    elif int_datetime < 100:
        if int_datetime % 10 != 0:
            mondayhr_string = mondayhr_str_list[0] + "拾" + mondayhr_str_list[1]
        else:
            mondayhr_string = mondayhr_str_list[0] + "拾"
    return mondayhr_string


def convertMinSecMicro(int_datetime):
    """ Changing all numbers of minute/second/ms into Chinese e.g. 909 to 玖佰零玖 """
    
    time_str_list = numberToStringList(int_datetime)


    if int_datetime < 10:                           # 1 digit
        time_string = "零" + time_str_list[0]
    elif int_datetime < 100:                        # 2 digit
        if int_datetime == 10:                          #10
            time_string = "拾"
        elif int_datetime < 20:                          #11-19
            time_string = "拾" + time_str_list[1]
        elif int_datetime % 10 == 0:                   #ends in 0
            time_string = time_str_list[0] + "拾"
        else:                                              #all other
            time_string = time_str_list[0] + "拾" + time_str_list[1]
    elif int_datetime < 1000:                       # 3 digit
        if int_datetime % 100 == 0: #hundreds
            time_string = time_str_list[0] + "佰"
        elif int_datetime % 100 < 10: # x0x
            time_string = time_str_list[0] + "佰零" + time_str_list[-1]
        elif int_datetime % 10 == 0: # xx0
            time_string = time_str_list[0] + "佰" + time_str_list[1] + "拾"
        else:
            time_string = time_str_list[0] + "佰" + time_str_list[1] + "拾" + time_str_list[2]
    return time_string


date_time_now = datetime.datetime.today() # get date and time for "now"

year = convertYear(date_time_now.year)
month = convertMonDayHr(date_time_now.month)
day = convertMonDayHr(date_time_now.day)
hr = convertMonDayHr(date_time_now.hour)
mins = convertMinSecMicro(date_time_now.minute)
sec = convertMinSecMicro(date_time_now.second)
ms = convertMinSecMicro(date_time_now.microsecond//1000) # this is converted from microsends to milliseconds


print(date_time_now)
print(year+"年"+month+"月"+day+"日"+hr+"時"+mins+"分"+sec+"秒"+ms+"毫秒")
