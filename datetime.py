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

# to demonstrate attributes of now()

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

# to find yesterday, today and tomorrow
# Import datetime and timedelta
# class from datetime module
from datetime import datetime, timedelta


# Get today's date
presentday = datetime.now() # or presentday = datetime.today()

# Get Yesterday
yesterday = presentday - timedelta(1)

# Get Tomorrow
tomorrow = presentday + timedelta(1)


# strftime() is to format date according to
# the need by converting them to string
print("Yesterday = ", yesterday.strftime('%d-%m-%Y'))
print("Today = ", presentday.strftime('%d-%m-%Y'))
print("Tomorrow = ", tomorrow.strftime('%d-%m-%Y'))

#17

import calendar
from datetime import date, timedelta

today = date.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday = ", calendar.day_name[yesterday.weekday()], yesterday.strftime('%d-%m-%Y'))
print("Today = ", calendar.day_name[today.weekday()], today.strftime('%d-%m-%Y'))
print("Tomorrow = ", calendar.day_name[tomorrow.weekday()], tomorrow.strftime('%d-%m-%Y'))


#18

#  to convert time from 12 hour to 24 hour format 

# Function to convert the date format 
def convert24(str1): 
	
	# Checking if last two elements of time 
	# is AM and first two elements are 12 
	if str1[-2:] == "AM" and str1[:2] == "12": 
		return "00" + str1[2:-2] 
		
	# remove the AM	 
	elif str1[-2:] == "AM": 
		return str1[:-2] 
	
	# Checking if last two elements of time 
	# is PM and first two elements are 12 
	elif str1[-2:] == "PM" and str1[:2] == "12": 
		return str1[:-2] 
		
	else: 
		
		# add 12 to hours and remove PM 
		return str(int(str1[:2]) + 12) + str1[2:8] 

# Driver Code		 
print(convert24("08:05:45 PM")) 


#19

from datetime import datetime

def convert24(time):
	# Parse the time string into a datetime object
	t = datetime.strptime(time, '%I:%M:%S %p')
	# Format the datetime object into a 24-hour time string
	return t.strftime('%H:%M:%S')

print(convert24('11:21:30 PM')) # Output: '23:21:30'
print(convert24('12:12:20 AM')) # Output: '00:12:20'


#20

from datetime import datetime

def convert24(time):
	# Parse the time string into a datetime object
	t = datetime.strptime(time, '%I:%M:%S %p')
	# Format the datetime object into a 24-hour time string
	return t.strftime('%H:%M:%S')

print(convert24('11:21:30 PM')) # Output: '23:21:30'
print(convert24('12:12:20 AM')) # Output: '00:12:20'


#21

import re

def convert_to_24hour(time_str):
	hour, minute, second, am_pm = re.findall('\d+|\w+', time_str)
	hour = int(hour)
	if am_pm == 'PM' and hour != 12:
		hour += 12
	elif am_pm == 'AM' and hour == 12:
		hour = 0
	return f'{hour:02d}:{minute}:{second}'
print(convert_to_24hour('11:21:30 PM')) 
print(convert_to_24hour('12:12:20 AM'))


#22

import time


# Timer starts
starttime = time.time()
lasttime = starttime
lapnum = 1

print("Press ENTER to count laps.\nPress CTRL+C to stop")

try:
	while True:

		# Input for the ENTER key press
		input()

		# The current lap-time
		laptime = round((time.time() - lasttime), 2)

		# Total time elapsed
		# since the timer started
		totaltime = round((time.time() - starttime), 2)

		# Printing the lap number,
		# lap-time and total time
		print("Lap No. "+str(lapnum))
		print("Total Time: "+str(totaltime))
		print("Lap Time: "+str(laptime))

		print("*"*20)

		# Updating the previous total time
		# and lap number
		lasttime = time.time()
		lapnum += 1

# Stopping when CTRL+C is pressed
except KeyboardInterrupt:
	print("Done")


#23

# to convert date to timestamp


import time
import datetime


string = "20/01/2020"
print(time.mktime(datetime.datetime.strptime(string, "%d/%m/%Y").timetuple()))


#24

import time
import datetime


string = "20/11/2024"

element = datetime.datetime.strptime(string,"%d/%m/%Y")

tuple = element.timetuple()
timestamp = time.mktime(tuple)

print(timestamp)


#25

import time
import datetime


string = "20/01/2020"


element = datetime.datetime.strptime(string,"%d/%m/%Y")

timestamp = datetime.datetime.timestamp(element)
print(timestamp)


#26

from datetime import datetime

timestamp_string = "2023-07-21 15:30:45"
format_string = "%Y-%m-%d %H:%M:%S"
datetime_object = datetime.strptime(timestamp_string, format_string)
print(datetime_object)


#27

from datetime import datetime


timestamp = 1545730073
dt_obj = datetime.fromtimestamp(1140825600)

print("date_time:",dt_obj)
print("type of dt:",type(dt_obj))


#28

from dateutil.parser import parse

timestamp_string = "2023-07-17 11:30:45"

datetime_object = parse(timestamp_string)
print(datetime_object)


#29

import datetime

timestamp = 1690433696

# Convert timestamp to datetime object
dt_object = datetime.datetime.fromtimestamp(timestamp)

print(dt_object) 


#30

#  Find number of times every day occurs in a Year 


import datetime 
import calendar

def day_occur_time(year):
	
	# stores days in a week 
	days = [ "Monday", "Tuesday", "Wednesday", 
		"Thursday", "Friday", "Saturday", 
		"Sunday" ]
	
	# Initialize all counts as 52
	L = [52 for i in range(7)]
	
	# Find the index of the first day
	# of the year
	pos = -1
	day = datetime.datetime(year, month = 1, day = 1).strftime("%A")
	for i in range(7):
		if day == days[i]:
			pos = i
			
	# mark the occurrence to be 53 of 1st day
	# and 2nd day if the year is leap year
	if calendar.isleap(year):
		L[pos] += 1
		L[(pos+1)%7] += 1
		
	else:
		L[pos] += 1
		
	
	# Print the days
	for i in range(7):
		print(days[i], L[i])
	

# Driver Code 
year = 2019
day_occur_time(year)

