from datetime import date, timedelta
import requests

class Student:
    """A student class as a base for method testing"""

    def __init__(self,first_name,last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._start_date = date.today()
        self.end_date = date.today() + timedelta(days=366) if date.today(). year % 4 == 0 else date.today() + timedelta(days=365)
        self.naughty_list = False
        self.extension = False
    
    

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"
    
    @property
    def get_start_date(self):
        return self._start_date

    def alert_santa(self):
        self.naughty_list = True

    def apply_extension(self, extension):
        self.end_date = self.end_date + timedelta(days=15)
        self.extension = True

    def course_schedule(self):
        response = requests.get(
            f"https://company.com/course-schedule/{self._last_name}/{self._first_name}")

        if response.ok:
            return response.text
        else:
            return "Something went wrong"


    @property
    def email(self):
        return f"{self._first_name.lower()}.{self._last_name.lower()}@email.com"






