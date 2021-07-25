from utilities import (space, separated, start, end, sub, new_topic)
import datetime  # Basic features
import pytz

# Key
key = 'modules_datetime_basic_format'


def run():
    start('Datetime: Formatting')
    sub('import datetime')
    new_topic('ISO format')
    dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
    print(dt_utcnow.isoformat())
    new_topic('Show date/time in string format with method strftime()', True)
    # documentation -> https://docs.python.org/2/library/datetime.html
    print(dt_utcnow.strftime('%B %m, %Y'))
    print(dt_utcnow.strftime('%A %w'))

    new_topic(
        'Convert string datetime to datetime with datetime.datetime.strptime()', True)
    str_datetime = 'June 06, 2020'
    dt = datetime.datetime.strptime(str_datetime, '%B %m, %Y')
    print(f'from string {str_datetime} can be converted into datetime as {dt}')

    end()
