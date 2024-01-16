#1
def check_year(year):
    # Leap year condition: 
    # 1. If the year is divisible by 4 and not divisible by 100, or
    # 2. If the year is divisible by 400.
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True  # It's a leap year
    else:
        return False  # It's not a leap year
 
year = 2000  # Sample input to test
 
if check_year(year):
    print("Leap Year")
else:
    print("Not a Leap Year")

#2
def checkYear(year): 
	
	# Return true if year is a multiple 
	# of 4 and not multiple of 100. 
	# OR year is multiple of 400. 
	import calendar
	return(calendar.isleap(year)) 
	
# Driver Code 
year = 2000
if (checkYear(year)): 
	print("Leap Year") 
else: 
	print("Not a Leap Year") 

