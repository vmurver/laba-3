# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
def plot_exchange_rates():
    file_path = r'C:\Valuta.txt'
    data = pd.read_csv(file_path, parse_dates=['Дата'])
    print(data)

    plt.figure(figsize=(12, 6))
    plt.plot(data['Дата'], data['Доллар'], label='Доллар')
    plt.plot(data['Дата'], data['Евро'], label='Евро')
    plt.xlabel('Дата')
    plt.ylabel('Курс обмена')
    plt.title('Курс обмена рубля к доллару и евро')
    plt.legend()
    plt.grid(True)
    plt.show()

    data['Изменение_доллара'] = data['Доллар'].diff()
    data['Изменение_евро'] = data['Евро'].diff()

    max_gain_currency1 = data['Изменение_доллара'].max()
    max_loss_currency1 = data['Изменение_доллара'].min()
    max_gain_day_currency1 = data.loc[data['Изменение_доллара'].idxmax(), 'Дата']
    max_loss_day_currency1 = data.loc[data['Изменение_доллара'].idxmin(), 'Дата']

    max_gain_currency2 = data['Изменение_евро'].max()
    max_loss_currency2 = data['Изменение_евро'].min()
    max_gain_day_currency2 = data.loc[data['Изменение_евро'].idxmax(), 'Дата']
    max_loss_day_currency2 = data.loc[data['Изменение_евро'].idxmin(), 'Дата']

    print(f'Доллар: Максимальный подъем: {max_gain_currency1} на {max_gain_day_currency1}')
    print(f'Доллар: Максимальное падение: {max_loss_currency1} на {max_loss_day_currency1}')
    print(f'Евро: Максимальный подъем: {max_gain_currency2} на {max_gain_day_currency2}')
    print(f'Евро: Максимальное падение: {max_loss_currency2} на {max_loss_day_currency2}')

    N = 5
    data['SMA_Доллар'] = data['Доллар'].rolling(window=N).mean()
    data['SMA_Евро'] = data['Евро'].rolling(window=N).mean()

    forecast_days = 10
    last_date = data['Дата'].iloc[-1]
    dates = pd.date_range(start=last_date, periods=forecast_days + 1, inclusive='right')

    forecast_currency1_values = [data['SMA_Доллар'].iloc[-1]] * forecast_days
    forecast_currency2_values = [data['SMA_Евро'].iloc[-1]] * forecast_days

    forecast_data = pd.DataFrame({
        'Дата': dates,
        'Доллар': forecast_currency1_values,
        'Евро': forecast_currency2_values
    })

    combined_data = pd.concat([data, forecast_data], ignore_index=True)

    plt.figure(figsize=(12, 6))
    plt.plot(combined_data['Дата'], combined_data['Доллар'], label='Доллар')
    plt.plot(combined_data['Дата'], combined_data['Евро'], label='Евро')
    plt.plot(forecast_data['Дата'], forecast_data['Доллар'], 'r--', label='Прогноз доллара')
    plt.plot(forecast_data['Дата'], forecast_data['Евро'], 'b--', label='Прогноз евро')
    plt.xlabel('Дата')
    plt.ylabel('Курс обмена')
    plt.title('Курс обмена рубля к доллару и евро с прогнозом')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_inflation():
    data = pd.read_csv(r'C:\inflation_data.txt')
    print(data)

    plt.figure(figsize=(10, 6))
    plt.plot(data['Год'], data['Инфляция'], marker='o', label='Инфляция')
    plt.xlabel('Год')
    plt.ylabel('Инфляция (%)')
    plt.title('Инфляция в России за последние 15 лет')
    plt.legend()
    plt.grid(True)
    plt.show()

    def moving_average_forecast(data, window, n_years):
        moving_avg = data['Инфляция'].rolling(window=window).mean().iloc[-1]
        forecast = [moving_avg] * n_years
        return forecast

    window_size = 3
    n_years_forecast = 5
    forecast_values = moving_average_forecast(data, window_size, n_years_forecast)

    last_year = data['Год'].iloc[-1]
    forecast_years = list(range(last_year + 1, last_year + 1 + n_years_forecast))
    forecast_df = pd.DataFrame({'Год': forecast_years, 'Инфляция': forecast_values})

    data_with_forecast = pd.concat([data, forecast_df])

    plt.figure(figsize=(10, 6))
    plt.plot(data['Год'], data['Инфляция'], marker='o', label='Инфляция')
    plt.plot(forecast_df['Год'], forecast_df['Инфляция'], marker='o', linestyle='--', color='orange', label='Прогноз')
    plt.xlabel('Год')
    plt.ylabel('Инфляция (%)')
    plt.title('Инфляция в России с прогнозом на ближайшие годы')
    plt.legend()
    plt.grid(True)
    plt.show()

    def calculate_future_price(current_price, inflation_forecast):
        future_price = current_price
        for inflation in inflation_forecast:
            future_price *= (1 + inflation / 100)
        return future_price

    current_price = 1000
    future_price = calculate_future_price(current_price, forecast_values)
    print(f"Прогнозируемая стоимость товара через {n_years_forecast} лет: {future_price:.2f} рублей")

