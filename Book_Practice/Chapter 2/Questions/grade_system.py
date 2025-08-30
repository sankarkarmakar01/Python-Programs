#  Question: Take input percentage of a student and print the Grade according to marks:
# 1) 81-100 Very Good 
# 2) 61-80 Good 
# 3) 41-60 Average 
# 4) <=40 Fail

percentage = float(input("Enter the percentage: "))

if percentage > 80 and percentage <= 100:
    print("Very Good")
elif percentage > 60 and percentage <= 80:
    print("Good")
if percentage > 40 and percentage <= 60:
    print("Average")
if percentage <= 40:
    print("Fail")
    