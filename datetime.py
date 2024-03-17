#1
from datetime import *
import pytz


tz_INDIA = pytz.timezone('Asia/Kolkata')
datetime_INDIA = datetime.now(tz_INDIA)
print("INDIA time:", datetime_INDIA.strftime("%H:%M:%S"))

#2
from datetime import datetime

# now() method is used to
# get object containing
# current date & time.
now_method = datetime.now()

# strftime() method used to
# create a string representing
# the current time.
currentTime = now_method.strftime("%H:%M:%S")
print("Current Time =", currentTime)

#3
from datetime import datetime

# Time object containing
# the current time.
time = datetime.now().time()

print("Current Time =", time)

#4
import time


# localtime() method used to
# get the object containing
# the local time.
Time = time.localtime()

# strftime() method used to
# create a string representing
# the current time.
currentTime = time.strftime("%H:%M:%S", Time)
print(currentTime)

#5
# Getting current date and time using now().

# importing datetime module for now()
import datetime

# using now() to get current time
current_time = datetime.datetime.now()

# Printing value of now.
print("Time now at greenwich meridian is:", current_time)

#6
# Python3 code to demonstrate
# attributes of now()

# importing datetime module for now()
import datetime

# using now() to get current time
current_time = datetime.datetime.now()

# Printing attributes of now().
print("The attributes of now() are :")

print("Year :", current_time.year)

print("Month : ", current_time.month)

print("Day : ", current_time.day)

print("Hour : ", current_time.hour)

print("Minute : ", current_time.minute)

print("Second :", current_time.second)

print("Microsecond :", current_time.microsecond)

#8
# for now()
import datetime

# for timezone()
import pytz

# using now() to get current time
current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))

# printing current time in india
print("The current time in india is :", current_time)

#9
from datetime import datetime

print("UTC Time: ", datetime.utcnow())

#10
from datetime import datetime as dt

x = dt.now().isoformat()
print('Current ISO:', x)

#11
import time

curr_time = time.strftime("%H:%M:%S", time.localtime())

print("Current Time is :", curr_time)

#12
import time

millisec = int(round(time.time() * 1000))

print("Time in Milli seconds: ", millisec)

#13
import time

curr_time = time.strftime("%H:%M:%S", time.localtime())

print("Current Time is :", curr_time)

nano_seconds = time.time_ns()

print("Current time in Nano seconds is : ", nano_seconds)

#14
import time

# current GMT Time
gmt_time = time.gmtime(time.time())

print('Current GMT Time:\n', gmt_time)

#15
import time

print("Epoch Time is : ", int(time.time()))

#16
