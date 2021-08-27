"""
Created on 25 Aug, 2021

@author : Sai Vikhyath
"""

"""
Demonstrating python datetime operations
"""

# Differentiate between DateTime and Python DateTime
# pip install pytz
from datetime import datetime
import pytz

aDate = datetime.utcnow().replace(tzinfo=pytz.UTC)
bDate = str(aDate)
print("str(aDate): {}".format(str(aDate)))
print("str(bDate): {}".format(str(bDate)))
print("repr(aDate): {}".format(repr(aDate)))
print("repr(bDate): {}".format(repr(bDate)))

print('all_timezones =', pytz.all_timezones, '\n')

# getting utc timezone
utc = pytz.utc

# getting timezone by name
ist = pytz.timezone('Asia/Kolkata')

# getting datetime of specified timezone
print('UTC Time =', datetime.now(tz=utc))
print('IST Time =', datetime.now(tz=ist))

# using localise() function, on system on IST timezone
local_datetime = ist.localize(datetime.now())
print('IST Current Time =', local_datetime.strftime('%Y-%m-%d %H:%M:%S %Z%z'))
print('Wrong UTC Current Time =', utc.localize(datetime.now()).strftime('%Y-%m-%d %H:%M:%S %Z%z'))

# converting IST to UTC
utc_datetime = local_datetime.astimezone(utc)
print('IST Current Time =', local_datetime.strftime('%Y-%m-%d %H:%M:%S %Z%z'))
print('UTC Time =', utc_datetime.strftime('%Y-%m-%d %H:%M:%S %Z%z'))