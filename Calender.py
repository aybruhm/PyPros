import calendar
import datetime
import time

# prints the week head
print(calendar.weekheader(3))
print()

print(calendar.firstweekday())
print()

print(calendar.month(2020, 3, w=3, l=1))
print()

#this prints out the data of a month in an array/list format
print(calendar.monthcalendar(2020, 3))
print()

days_of_the_week = calendar.weekday(2020, 4, 6)
print(days_of_the_week)

print(calendar.calendar(2020))
print()

#checks if the year is a leap year
is_leap = calendar.isleap(2020)
print(is_leap)

# checks how many leap years in the range of 2020 - 2025
how_many_leap_days = calendar.leapdays(2020, 2025)
print(how_many_leap_days) 

