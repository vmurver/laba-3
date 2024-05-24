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

# Объединяем исходные данные с прогнозомdata_with_forecast = pd.concat([data, forecast_df])

# Построение графика с прогнозомplt.figure(figsize=(10, 6))
plt.plot(data['Год'], data['Инфляция'], marker='o', label='Инфляция')
plt.plot(forecast_df['Год'], forecast_df['Инфляция'], marker='o', linestyle='--', color='orange', label='Прогноз')
plt.xlabel('Год')
plt.ylabel('Инфляция (%)')
plt.title('Инфляция в России с прогнозом на ближайшие годы')
plt.legend()
plt.grid(True)
plt.show()
def calculate_future_price(current_price, inflation_forecast):
    """    Расчет будущей стоимости товара на основе прогноза инфляции.    :param current_price: Текущая стоимость товара.    :param inflation_forecast: Прогнозируемые значения инфляции.    :return: Прогнозируемая стоимость товара через N лет.    """    future_price = current_price
    for inflation in inflation_forecast:
        future_price *= (1 + inflation / 100)
    return future_price

# Пример: текущая стоимость товара 1000 рублейcurrent_price = 1000future_price = calculate_future_price(current_price, forecast_values)

print(f"Прогнозируемая стоимость товара через {n_years_forecast} лет: {future_price:.2f} рублей")
