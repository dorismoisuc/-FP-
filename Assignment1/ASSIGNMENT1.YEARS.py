from datetime import date
today = date.today()
current_year = today.year
yearb = int(input("The year you were born is:"))
monthb = int(input("The month you were born is:"))
dayb = int(input("The day you were born is:"))
monthdays = [31,28,31,30,31,30,31,31,30,31,30,31]
thedays = 0

#verifies if a year is a leapyear

def LeapYear (BirthYear):
        if (((BirthYear%4) == 0 and (BirthYear % 100) != 0) or (BirthYear % 400) == 0):
            return True
        else:
            return False
    
#verifies how many years since birth were leap years

def check_leap (month,year,thedays):
    from datetime import date
    today = date.today()
    current_year = today.year
    while ( year <= current_year ):
        if (LeapYear(year)==False):
            thedays += 0
        else:
            thedays += 1
        year = year + 1
    return thedays

#if a person is born in a leap year and
#their birth month > 2
#it means that they haven't lived that +1 day
#so it has to be subtracted

def minusOne (month,year,thedays):
    if (LeapYear(year)==True):
        if (month > 2 ):
            thedays -= 1
    return thedays

#calculating the number of days that have passed
#until the end of the month

def birthdayMonthPassed (day,month,year,thedays):
    from datetime import date
    today = date.today()
    currentmonth = today.month
    currentyear = today.year
    currentday = today.day
    if (currentyear == year and currentmonth == month ):
        thedays += 0
    else: 
        thedays = monthdays[month-1] - day
    return thedays

#calculating days that have passed since the birthdaymonth+1 until the current
#date if the number of the monthb < currentmonth

def until_currentDate (month,thedays):
    month = month + 1
    from datetime import date
    today = date.today()
    currentmonth = today.month
    while (month < currentmonth):
        thedays += monthdays[month-1]
        month = month + 1
    return thedays

#calculating the total number of years the person has lived
#then transforming it in days

def allYearsLived (month,year,thedays):
    from datetime import date
    today = date.today()
    currentyear = today.year
    currentmonth = today.month
    thedays = (currentyear-year)*365
    if (currentyear != year):
        while ( month >= currentmonth ):
            thedays -= monthdays[month-1]
            month = month - 1
    return thedays

#calculating the days that have passed in this month

def passedThis_month (month,year,day,thedays):
    from datetime import date
    today = date.today()
    currentmonth = today.month
    currentyear = today.year
    currentday = today.day
    if (currentyear == year and currentmonth == month ):
        thedays = currentday - day + 1
    else:
        thedays += currentday
    return thedays

x = birthdayMonthPassed (dayb,monthb,yearb,thedays)
x += passedThis_month (monthb,yearb,dayb,thedays)
x += check_leap (monthb,yearb,thedays)
x += until_currentDate(monthb,thedays)
x += allYearsLived (monthb,yearb,thedays)
x += minusOne(monthb,yearb,thedays)
from datetime import datetime
print ("The number of days are:",x)
print ((datetime.today()-datetime(yearb,monthb,dayb)).days)
