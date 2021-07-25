from utilities import (space, separated, start, end, sub, new_topic)
import datetime  # Basic features

# Key
key = 'modules_datetime_basic_date'


def run():
    start('Datetime: Basic Date')
    sub('import datetime')
    new_topic('Date variable')
    d = datetime.date(2020, 6, 24)
    print(d)
    new_topic('Current local date', True)
    print(datetime.date.today())
    print(datetime.date.today().year)
    new_topic('Weekday from date', True)
    # Weekday[Monday 0 Sunday 6]
    # ISO Weekday[Monday 1 Sunday 7]
    today = datetime.date.today()
    print(f'Weekday of {today} is {today.weekday()}')
    print(f'ISO weekday of {today} is {today.isoweekday()}')
    new_topic('Time Delta (datetime interval)', True)
    tdelta = datetime.timedelta(days=7)
    print(f'Last 7 days: {today - tdelta}')
    print(f'Next 7 days: {today + tdelta}')

    new_topic('Time Delta (the different from 2 dates)', True)
    # date2 = date1 + timedelta
    # timedelta = date1 + date2
    today = datetime.date.today()
    bday = datetime.date(2020, 7, 25)
    till_bday = bday - today
    print(f'days interval is {till_bday}, {till_bday.days}')
    print(f'time interval in secound is {till_bday.total_seconds()} secs')
    end()
