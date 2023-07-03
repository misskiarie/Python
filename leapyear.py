# create a python program to check if a given year is a leap year
# the year is divisible by 4 but not divisible by 100
# except if it is also divisible by 400

year = int(input("Enter the year"))
if year % 4 == 0 and year % 100 != 0:
    print("year is a leap year")
elif year % 400 == 0 and year % 100 == 0:
    print("year is a leap year")
else:
    print("year is not a leap year")

#if year & 4 == 0 and (year % 100 != 0 or year % 400 == 0)