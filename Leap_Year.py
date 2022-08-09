year = int(input("Enter a year:"))

def leap(year):
    if (year%400==0) or (year%4==0 and year%100!=0):
        return True
    else:
        return False

if leap(year):
    print('It is leap year')
else:
    print('It is not a leap year')
