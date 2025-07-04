import datetime

gvr = datetime.date(1956, 1, 31)
print(gvr.year, gvr.month, gvr.day)

today = datetime.date(2025,1,3)
extra = datetime.timedelta(7)
print(today + extra)  
print (today - gvr, gvr - today)

message = "GVR was born on {:%A , %B %d, %y}."
print(message.format(gvr))

now = datetime.datetime.now()
print(now)
print(now.microsecond)