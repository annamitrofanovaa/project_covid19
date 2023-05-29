import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#data = pd.read_excel('russian_data.xlsx')
#data['Дата'] = pd.to_datetime(data['Дата'], format='%Y.%m.%d')

def reg_dynamic(data, region):
    region_data = data[data['Регион'] == region]
    dd=region_data
    fig, ax = plt.subplots()
    ax.plot(region_data['Дата'], region_data['Заражений'], label='Заражений')
    ax.plot(region_data['Дата'], region_data['Смертей'], label='Смертей')
    ax.plot(region_data['Дата'], region_data['Выздоровлений'], label='Выздоровлений')
    ax.set_title(f'Статистика по региону {region}')
    ax.set_xlabel('Дата')
    ax.set_ylabel('Количество')
    ax.legend()
    plt.show()

    corr = np.corrcoef(region_data['Заражений'], region_data['Выздоровлений'])[0, 1]
    print('Коэффициент корреляции Пирсона между числом зарегистрированных случаев и числом выздоровлений:', corr)

    corr = np.corrcoef(region_data['Заражений'], region_data['Смертей'])[0, 1]
    print('Коэффициент корреляции Пирсона между числом зарегистрированных случаев и числом смертей:', corr)
    
    region_data['дата'] = pd.to_datetime(region_data['Дата']).dt.strftime('%mY')
    
    # расчет динамики выбывания
    region_data['recovery_rate'] = (region_data['Выздоровлений'] / region_data['Заражений']) * 100
    region_data['mortality_rate'] = (region_data['Смертей'] / region_data['Заражений']) * 100
    
    reg_data = region_data.groupby('Дата')[['recovery_rate', 'mortality_rate']].mean().reset_index()
    
    plt.plot(reg_data['Дата'], reg_data['recovery_rate'], label='Динамика выбывания выздоровлений')
    plt.plot(reg_data['Дата'], reg_data['mortality_rate'], label='Динамика выбывания смертности')
   
    plt.xlabel('Месяц')
    plt.ylabel('Динамика выбывания, %')
    plt.title('Динамика выбывания(смертности и выздоровлений) по месяцам')
    plt.legend()
    plt.show()
