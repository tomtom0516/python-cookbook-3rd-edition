import datetime
import time

timestamp = time.time()
local_tm = datetime.datetime.fromtimestamp(timestamp)
utc_tm = datetime.datetime.utcfromtimestamp(timestamp)

delta = local_tm - utc_tm
delta.seconds/3600
