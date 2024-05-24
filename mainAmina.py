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
