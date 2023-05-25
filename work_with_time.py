import pandas as pd

# Загрузка данных из файла
df = pd.read_excel('russian_data.xlsx')
# Преобразование столбца "Дата" в тип datetime
df['Дата'] = pd.to_datetime(df['Дата'], format='%Y.%m.%d %H:%M:%S')
# Ввод пользователем временного промежутка
start_date = input('Введите начальную дату (ГГГГ.ММ.ДД): ')
end_date = input('Введите конечную дату (ГГГГ.ММ.ДД): ')
# Преобразование введенных дат в тип datetime
start_date = pd.to_datetime(start_date, format='%Y.%m.%d')
end_date = pd.to_datetime(end_date, format='%Y.%m.%d')
# Оставляем только строки, значение в "ДАТА" в которых входит в заданный промежуток
df = df[(df['Дата'] >= start_date) & (df['Дата'] <= end_date)]
# Удаление времени из столбца "Дата"
df['Дата'] = df['Дата'].dt.date
# Вывод результата
df.to_excel('choosen_data.xlsx', index=False)



