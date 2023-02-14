'''
To determine the current date and time, Python provides us with various methods via the datetime module.

With the now() method we get a datetime object with current date and time. With the today() method we get a date object with the current date. The strftime() method formats a datetime object with a specified formatting
'''
import datetime

current_datetime = datetime.datetime.now()
current_date = datetime.date.today()
current_time = current_datetime.strftime("%H:%M:%S")

print(current_datetime)
print(current_date)
print(current_time)