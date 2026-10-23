"""Проект FitLife - MVP версия 1.0"""

import datetime

WATER_PER_KG = 30
ML_TO_LITRES = 1000

# 1. Знакомство
print("Приветствую пользователь! Эта программа следит за вашим здоровьем!")
print("Она поможет рассчитать ваш ИМТ и сколько воды стоит пить каждый день")
print("Давайте знакомиться!")
print()
# Спрашиваем у пользователя имя и сохраняем в переменную user_name
user_name = input("Как ваше имя? - ")
while True:
    try:
        # Спрашиваем возраст и сохраняем в переменную user_age
        user_age = int(input("Сколько вам полных лет? - "))
        break
    except ValueError:
        print("Пожалуйста, введите число!")

# 2. Сбор данных
while True:
    try:
        # Запрашиваем вес (в кг) и сохраняем в user_weight (тип float)
        user_weight = float(input("Укажите ваш вес (в килограммах) - "))
        break
    except ValueError:
        print("Пожалуйста, введите число!")
while True:
    try:
        # Запрашиваем рост и сохраняем в user_height (тип float)
        user_height = float(input("Укажите ваш рост в м. (например 1.75) - "))
        break
    except ValueError:
        print("Пожалуйста, введите число!")

# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
bmi = user_weight / (user_height ** 2)  # Рассчитываем bmi (Индекс массы тела)
# Подсчет нормы воды: (вес * 30 мл) и делим для перевода в литры
water_needed = (user_weight * WATER_PER_KG) / ML_TO_LITRES

# 4. Вывод красивого результата
# Логика склонения возраста
if user_age % 10 == 1 and user_age % 100 != 11:
    age_word = "год"
elif 2 <= user_age % 10 <= 4 and not (12 <= user_age % 100 <= 14):
    age_word = "года"
else:
    age_word = "лет"
today = datetime.datetime.today()  # Выводим сегодняшнуюю дату
print()
print(f"Отчёт для пользователя на {today:%d-%m-%Y}")
print(f"{user_name} - {user_age} {age_word}.")
print(f"Ваш индекс массы тела: {bmi:.1f}")
print(f"Ваша рекомендуемая норма воды: {round(water_needed, 1)} л. в день")
print()
print("Расчет окончен. Будьте здоровы!")
