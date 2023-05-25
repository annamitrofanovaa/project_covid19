import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("Russia.xlsx")
#print(data.head())

# фильтруем строки
df = df[df['Регион'].isin(['Бурятия', 'Оренбургская обл.', 'Ростовская обл.','Москва','Санкт-Петербург','Крым','Регион'])]

# сохраняем результат в новый файл
df.to_excel('russian_data.xlsx', index=False)