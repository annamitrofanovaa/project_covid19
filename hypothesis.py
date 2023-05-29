from datetime import datetime
import pandas as pd

def hypothesis(df, city, what_to_do):
  start_vaccination = pd.to_datetime('2020.12.02', format='%Y.%m.%d')
  #start_vaccination = pd.to_datetime('2021.11.19', format='%Y.%m.%d')
  dataframe = df[df['Регион'] == city]
  data = dataframe['Дата']
  zaraza = dataframe[what_to_do]
  plt.plot(data, zaraza)
  plt.xlabel('Дата')
  plt.xticks(rotation=45)
  plt.ylabel(what_to_do)
  plt.show()
  date_start = dataframe.iloc[0]['Дата']
  date_end = dataframe.iloc[dataframe.shape[0] - 1]['Дата']
  y1 = dataframe[dataframe['Дата'] == date_start].iloc[0][action]
  #условие на случай если y1 окажется нулем - на ноль делить нельзя
  idx = 0
  while y1 == 0:
    date_start = dataframe.iloc[idx]['Дата']
    y1 = dataframe[dataframe['Дата'] == date_start].iloc[0][action]
    idx += 1
  yn = dataframe[dataframe['Дата'] == date_end].iloc[0][action]
  y_sv = dataframe[dataframe['Дата'] == start_vaccination].iloc[0][action]
  print('показания "', action, '" с начала до начала вакцинации')
  t = (y_sv/y1)**(1/(dataframe.shape[0] - 1))*100
  print('средний темп прироста:')
  k1 = t - 100
  print(k1, '%')
  print('показания "', action, '" с начала вакцинации до конца')
  t = (yn/y_sv)**(1/(dataframe.shape[0] - 1))*100
  print('средний темп прироста:')
  k2 = t - 100
  print(k2, '%')
  if (k2 <= 0):
    print('Гипотеза верна')
  else:
    print('Гипотеза неверна')
