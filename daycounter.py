from persiantools.jdatetime import JalaliDate
from datetime import datetime
y = JalaliDate.today()
if y.month == 1:
    DaysPassed = y.day
if 1 < y.month <= 6:
    DaysPassed = ((y.month-1) * 31) + y.day
elif y.month > 6:
    DaysPassed = ((6 * 31) + ((y.month - 7) * 30)) + y.day
elif y.month == 12:
    if y.year % 33 == 1 or 5 or 9 or 13 or 17 or 22 or 26 or 30:
        DaysPassed = ((6 * 31)) + ((5 * 30)) + y.day
    else:
        (6 * 31) + (5 * 30) + y.day
        

if y.year % 33 == 1 or 5 or 9 or 13 or 17 or 22 or 26 or 30:
    totalDays = 365
else:
    totalDays = 366
    
    
Percentage = DaysPassed / totalDays * 100
print(Percentage,'%')
if DaysPassed == 1:
    print(DaysPassed,'Day ',end = '')
else:
    print(DaysPassed,'Days ',end = '')
print('Of the year is passed')


for days in range(DaysPassed):
    print('▂',end='')
for i in range((totalDays-DaysPassed)):
    print('_',end='')



from datetime import datetime
time = datetime.now()
current_time = time.strftime("%H:%M")
#print(current_time,'hours of the day is passed')
print(time.hour,':',time.minute)


from datetime import datetime
datetime_object = datetime.now()
hour = datetime_object.hour
minute = datetime_object.minute
second = datetime_object.second

totalhours = 24
print(hour / totalhours,'% of the day is passed')
for hours in range(hour):
    print('▂',end='')
for i in range((totalhours-hour)):
    print('_',end='')




total_minutes = 1440
passedminutes = (hour*60) + minute
print(passedminutes,'minutes',',',passedminutes/total_minutes,'%','of the day is passed')
for i in range(total_minutes):
    print('▃',end='')
for u in range(total_minutes-passedminutes):
    print('_',end='')


