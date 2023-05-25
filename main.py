import pandas as pd
import matplotlib.pyplot as plt
from infection_plot import infection_plt

# Загрузка данных из файла
df = pd.read_excel('russian_data.xlsx')
df_all_time = df

# Преобразование столбца "Дата" в тип datetime
df['Дата'] = pd.to_datetime(df['Дата'], format='%Y.%m.%d %H:%M:%S')

# Ввод пользователем временного промежутка
start_date = input('Введите начальную дату (ГГГГ.ММ.ДД): ')
end_date = input('Введите конечную дату (ГГГГ.ММ.ДД): ')

# Преобразование введенных дат в тип datetime
start_date = pd.to_datetime(start_date, format='%Y.%m.%d')
end_date = pd.to_datetime(end_date, format='%Y.%m.%d')

# Оставляем только строки, значение в "Дата" которых входит в заданный промежуток
df = df[(df['Дата'] >= start_date) & (df['Дата'] <= end_date)]
# Удаление времени из столбца "Дата"
df['Дата'] = df['Дата'].dt.date

#вывести график для заданной даты
infection_plt(df)
#для всех дат
infection_plt(df_all_time)

