import datetime
from exceptions import InvalidDate


class Utils:
    def __init__(self) -> None:
        self.date_format = '%d-%m-%Y'

    def date_validator(self, date):
        try:
            datetime.datetime.strptime(date, self.date_format)
        except ValueError:
            raise ValueError('INVALID_DATE')

    def calculate_future_date(self, date, days_ahead=0, months_ahead=0, years_ahead=0):
        if isinstance(date, str):
            date = datetime.datetime.strptime(date, self.date_format)
        month, year = date.month, date.year
        future_year = year + years_ahead
        future_year = future_year + (month + months_ahead - 1)//12
        future_month = (month + months_ahead - 1) % 12 + 1
        future_date = date + datetime.timedelta(days=days_ahead)
        future_day = future_date.day
        future = datetime.datetime(day=future_day, month=future_month, year=future_year)
        return future.strftime(self.date_format)

    def calculate_past_date(self, date, days_behind=0):
        if isinstance(date, str):
            date = datetime.datetime.strptime(date, self.date_format)
        past = date - datetime.timedelta(days=days_behind)
        return past.strftime(self.date_format)
