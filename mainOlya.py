import pandas as pd
import matplotlib.pyplot as plt

# Чтение данных из файлаdata = pd.read_csv('C:\inflation_data.txt')

# Вывод данных в табличном форматеprint(data)
# Построение графика инфляцииplt.figure(figsize=(10, 6))
plt.plot(data['Год'], data['Инфляция'], marker='o', label='Инфляция')
plt.xlabel('Год')
plt.ylabel('Инфляция (%)')
plt.title('Инфляция в России за последние 15 лет')
plt.legend()
plt.grid(True)
plt.show()
def moving_average_forecast(data, window, n_years):
    """    Прогнозирование методом скользящей средней.    :param data: Исходные данные о инфляции.    :param window: Размер окна скользящей средней.    :param n_years: Количество лет для прогноза.    :return: Список с прогнозируемыми значениями инфляции.    """    moving_avg = data['Инфляция'].rolling(window=window).mean().iloc[-1]
    forecast = [moving_avg] * n_years
    return forecast

window_size = 3  
# Размер окна скользящей среднейn_years_forecast = 5  # Количество лет для прогноза forecast_values = moving_average_forecast(data, window_size, n_years_forecast)

# Добавляем прогнозируемые годы и значения в DataFramelast_year = data['Год'].iloc[-1]
forecast_years = list(range(last_year + 1, last_year + 1 + n_years_forecast))
forecast_df = pd.DataFrame({'Год': forecast_years, 'Инфляция': forecast_values})
