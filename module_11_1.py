import pandas as pd

# Пример чтения данных из CSV
data = pd.read_csv("https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv")

# Вывод первых строк
print("Первые строки таблицы:")
print(data.head())

# Подсчет статистики по данным
print("\nСтатистика по данным:")
print(data.describe())

# Выбор определенных строк и колонок
print("\nДанные за июль (3-я колонка):")
print(data["JUL"])

import requests

# Пример работы с библиотекой requests
url = "https://jsonplaceholder.typicode.com/posts"  # API с тестовыми данными
response = requests.get(url)

# Проверка успешного ответа
if response.status_code == 200:
    data = response.json()
    print("Получено данных:", len(data))
    # Вывод первых трех записей
    for i in range(3):
        print(f"Пост {i + 1}: {data[i]['title']}")
else:
    print(f"Ошибка запроса: {response.status_code}")


import matplotlib.pyplot as plt

# Данные для графика (на основе данных из pandas)
months = data["Month"]
july_data = data["JUL"]

# Построение графика
plt.figure(figsize=(10, 5))
plt.plot(months, july_data, marker='o', label='Данные за июль')
plt.title("Пассажиропоток в июле")
plt.xlabel("Месяц")
plt.ylabel("Количество пассажиров")
plt.legend()
plt.grid(True)
plt.show()

