import pandas as pd
import matplotlib.pyplot as plt

def plot_my(dataframe):
    # Сортируем датафрейм по странам и датам
    dataframe = dataframe.sort_values(['Регион', 'Дата'])
    
    # Создаем пустой словарь для хранения данных по странам
    country_data = {}
    
    # Проходим по каждой строке датафрейма
    for index, row in dataframe.iterrows():
        # Получаем название страны, дату и население
        country = row['Регион']
        date = row['Дата']
        zaraza = row['Заражений за день']
        
        # Если страна еще не добавлена в словарь, создаем для нее новый список
        if country not in country_data:
            country_data[country] = [[zaraza, date]]
        else:
            # Иначе добавляем данные в список для данной страны
            country_data[country].append([zaraza, date])
    
    # Создаем график для каждой страны
    for country, data in country_data.items():
        # Получаем даты и население для данной страны
        dates = [row[1] for row in data]
        zarazas = [row[0] for row in data]
        
        # Строим график
        plt.plot(dates, zarazas, label=country)
    
    # Добавляем легенду и метки осей
    plt.legend()
    plt.xlabel('Дата')
    plt.xticks(rotation=45)
    plt.ylabel('Всего заражений')
    
    # Отображаем график
    plt.show()

dataframe = pd.read_excel('my_date.xlsx')
plot_my(dataframe)
