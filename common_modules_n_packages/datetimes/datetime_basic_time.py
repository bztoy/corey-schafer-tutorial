from utilities import (space, separated, start, end, sub, new_topic)
import datetime  # Basic features
import pytz

# Key
key = 'modules_datetime_basic_time'

# Working with hours, minutes, secound, milliseconds


def run():
    start('Datetime: Basic Time')
    sub('import datetime')
    new_topic('Time variable')
    t = datetime.time(11, 30, 24, 100000)
    print(t)
    print(f'only hour: {t.hour}')
    new_topic('Whole date/time', True)
    dt = datetime.datetime(2020, 6, 25, 9, 19, 29, 100000)
    print(f'Full date/time : {dt}')
    print(f'Only date : {dt.date()}')
    print(f'Only time : {dt.time()}')
    print(
        f'Other attrs, Year: {dt.year}, Hour: {dt.hour}, Secounds: {dt.second}')
    new_topic('Time Delta (time interval)', True)
    print(f'current date/time is {dt}')
    tdelta = datetime.timedelta(hours=12)
    print(f'Last 12 hours: {dt - tdelta}')
    tdelta = datetime.timedelta(hours=5)
    print(f'Next 5 hours: {dt + tdelta}')

    new_topic('today, now, utcnow', True)
    dt_today = datetime.datetime.today()  # local time
    dt_now = datetime.datetime.now()
    dt_utcnow = datetime.datetime.utcnow()
    print(f'today() : {dt_today}')
    print(f'now()   : {dt_now}')
    print(f'utcnow(): {dt_utcnow}')

    new_topic('Working with timezone (pytz) and today, now, utcnow', True)
    dt = datetime.datetime(2020, 7, 1, 14, 30, 30, tzinfo=pytz.UTC)
    dt_now = datetime.datetime.now(tz=pytz.UTC)
    print(f'DateTime with UTC: {dt}')
    print(f'Current DateTime with UTC: {dt_now}')

    new_topic('Timezone converting', True)
    dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
    dt_bkktc = dt_utcnow.astimezone(pytz.timezone('Asia/Bangkok'))
    print(f'UTC Time: {dt_utcnow}')
    print(f'Bangkok Time: {dt_bkktc}')

    new_topic('Get all timezone', True)
    for tz in pytz.all_timezones:
        if tz.find('Asia/Bangkok') != -1:
            print(tz)

    new_topic('Timezone localization', True)
    my_tz = pytz.timezone('Asia/Bangkok')
    my_dtnow = my_tz.localize(datetime.datetime.now())
    print(f'Current date/time in my timezone is: {my_dtnow}')
    tokyo_dt = my_dtnow.astimezone(pytz.timezone('Asia/Tokyo'))
    print(f'Current date/time in Japan/Tokyo is: {tokyo_dt}')

    # new_topic('Current local date', True)
    # print(datetime.date.today())
    # print(datetime.date.today().year)
    # new_topic('Weekday from date', True)
    # # Weekday[Monday 0 Sunday 6]
    # # ISO Weekday[Monday 1 Sunday 7]
    # today = datetime.date.today()
    # print(f'Weekday of {today} is {today.weekday()}')
    # print(f'ISO weekday of {today} is {today.isoweekday()}')
    # new_topic('Time Delta (datetime interval)', True)
    # tdelta = datetime.timedelta(days=7)
    # print(f'Last 7 days: {today - tdelta}')
    # print(f'Next 7 days: {today + tdelta}')

    # new_topic('Time Delta (the different from 2 dates)', True)
    # # date2 = date1 + timedelta
    # # timedelta = date1 + date2
    # today = datetime.date.today()
    # bday = datetime.date(2020, 7, 25)
    # till_bday = bday - today
    # print(f'days interval is {till_bday}, {till_bday.days}')
    # print(f'time interval in secound is {till_bday.total_seconds()} secs')
    end()
