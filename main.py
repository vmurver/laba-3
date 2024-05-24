# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из текстового файла
file_path = r'C:\Valuta.txt'
data = pd.read_csv(file_path, parse_dates=['Date'])

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

# Вычисление максимальных изменений курса валют
data['Change_Currency1'] = data['Currency1'].diff()
data['Change_Currency2'] = data['Currency2'].diff()

max_gain_currency1 = data['Change_Currency1'].max()
max_loss_currency1 = data['Change_Currency1'].min()
max_gain_day_currency1 = data.loc[data['Change_Currency1'].idxmax(), 'Date']
max_loss_day_currency1 = data.loc[data['Change_Currency1'].idxmin(), 'Date']

max_gain_currency2 = data['Change_Currency2'].max()
max_loss_currency2 = data['Change_Currency2'].min()
max_gain_day_currency2 = data.loc[data['Change_Currency2'].idxmax(), 'Date']
max_loss_day_currency2 = data.loc[data['Change_Currency2'].idxmin(), 'Date']

print(f'Currency 1: Max Gain: {max_gain_currency1} on {max_gain_day_currency1}')
print(f'Currency 1: Max Loss: {max_loss_currency1} on {max_loss_day_currency1}')
print(f'Currency 2: Max Gain: {max_gain_currency2} on {max_gain_day_currency2}')
print(f'Currency 2: Max Loss: {max_loss_currency2} on {max_loss_day_currency2}')

# Реализация прогнозирования методом скользящей средней
N = 5  # Количество дней для прогнозирования
data['SMA_Currency1'] = data['Currency1'].rolling(window=N).mean()
data['SMA_Currency2'] = data['Currency2'].rolling(window=N).mean()

# Прогнозирование на следующие N дней
forecast_days = 10
last_date = data['Date'].iloc[-1]
dates = pd.date_range(start=last_date, periods=forecast_days + 1, closed='right')

forecast_currency1_values = [data['SMA_Currency1'].iloc[-1]] * forecast_days
forecast_currency2_values = [data['SMA_Currency2'].iloc[-1]] * forecast_days

forecast_data = pd.DataFrame({
    'Date': dates,
    'Currency1': forecast_currency1_values,
    'Currency2': forecast_currency2_values
})

# Объединение данных для отображения
combined_data = pd.concat([data, forecast_data], ignore_index=True)

# Построение графиков с прогнозированием
plt.figure(figsize=(12, 6))
plt.plot(combined_data['Date'], combined_data['Currency1'], label='Currency 1')
plt.plot(combined_data['Date'], combined_data['Currency2'], label='Currency 2')
plt.plot(forecast_data['Date'], forecast_data['Currency1'], 'r--', label='Forecast Currency 1')
plt.plot(forecast_data['Date'], forecast_data['Currency2'], 'b--', label='Forecast Currency 2')
plt.xlabel('Date')
plt.ylabel('Exchange Rate')
plt.title('Exchange Rate of Ruble to Two Currencies with Forecast')
plt.legend()
plt.grid(True)
plt.show()