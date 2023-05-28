import pandas as pd
from datetime import datetime

def dinamics(df, city, ds, de):
  dataframe = df[df['Регион'] == city]
  #нахожу максимальное значение
  maxx = dataframe['Заражений за день'].max()
  date_maxx = dataframe[dataframe['Заражений за день'] == maxx].iloc[0]['Дата']
  #оценить показатели от начала до максимального значения, от максимального значения до конца, с самого начала до конца
  date_start = dataframe.iloc[0]['Дата']
  date_end = dataframe.iloc[dataframe.shape[0] - 1]['Дата']
  y1 = dataframe[dataframe['Дата'] == date_start].iloc[0]['Заражений за день']
  yn = dataframe[dataframe['Дата'] == date_end].iloc[0]['Заражений за день']
  print('----', 'ДАТА:', date_start, " - ", date_end, '----')
  print('средний абсолютный прирост в регионе ', city, 'равен:')
  y = abs(yn - y1) / (dataframe.shape[0] - 1)
  print(y)
  print('средний темп роста:')
  t = (yn/y1)**(1/(dataframe.shape[0] - 1))*100
  print(t, '%')
  print('средний темп прироста:')
  k = t - 100
  print(k, '%')
  print('---', 'ДЕНЬ С МАКСИМАЛЬНЫМ КОЛИЧЕСТВОМ ЗАРАЖЕНИЙ', date_maxx)
  print('Значения до дня с максимальным количеством заражений:')
  yn = maxx
  print('средний абсолютный прирост равен:')
  y = abs(yn - y1) / (dataframe.shape[0] - 1)
  print(y)
  print('средний темп роста:')
  t = (yn/y1)**(1/(dataframe.shape[0] - 1))*100
  print(t, '%')
  print('средний темп прироста:')
  k = t - 100
  print(k, '%')
  print('---------')
  print('Значения после дня с максимальным количеством заражений:')
  y1 = maxx
  yn = dataframe[dataframe['Дата'] == date_end].iloc[0]['Заражений за день']
  print('средний абсолютный прирост равен:')
  y = abs(yn - y1) / (dataframe.shape[0] - 1)
  print(y)
  print('средний темп роста:')
  t = (yn/y1)**(1/(dataframe.shape[0] - 1))*100
  print(t, '%')
  print('средний темп прироста:')
  k = t - 100
  print(k, '%', '\n')
  #---------- за выбранный промежуток
  date_start = ds
  date_end = de
  y1 = dataframe[dataframe['Дата'] == date_start].iloc[0]['Заражений за день']
  yn = dataframe[dataframe['Дата'] == date_end].iloc[0]['Заражений за день']
  print('----', 'ДАТА:', date_start, " - ", date_end, '----')
  print('Cредний абсолютный прирост в регионе ', city, ' равен:')
  y = abs(yn - y1) / (dataframe.shape[0] - 1)
  print(y)
  print('средний темп роста:')
  t = (yn/y1)**(1/(dataframe.shape[0] - 1))*100
  print(t, '%')
  print('средний темп прироста:')
  k = t - 100
  print(k, '%')
