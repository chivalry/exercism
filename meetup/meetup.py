from datetime import date
from calendar import day_name, monthrange


weekdays = list(day_name)


class MeetupDayException(ValueError):
    pass


def meetup(year, month, week, day_of_week):
    if week == 'teenth':
        _range = range(13, 20)
    elif week == 'last':
        last = monthrange(year, month)[1]
        _range = range(last - 6, last + 1)
    else:
        ordinal = int(week[0])
        _range = range(7 * (ordinal - 1) + 1, 7 * ordinal + 1)
    weekday = weekdays.index(day_of_week)
    for day in _range:
        try:
            candidate = date(year, month, day)
        except ValueError:
            raise MeetupDayException(f'no fifth {day_of_week} in month {month}')
        if candidate.weekday() == weekday:
            return candidate
