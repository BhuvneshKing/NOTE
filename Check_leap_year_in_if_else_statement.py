'''
A normal year has 365 days. Every four years, however, there is a leap year with 366 days. This is because the earth does not need exactly 365 days to travel once around the sun, but about a quarter day more. So a year has one day more every 4 years.

So that the calculation is correct, there is no leap year every 100 years. Nevertheless, every four hundred years a leap year takes place. This concerns the years 2000, 2400 etc.
'''
def isLeapYear(year):
    if (year % 4 != 0):
        return False
    elif (year % 400 == 0):
        return True
    elif (year % 100 == 0):
        return False
    else:
        return True


year = int(input("Enter the Year:-\n"))

if(isLeapYear(year)):
    print(str(year) + " is a leap year")
else:
    print(str(year) + " is not a leap year")