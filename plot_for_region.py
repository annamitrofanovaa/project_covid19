import pandas as pd
import matplotlib.pyplot as plt
def plt_for_region(reg_name, dataframe):

# загрузка данных из файла
    data = dataframe

    # фильтрация данных по региону
    region_data = data[data['Регион'] == reg_name]

    # построение граиков
    plt.plot(region_data['Дата'], region_data['Заражений за день'], label='Заражения')
    plt.plot(region_data['Дата'], region_data['Смертей за день'], label='Смерти')
    plt.plot(region_data['Дата'], region_data['Выздоровлений за день'], label='Выздоровления')

    # настройка осей и легенды
    plt.xlabel('Дата')
    plt.ylabel('Количество')
    plt.legend()

    # отображение граика
    plt.show()
