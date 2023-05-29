import pandas as pd

df = pd.read_excel("Russia.xlsx")

df = df[df['Регион'].isin(['Бурятия', 'Оренбургская обл.', 'Ростовская обл.','Москва','Санкт-Петербург','Крым','Регион'])]

df['Дата'] = pd.to_datetime(df['Дата']).dt.date
# сортировка по возрастанию дат
df = df.sort_values(by='Дата')

df.to_excel('russian_data.xlsx', index=False)