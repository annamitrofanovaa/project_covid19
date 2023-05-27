import matplotlib.pyplot as plt
import pandas as pd

def season_statistic(data):
    # преобразование данных в столбце "Дата" формат даты/времени
    data['Дата'] = pd.to_datetime(data['Дата'])

    # создание нового столбца "Месяц"
    data['Месяц'] = data['Дата'].dt.month# группировка данных по месяцам и подсчет общего количества случаев заражения коронавирусом
    cases_by_month = data.groupby('Месяц')['Заражений за день'].sum()

    # визуализация данных в виде графика
    plt.plot(cases_by_month.index, cases_by_month.values)
    plt.xlabel('Месяц')
    plt.ylabel('Количество случаев заражения')
    plt.show()
