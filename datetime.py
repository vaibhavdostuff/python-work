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
