from datetime import datetime
#я еще доделаю тут

def check_is_weekend(df, city):
  dataframe = df[df['Регион'] == city]
  cnt = 0
  cnt2 = 0
  for i in range(dataframe.shape[0]):
    if dataframe.iloc[i]['Заражений за день'] == 0:
      cnt += 1
      if (datetime.weekday(df.iloc[i]['Дата']) == 6 or datetime.weekday(df.iloc[i]['Дата']) == 5):
        cnt2 += 1
  cnt3 = 0
  for i in range(dataframe.shape[0] - 1):
    if dataframe.iloc[i]['Заражений за день'] == 0 and dataframe.iloc[i + 1]['Заражений за день'] != 0 and datetime.weekday(dataframe.iloc[i + 1]['Дата']) == 0:
        cnt3 += 1
  
  return cnt, cnt2, cnt3
