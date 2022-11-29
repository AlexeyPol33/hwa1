import application.salary as salary
from application.db import people
from datetime import datetime

if __name__ == '__main__':
    date = datetime.today()
    print(date)
    people.get_employees()
    salary.calculate_salary()