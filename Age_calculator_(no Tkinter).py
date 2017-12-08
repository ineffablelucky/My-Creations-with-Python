import datetime
from dateutil import relativedelta

class Person:
    def __init__(self, name, DOB):
        self.name = name
        self.DOB = DOB

    def age(self):
        self.todays_date = datetime.date.today()
        self.difference = relativedelta.relativedelta(self.todays_date, self.DOB)  # to calculate the difference in years, month and days
        return self.difference.years # returns only years
        # months=difference.years*12 + difference.months
        # print(months)
        # ageindays = todays_date-birthdate
        # print(ageindays.days)

name_of_person = input("Enter your full name: ")  # added name just for fun
year = int(input("enter your year of birth: "))
month = int(input("enter your month of birth: "))
day = int(input("enter your day of birth: "))
dob = datetime.date(year, month, day)  # this is our date of birth

lucky = Person(name_of_person, dob)
print(lucky.age())
print(lucky.difference)