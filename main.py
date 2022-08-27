from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime

def print_hi(name):
    print(f'Здравствуйте, {name}!')


if __name__ == '__main__':
    print_hi('Anna')
    time_now = datetime.now()
    print(f'Сейчас {time_now}')
    calculate_salary()
    get_employees()


