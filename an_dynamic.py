import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#data = pd.read_excel('russian_data.xlsx')
#data['Дата'] = pd.to_datetime(data['Дата'], format='%Y.%m.%d')

def reg_dynamic(data, region):
    region_data = data[data['Регион'] == region]
    fig, ax = plt.subplots()
    ax.plot(region_data['Дата'], region_data['Заражений'], label='Заражений')
    ax.plot(region_data['Дата'], region_data['Смертей'], label='Смертей')
    ax.plot(region_data['Дата'], region_data['Выздоровлений'], label='Выздоровлений')
    ax.set_title(f'Статистика по региону {region}')
    ax.set_xlabel('Дата')
    ax.set_ylabel('Количество')
    ax.legend()
    plt.show()

    # вычисление коэффициента корреляции Пирсона между числом зарегистрированных случаев и числом выздоровевших/умерших
    corr = np.corrcoef(data['Заражений'], data['Выздоровлений'])[0, 1]
    print('Коэффициент корреляции Пирсона между числом зарегистрированных случаев и числом выздоровлений:', corr)

    corr = np.corrcoef(data['Заражений'], data['Смертей'])[0, 1]
    print('Коэффициент корреляции Пирсона между числом зарегистрированных случаев и числом смертей:', corr)
    
    # преобразование даты к формату "месяц-год"
    data['дата'] = pd.to_datetime(data['Дата']).dt.strftime('%mY')
    
    # расчет динамики выбывания
    data['recovery_rate'] = (data['Выздоровлений'] / data['Заражений']) * 100
    data['mortality_rate'] = (data['Смертей'] / data['Заражений']) * 100
    
    # группировка данных по месяцам и расчет среднего значения динамики выбывания
    data = data.groupby('Дата')[['recovery_rate', 'mortality_rate']].mean().reset_index()
    
    # визуализация результатов
    plt.plot(data['Дата'], data['recovery_rate'], label='Динамика выбывания выздоровлений')
    plt.plot(data['Дата'], data['mortality_rate'], label='Динамика выбывания смертности')
   
    plt.xlabel('Месяц')
    plt.ylabel('Динамика выбывания, %')
    plt.title('Динамика выбывания(смертности и выздоровлений) по месяцам')
    plt.show()
