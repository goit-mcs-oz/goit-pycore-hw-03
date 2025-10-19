from datetime import datetime
import random
import re

# Завдання 1
def get_days_from_today(date: int) -> int:
    try:
        date_datetime = datetime.strptime(date, "%Y-%m-%d")
        today_datetime = datetime.today()
        delta = today_datetime - date_datetime
        return delta.days
    except ValueError as ex:
        print(ex)

# Завдання 2
def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    if min < 1:
        return []
    elif min >= max:
        return []
    if max <= 1 or max > 1000:
        return []
    if quantity <= 0 or quantity > max - min + 1:
        return []
    
    numbers = list(range(min, max + 1))
    numbers_random = random.sample(numbers, quantity)
    numbers_random.sort()

    return numbers_random

# Завдання 3
def normalize_phone(phone_number: str) -> str:
    normalized_phone_number = re.sub(r'\D','', phone_number)
    if normalized_phone_number.startswith('380'):
        normalized_phone_number = '+'+ normalized_phone_number
    elif normalized_phone_number.startswith('0'):
       normalized_phone_number = '+38'+ normalized_phone_number
    else:
        normalized_phone_number = '+380'+ normalized_phone_number

    return normalized_phone_number

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", *sanitized_numbers, sep = '\n')

# Завдання 4
def get_upcoming_birthdays(users: dict) -> dict:
    upcoming_birthdays = []
    for user in users:
        user['birthday'] = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
    today = datetime.today().date()
    for user in users:
        birthday = user['birthday'].replace(year = today.year)
        if birthday < today:
            birthday = birthday.replace(year = today.year + 1)
        delta = birthday - today
        if delta.days < 7:
            congratulation_date = birthday.replace()
            if birthday.weekday() == 5 or birthday.weekday() == 6:
                congratulation_date = congratulation_date.replace(day = congratulation_date.day + 7 - birthday.weekday())
            upcoming_birthdays.append({"name": user['name'], "congratulation_date": congratulation_date.strftime("%Y.%m.%d")})
    return upcoming_birthdays

users = [
    {"name": "Mike Doe", "birthday": "1987.09.20"},
    {"name": "John Doe", "birthday": "1985.10.16"},
    {"name": "Jane Smith", "birthday": "1990.10.18"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
#print("Список привітань на цьому тижні:", upcoming_birthdays)