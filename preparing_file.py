import pandas as pd

df = pd.read_excel("Russia.xlsx")
#print(data.head())

# фильтруем строки
df = df[df['Регион'].isin(['Бурятия', 'Оренбургская обл.', 'Ростовская обл.','Москва','Санкт-Петербург','Крым','Регион'])]

# преобразование столбца "Дата" в формат даты
df['Дата'] = pd.to_datetime(df['Дата']).dt.date
# сортировка по возрастанию дат
df = df.sort_values(by='Дата')

# сохраняем результат в новый файл
df.to_excel('russian_data.xlsx', index=False)