def plot_disease():
    file_path = r'C:\diseases_data.txt'
    data = pd.read_csv(file_path, delimiter=',')
    print(data)

    plt.figure(figsize=(12, 8))
    for column in data.columns[1:]:
        plt.plot(data['Год'], data[column], marker='o', label=column)
    plt.xlabel('Год')
    plt.ylabel('Количество случаев')
    plt.title('Заболеваемость инфекциями в России за последние 15 лет')
    plt.legend()
    plt.grid(True)
    plt.show()

    change = {}
    for column in data.columns[1:]:
        initial_value = data[column].iloc[0]
        final_value = data[column].iloc[-1]
        change[column] = final_value - initial_value

    max_decrease = min(change, key=change.get)
    min_decrease = max(change, key=change.get)

    print(f"Наибольшее снижение заболеваемости: {max_decrease}, снижение на {change[max_decrease]}")
    print(f"Наименьшее снижение заболеваемости: {min_decrease}, снижение на {change[min_decrease]}")

    def moving_average_forecast(series, window, n_years):
        moving_avg = series.rolling(window=window).mean().iloc[-1]
        forecast = [moving_avg] * n_years
        return forecast

    window_size = 3
    n_years_forecast = 8
    forecast_data = {}
    for column in data.columns[1:]:
        forecast_values = moving_average_forecast(data[column], window_size, n_years_forecast)
        forecast_data[column] = forecast_values

    last_year = data['Год'].iloc[-1]
    forecast_years = list(range(last_year + 1, last_year + 1 + n_years_forecast))
    forecast_df = pd.DataFrame({'Год': forecast_years})

    for column in data.columns[1:]:
        forecast_df[column] = forecast_data[column]

    combined_data = pd.concat([data, forecast_df])

    plt.figure(figsize=(12, 8))
    for column in combined_data.columns[1:]:
        plt.plot(combined_data['Год'], combined_data[column], marker='o', label=column)
    plt.xlabel('Год')
    plt.ylabel('Количество случаев')
    plt.title('Заболеваемость инфекциями в России за последние 15 лет с прогнозом')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    while True:
        print("Выберите график для отображения:")
        print("1. Курсы валют")
        print("2. Инфляция")
        print("3. Заболеваемость")
        print("4. Выход")

        choice = input("Введите номер графика (1-4): ")

        if choice == '1':
            plot_exchange_rates()
        elif choice == '2':
            plot_inflation()
        elif choice == '3':
            plot_disease()
        elif choice == '4':
            break
        else:
            print("Неверный ввод. Пожалуйста, введите номер от 1 до 4.")

if __name__ == "__main__":
    main()
