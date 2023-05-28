import pandas as pd
from datetime import datetime

def dinamics(df, city, ds, de, what_to_do):
  dataframe = df[df['Регион'] == city]
  #нахожу максимальное значение
  maxx = dataframe[what_to_do].max()
  date_maxx = dataframe[dataframe[what_to_do] == maxx].iloc[0]['Дата']
  #оценить показатели от начала до максимального значения, от максимального значения до конца, с самого начала до конца
  date_start = dataframe.iloc[0]['Дата']
  date_end = dataframe.iloc[dataframe.shape[0] - 1]['Дата']
  y1 = dataframe[dataframe['Дата'] == date_start].iloc[0][what_to_do]
  #условие на случай если y1 окажется нулем - на ноль делить нельзя
  idx = 0
  while y1 == 0:
    date_start = dataframe.iloc[idx]['Дата']
    y1 = dataframe[dataframe['Дата'] == date_start].iloc[0][what_to_do]
    idx += 1
  yn = dataframe[dataframe['Дата'] == date_end].iloc[0][what_to_do]
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
  print('---', 'ДЕНЬ С МАКСИМАЛЬНЫМ ЗНАЧЕНИЕМ', date_maxx)
  print('Значения до:')
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
  print('Значения после:')
  y1 = maxx
  yn = dataframe[dataframe['Дата'] == date_end].iloc[0][what_to_do]
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
  y1 = dataframe[dataframe['Дата'] == date_start].iloc[0][what_to_do]
  yn = dataframe[dataframe['Дата'] == date_end].iloc[0][what_to_do]
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
