import datetime
import time


timestamp_local = time.time() # start point local timestamp
timestamp_utc = time.timezone + timestamp_local

time_tuple = time.localtime(timestamp_local) # from timestamp to timetuple
timestamp_x = time.mktime(time_tuple) # back to timestamp from timetuple

datetime_local = datetime.datetime.fromtimestamp(timestamp_local) # from timestamp to local datetime
datetime_utc = datetime.datetime.utcfromtimestamp(timestamp_local) # from timestamp to utc datetime
datetime_local.timestamp()
datetime_utc.timestamp()

# date and timedelta
a = datetime.date.today()
delta = datetime.timedelta(days=1)
b = a + delta

# isocalendar|isoformat|isoweekday
a.isocalendar()
a.isoformat()
a.isoweekday()

# timetuple (relationship with time module)
a.timetuple() # tm_isdst value is not correct
time.mktime(a.timetuple())

####################################################

# datetime
b = datetime.datetime.now()
b.time()
b.date()
b.utctimetuple()
b.date().timetuple()

#####################################################

# last friday's date
today = datetime.datetime.today()
day_delta = datetime.timedelta(days=today.isocalendar()[2] + 2)
last_friday = today - day_delta
