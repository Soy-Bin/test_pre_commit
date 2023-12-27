import datetime


class Day():
    """Invert date and time.

    Parameters
    ----------
    now : str
        date and time like "2222-02-20 22:22"

    Attributes
    ----------
    date_time : datetime
        where store date and time
    holidays : list
        where store public holidays
    """

    def __init__(
        self,
        now: str,
    ) -> str:
        try:
            now = datetime.datetime.strptime(now, '%Y-%m-%d %H:%M')
        except ValueError:
            print('Please input date and time like "2222-02-20 22:22"')

        self.date_time = now
        self.holidays = [
            '01-01', '03-01', '05-05', '06-06',
            '08-15', '10-03', '10-09', '12-25',
        ]

    def is_holiday(
        self,
    ) -> str:
        """Returns whether the date is a public holiday or not.

        Parameters
        ----------
        None

        Returns
        -------
        holiday_or_not :str

        Examples
        --------
        day_time = Day('2023-12-25 14:00')
        day_time.is_holiday() -> 'a public holiday'
        """
        if self.date_time.date().strftime("%m-%d") in self.holidays:
            holiday_or_not = 'a public holiday'
            return holiday_or_not
        else:
            holiday_or_not = 'not a public holiday'
            return holiday_or_not

    def invert_time(
        self,
    ) -> str:
        """Returns time as the form of pm/am.

        Parameters
        ----------
        None

        Returns
        -------
        time_12 : str

        Examples
        --------
        day_time.invert_time() -> '02:00 pm'
        """
        time_12 = self.date_time.time().strftime('%I:%M %p')
        return time_12
