import datetime

date_time_now = datetime.datetime.today() # get date and time for "now"
# 零壹貳叁肆伍陸柒捌玖 拾佰

def numberToIntList(number):
    """ Converts an int into a list containing the integer digits """
    
    int_list = [int(i) for i in str(number)]
    return int_list


def IntListToStringList(int_list):
    """ Converts a list with ints into a list containing the Chinese character of the digits """

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

    year_int_list = numberToIntList(int_year)
    year_str_list = IntListToStringList(year_int_list)
    year_string = ''.join(year_str_list).strip()
    return year_string
    

def convertMonDayHr(int_datetime):
    """ Changing all numbers of month/day/hour into Chinese e.g. 999 to 玖佰玖拾玖 """
    
    datetime_int_list = numberToIntList(int_datetime)
    mondayhr_str_list = IntListToStringList(datetime_int_list)
    
    # 0-9, 10, 11-19, 20-99
    if int_datetime < 10:
        return mondayhr_str_list[0]
    elif int_datetime == 10:
        mondayhr_string = "拾"
        return mondayhr_string
    elif int_datetime < 20:
        mondayhr_string = "拾" + mondayhr_str_list[1]
        return mondayhr_string
    elif int_datetime < 100:
        if int_datetime % 10 != 0:
            mondayhr_string = mondayhr_str_list[0] + "拾" + mondayhr_str_list[1]
            return mondayhr_string
        else:
            mondayhr_string = mondayhr_str_list[0] + "拾"
            return mondayhr_string


def convertMinSecMicro(int_datetime):
    """ Changing all numbers of minute/second/ms into Chinese e.g. 999 to 玖佰玖拾玖 """
    
    time_int_list = numberToIntList(int_datetime)
    time_str_list = IntListToStringList(time_int_list)

    # 1 digit: 0-9
    # 2 digit: 10, 11-19, 20-99, %10 = 0
    # 3 digit: %100 = 0, %10 = 0 and %1 != 0, %10 = 0, rest
    if int_datetime < 10:                           # 1 digit
        time_string = "零" + time_str_list[0]
        return time_string
    elif int_datetime < 100:                        # 2 digit
        if int_datetime == 10:                          #10
            time_string = "拾"
            return time_string
        elif int_datetime < 20:                          #11-19
            time_string = "拾" + time_str_list[1]
            return time_string
        elif int_datetime % 10 == 0:                   #ends in 0
            time_string = time_str_list[0] + "拾"
            return time_string
        else:                                              #all other
            time_string = time_str_list[0] + "拾" + time_str_list[1]
            return time_string
    elif int_datetime < 1000:                       # 3 digit
        if int_datetime % 100 == 0: #hundreds
            time_string = time_str_list[0] + "佰"
            return time_string
        elif int_datetime % 100 < 10: # x0x
            time_string = time_str_list[0] + "佰零" + time_str_list[-1]
            return time_string
        elif int_datetime % 10 == 0: # xx0
            time_string = time_str_list[0] + "佰" + time_str_list[1] + "拾"
            return time_string
        else:
            time_string = time_str_list[0] + "佰" + time_str_list[1] + "拾" + time_str_list[2]
            return time_string
    

# year = convertYear(4504)
# month = convertMonDayHr(50)
ms = convertMinSecMicro(104)

# year = convertYear(date_time_now.year)
# month = convertMonDayHr(date_time_now.month)
# day = convertMonDayHr(date_time_now.day)
# hr = convertMonDayHr(date_time_now.hour)
# mins = convertMinSecMicro(date_time_now.minute)
# sec = convertMinSecMicro(date_time_now.second)
# ms = convertMinSecMicro(date_time_now.microsecond//1000) # this is converted from microsends to milliseconds


print(date_time_now)
# print(year+"年"+month+"月"+day+"日"+hr+"時"+mins+"分"+sec+"秒"+ms+"毫秒")

print(ms)


# edge case testing: 0, 1, 10, 14, 100, 101, 110, 