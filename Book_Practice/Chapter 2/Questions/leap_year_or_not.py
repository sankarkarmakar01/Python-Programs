#  Determine whether the year is a leap year or not.

year = int(input("Enter the year: "))

if year%4 == 0 and year%100 != 0:
    print(f"{year} is leap year")
elif year%400 == 0:
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")