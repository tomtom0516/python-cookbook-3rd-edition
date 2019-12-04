from datetime import datetime, date, timedelta
import calendar

month = datetime.today().month
year = datetime.today().year

_, days_in_month = calendar.monthrange(year, month)