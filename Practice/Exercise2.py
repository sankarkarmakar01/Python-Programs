# https://docs.python.org/3/library/time.html#time.strftime
#Not Completed

import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)

hours = int(time.strftime('%H'))
minute = int(time.strftime('%M'))
second = int(time.strftime('%S'))
local = time.strftime('%p')

if hours >= 5 and hours <= 11:
    if minute <= 59:
        if local == "AM":
            print("Good Morning Sir")
elif hours >= 12 and hours <= 4:
    if minute <= 59:
        if local == "PM":
            print("Good Afternoon Sir")
elif hours >= 5 and hours <= 11:
    pass