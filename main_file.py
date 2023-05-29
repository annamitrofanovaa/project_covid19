import pandas as pd
import matplotlib.pyplot as plt
from infection_plot import infection_plt
from plot_for_region import plt_for_region
from seasons import season_statistic
from wave_duration import *

df = pd.read_excel('russian_data.xlsx')
df['Дата'] = pd.to_datetime(df['Дата'], format='%Y.%m.%d')

print("Что вы хотите сделать?")
choice = input("1. Вывести данные за всё время\n2. Вывести данные за определенный период\n")

if choice=="2":
    start_date = input('Введите начальную дату (ГГГГ.ММ.ДД): ')
    end_date = input('Введите конечную дату (ГГГГ.ММ.ДД): ')
    # Преобразование введенных дат в тип datetime
    start_date = pd.to_datetime(start_date, format='%Y.%m.%d')
    end_date = pd.to_datetime(end_date, format='%Y.%m.%d')
    # Оставляем только строки, значение в "Дата" которых входит в заданный промежуток
    df = df[(df['Дата'] >= start_date) & (df['Дата'] <= end_date)]

while True:
    print("Что вы хотите сделать?")
    choice = input("1. Вывести график (далее выбрать какой)\n2. Вывести статистику по временам года\n3. Проверить гипотезу \n4. Вывести динамику новых случаев для разных стран в абсолютных значениях и в %\n5. Длина волны для регионов\n6. Выход\n")
    if choice=="1":
        what = input("1. Количество зараженных \n2. Количество смертей  \n3.Количество выздоровлений\n")
        if what=="1":
            what_to_do = "Заражений за день" 
            chart_name = "Количество заражений"
            infection_plt(df, what_to_do, chart_name)
        if what == "2":
            what_to_do = "Смертей за день" 
            chart_name = "Количество Смертей"
            infection_plt(df, what_to_do, chart_name)
        if what== "3":
            what_to_do = "Выздоровлений за день"
            chart_name = "Количество выздоровлений" 
            infection_plt(df, what_to_do, chart_name)
    if choice == "2":
        #в какой сезон чаще заражались?
        season_statistic(df)
    if choice == "3":
        a=1
        #####АЛЬБИНА НАПИШИ
    if choice == "4":
        a=1
        #albinananan
    if choice == "5":
        A=1
        region = 'Ростовская обл.'
        wave_periods, decline_periods = estimate_wave_duration(df, region)
    if choice == "6":
        break
        