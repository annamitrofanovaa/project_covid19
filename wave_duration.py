import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def estimate_wave_duration(df, region):
    region_data = df[df['Регион'] == region].copy()

    dates = region_data['Дата'].values
    cases = region_data['Заражений за день'].values

    # print("cases = ")
    # print(cases)
    
    rises = []  # список для длительности подъемов
    falls = []  # список для длительности спадов
    rise_values = []  # список значений в каждом подъеме
    fall_values = []  # список значений в каждом спаде

    current_wave = []  # текущая волна (подъем или спад)
    current_trend = None  # текущий тренд: 'rise' (подъем) или 'fall' (спад)

    for i in range(1, len(cases)):
        if cases[i] <= cases[i-1]:  
            if current_trend != 'rise':  # Если тренд изменился, сохраняем предыдущую волну и начинаем новую
                if current_wave:
                    rises.append(len(current_wave))
                    rise_values.append(current_wave)
                current_wave = [cases[i-1], cases[i]]
                current_trend = 'rise'
            else:  # Продолжаем текущую волну
                current_wave.append(cases[i])
        else:   
            if current_trend != 'fall':   # Если тренд изменился, сохраняем предыдущую волну и начинаем новую
                if current_wave:
                    falls.append(len(current_wave))
                    fall_values.append(current_wave)
                current_wave = [cases[i-1], cases[i]]
                current_trend = 'fall'
            else:  # Продолжаем текущую волну
                current_wave.append(cases[i])

    # Добавляем последнюю волну в соответствующий список
    if current_wave:
        if current_trend == 'rise':
            rises.append(len(current_wave))
            rise_values.append(current_wave)
        else:
            falls.append(len(current_wave))
            fall_values.append(current_wave)
    

    # Выводим длительности подъемов и спадов    
    print("Длительность подъемов (в днях):", rises)
    print("Длительность спадов (в днях):", falls)

    print("Значения в подъемах:")
    for i, values in enumerate(rise_values):
        print("Подъем", i+1, ":", values)

    print("Значения в спадах:")
    for i, values in enumerate(fall_values):
        print("Спад", i+1, ":", values)

    # Строим график
    plt.plot(region_data['Дата'],cases)
    
    # Отображаем волны
    # for i, wave in enumerate(rise_values):
    #     x_wave = np.arange(len(wave))
    #     x_offset = np.sum(rises[:i])  # Смещение для горизонтальной оси
    #     plt.plot(x_wave + x_offset, wave, color='blue')

    # for i, wave in enumerate(fall_values):
    #     x_wave = np.arange(len(wave))
    #     x_offset = np.sum(rises[:len(rise_values)]) + np.sum(falls[:i])  # Смещение для горизонтальной оси
    #     plt.plot(x_wave + x_offset, wave, color='blue')

    plt.title(f'Длительность волн для региона: {region}')
    plt.xlabel('Дни')
    plt.ylabel('Значение')
    plt.xticks(rotation = 45)

    table_text = f'Rises: {rises}\nFalls: {falls}'
    plt.text(0.75, 0.95, table_text, transform=plt.gca().transAxes, fontsize=10, va='top')

    plt.show()
