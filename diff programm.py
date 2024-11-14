#1

def check_year(year):
    # Leap year condition: 
    # 1. If the year is divisible by 4 and not divisible by 100, or
    # 2. If the year is divisible by 400.
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True  # It's a leap year
    else:
        return False  # It's not a leap year
 
year = 2003  # Sample input to test
 
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
year = 2024
if (checkYear(year)): 
	print("Leap Year") 
else: 
	print("Not a Leap Year") 

#3

def ISLP(y):
    if (y % 400 == 0) or (y % 100 != 0 and y % 4 == 0):
        print("its a leap year")
    else:
        print("its not a leap year")

# Driver code
if __name__ == '__main__':
    year = 2020
    print(ISLP(year))


#4

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Input from the user
year_input = input("Enter a year: ")

# Check if the input is a valid integer
try:
    year = int(year_input)
    if year > 0:
        if is_leap_year(year):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print("Please enter a valid positive year.")
except ValueError:
    print("Invalid input. Please enter a valid year.")
