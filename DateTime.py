#DateTime Module

# learn how to work with DateTime,
# learn how to work with DateTime Objects,
# learn how to format string(that is, converting strings to DateTime Objects)

#benefits of DateTime Module?
# well, you can essentialy:
# (1). calculate the difference between today and your birthday
# (2). create an App that send emails automatically based on date
# (3). create an App also like Instagram(Clone), that can say things like "posted three days ago"


import datetime
from pytz import timezone
import pytz


today = datetime.date.today()
print(today)

birthday = datetime.date(2002, 5, 21)
print(birthday)

days_lived_since_birth = (today - birthday).days
print(days_lived_since_birth)

print(today.weekday()) #Monday = 0, #Sunday = 6
print(datetime.time(4, 37, 34, 64))
#print(datetime.date(2020, 4, 5))
# datetime.time(Hr, Min, Sec, MS's(microseconds))
# datetime.datetime(Y, M, D, Hr, Min, Sec, MS's)

# Add 10 hours to current day
hour_delta = datetime.timedelta(hours=10)
print(datetime.datetime.now() + hour_delta)


#this code won't run, untill the module 'pytz' is installed
#print(datetime.datetime.now(tz=pytz('US/Eastern')))
for tz in pytz.timezone(pytz):
    print(tz)
