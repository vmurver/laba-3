# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

# Указание пути к файлу
file_path = r'C:\Valuta.txt'

# Чтение данных из файла
try:
    data = pd.read_csv(file_path, parse_dates=['Date'])
except ValueError as e:
    print(f"Error reading the file: {e}")
    exit()

# Отображение данных в табличном формате
print(data)

# Построение графиков изменения курсов валют
plt.figure(figsize=(12, 6))
plt.plot(data['Date'], data['Currency1'], label='Currency 1')
plt.plot(data['Date'], data['Currency2'], label='Currency 2')
plt.xlabel('Date')
plt.ylabel('Exchange Rate')
plt.title('Exchange Rate of Ruble to Two Currencies')
plt.legend()
plt.grid(True)
plt.show()
