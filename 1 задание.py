import requests # делаем запрос на чтение страницы https://urban-university.ru/
import pandas as pd
import numpy as np


#response = requests.get('https://urban-university.ru/')
#print(response.ok)  # проверяем успешен ли запрос?
#print(response.text)  # выводим полученный ответ на экран

##########################################################

# Создаем тестовый CSV-файл
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [25, 30, 35, 40, 22],
    "Salary": [50000, 60000, 70000, 80000, 55000]
}
df = pd.DataFrame(data)
df.to_csv("data.csv", index=False)

# Читаем CSV-файл
df = pd.read_csv("data.csv")

# Вывод первых строк данных
print("Первый взгляд на данные:")
print(df.head())

# Анализ данных: средний возраст и зарплата
average_age = df["Age"].mean()
average_salary = df["Salary"].mean()

print("\nПростой анализ данных:")
print(f"Средний возраст: {average_age:.2f}")
print(f"Средняя зарплата: {average_salary:.2f}")

# Фильтрация: сотрудники с зарплатой больше 60000
high_salary = df[df["Salary"] > 60000]
print("\nСотрудники с зарплатой больше 60000:")
print(high_salary)


##################################################



# Создаем массив чисел от 1 до 10
array = np.arange(1, 11)

# Выполняем математические операции
squared = array ** 2  # Возведение в квадрат
summation = np.sum(array)  # Сумма всех элементов
mean_value = np.mean(array)  # Среднее значение
std_deviation = np.std(array)  # Стандартное отклонение

# Вывод результатов
print("Оригинальный массив:")
print(array)

print("\nРезультаты математических операций:")
print(f"Квадраты элементов: {squared}")
print(f"Сумма элементов: {summation}")
print(f"Среднее значение: {mean_value:.2f}")
print(f"Стандартное отклонение: {std_deviation:.2f}")