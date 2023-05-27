import pandas as pd
import matplotlib.pyplot as plt
from infection_plot import infection_plt
from plot_for_region import plt_for_region

# Загрузка данных из файла
df = pd.read_excel('russian_data.xlsx')
df_all_time = df

# Преобразование столбца "Дата" в тип datetime
df['Дата'] = pd.to_datetime(df['Дата'], format='%Y.%m.%d')

# Ввод пользователем временного промежутка
start_date = input('Введите начальную дату (ГГГГ.ММ.ДД): ')
end_date = input('Введите конечную дату (ГГГГ.ММ.ДД): ')

# Преобразование введенных дат в тип datetime
start_date = pd.to_datetime(start_date, format='%Y.%m.%d')
end_date = pd.to_datetime(end_date, format='%Y.%m.%d')

# Оставляем только строки, значение в "Дата" которых входит в заданный промежуток
df = df[(df['Дата'] >= start_date) & (df['Дата'] <= end_date)]
# Удаление времени из столбца "Дата"
#df['Дата'] = df['Дата'].dt.date

##########################################################################################################3
#выводим графики
what_to_do = "Заражений за день" #или "Смертей" или "Выздоровлений за день" или .......
chart_name = "Количество заражений" #или "Количество смертей" или "Количество выздоровлений" или.....
###infection_plt(df, what_to_do, chart_name)
#для всех дат
###infection_plt(df_all_time, what_to_do, chart_name)

#посмотреть данные для одного региона
plt_for_region("Бурятия", df)