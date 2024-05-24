import pandas as pd
import matplotlib.pyplot as plt

# Чтение данных из файлаfile_path = 'C:\\diseases_data.txt'data = pd.read_csv(file_path, delimiter=',')

# Вывод данных в табличном форматеprint(data)

# Построение графиков заболеваемостиplt.figure(figsize=(12, 8))
for column in data.columns[1:]:
    plt.plot(data['Год'], data[column], marker='o', label=column)
plt.xlabel('Год')
plt.ylabel('Количество случаев')
plt.title('Заболеваемость инфекциями в России за последние 15 лет')
plt.legend()
plt.grid(True)
plt.show()

# Вычисление изменений заболеваемости за 15 летchange = {}
for column in data.columns[1:]:
    initial_value = data[column].iloc[0]
    final_value = data[column].iloc[-1]
    change[column] = final_value - initial_value

# Наибольшее снижение и наименьшее снижениеmax_decrease = min(change, key=change.get)
min_decrease = max(change, key=change.get)

print(f"Наибольшее снижение заболеваемости: {max_decrease}, снижение на {change[max_decrease]}")
print(f"Наименьшее снижение заболеваемости: {min_decrease}, снижение на {change[min_decrease]}")

# Прогнозирование методом скользящей среднейdef moving_average_forecast(series, window, n_years):
    moving_avg = series.rolling(window=window).mean().iloc[-1]
    forecast = [moving_avg] * n_years
    return forecast

window_size = 3  # Размер окна скользящей среднейn_years_forecast = 8  # Количество лет для прогнозаforecast_data = {}
for column in data.columns[1:]:
    forecast_values = moving_average_forecast(data[column], window_size, n_years_forecast)
    forecast_data[column] = forecast_values

# Добавляем прогнозируемые годы и значения в DataFramelast_year = data['Год'].iloc[-1]
forecast_years = list(range(last_year + 1, last_year + 1 + n_years_forecast))
forecast_df = pd.DataFrame({'Год': forecast_years})

for column in data.columns[1:]:
    forecast_df[column] = forecast_data[column]