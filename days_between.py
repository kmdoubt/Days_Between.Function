#this function returns the number of days between two dates
def days_between(month, day, year, month2, day2, year2):
    leap_years = (year-1)//4
    y = ((year-1)*365)+leap_years
    if (month.lower() == 'february') or (month == 2):
        y = y + 31
    elif (month.lower() == 'march') or (month == 3):
        if (year%4 == 0):
            y = y + 60
        else:
            y = y + 59
    elif (month.lower() == 'april') or (month == 4):
        if (year%4 == 0):
            y = y + 91
        else:
            y = y + 90  
    elif (month.lower() == 'may') or (month == 5):
        if (year%4 == 0):
            y = y + 121
        else:
            y = y + 120
    elif (month.lower() == 'june') or (month == 6):
        if (year%4 == 0):
            y = y + 151
        else:
           y = y + 151
    elif (month.lower() == 'july') or (month == 7):
        if (year%4 == 0):
            y = y + 183
        else:
            y = y + 182
    elif (month.lower() == 'august') or (month == 8):
        if (year%4 == 0):
            y = y + 213
        else:
            y = y + 212
    elif (month.lower() == 'september') or (month == 9):
        if (year%4 == 0):
            y = y + 244
        else:
            y = y + 243
    elif (month.lower() == 'october') or (month == 10):
        if (year%4 == 0):
            y = y + 274
        else:
            y = y + 273
    elif (month.lower() == 'november') or (month == 11):
        if (year%4 == 0):
            y = y + 305
        else:
            y = y + 304
    elif (month.lower() == 'december') or (month == 12):
        if (year%4 == 0):
            y = y + 335
        else:
            y = y + 334

    y = y+day

    leap_years2 = (year2-1)//4
    z = ((year2-1)*365)+leap_years2
    if (month2.lower() == 'february') or (month2 == 2):
        z = z + 31
    elif (month2.lower() == 'march') or (month2 == 3):
        if (year2%4 == 0):
            z = z + 60
        else:
            z = z + 59
    elif (month2.lower() == 'april') or (month2 == 4):
        if (year2%4 == 0):
            z = z + 91
        else:
            z = z + 90  
    elif (month2.lower() == 'may') or (month2 == 5):
        if (year2%4 == 0):
            z = z + 121
        else:
            z = z + 120
    elif (month2.lower() == 'june') or (month2 == 6):
        if (year2%4 == 0):
            z = z + 151
        else:
           z = z + 151
    elif (month2.lower() == 'july') or (month2 == 7):
        if (year2%4 == 0):
            z = z + 183
        else:
            z = z + 182
    elif (month2.lower() == 'august') or (month2 == 8):
        if (year2%4 == 0):
            z = z + 213
        else:
            z = z + 212
    elif (month2.lower() == 'september') or (month2 == 9):
        if (year2%4 == 0):
            z = z + 244
        else:
            z = z + 243
    elif (month2.lower() == 'october') or (month2 == 10):
        if (year2%4 == 0):
            z = z + 274
        else:
            z = z + 273
    elif (month2.lower() == 'november') or (month2 == 11):
        if (year2%4 == 0):
            z = z + 305
        else:
            z = z + 304
    elif (month2.lower() == 'december') or (month2 == 12):
        if (year2%4 == 0):
            z = z + 335
        else:
            z = z + 334

    z = z+day2

    x = y-z
    return(x)