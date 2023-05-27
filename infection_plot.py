import pandas as pd
import matplotlib.pyplot as plt

def infection_plt(dataframe, what_to_do, chart_name):
    # Сортируем датафрейм по регионам и датам
    dataframe = dataframe.sort_values(['Регион', 'Дата'])
    
    # Создаем пустой словарь для хранения данных 
    region_data = {}
    
    # Проходим по каждой строке датафрейма
    for index, row in dataframe.iterrows():
        # Получаем название региона, дату и население
        region = row['Регион']
        date = row['Дата']
        #zaraza = row['Заражений за день']
        zaraza = row[what_to_do]
        
        # Если регион еще не добавлена в словарь, создаем для нее новый список
        if region not in region_data:
            region_data[region] = [[zaraza, date]]
        else:
            # Иначе добавляем данные в список для данного регионы
            region_data[region].append([zaraza, date])
    
    # Создаем график для каждого региона
    for region, data in region_data.items():
        # Получаем даты и население для данного региона
        dates = [row[1] for row in data]
        zarazas = [row[0] for row in data]
        
        # Строим график
        plt.plot(dates, zarazas, label=region)
    
    # Добавляем легенду и метки осей
    plt.legend()
    plt.xlabel('Дата')
    plt.xticks(rotation=45)
    plt.ylabel(chart_name)
    
    # Отображаем график
    plt.show()
    
    