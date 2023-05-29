import pandas as pd
import matplotlib.pyplot as plt
from infection_plot import infection_plt
#from plot_for_region import plt_for_region
from seasons import season_statistic
from hypothesis import hypothesis
from dinamics import dinamics
from check_is_weekend import check_is_weekend
from pirson_dinamic import reg_dynamic
from test_vaccine import draw_vaccination_pie_chart
from all_reg_plot import all_region_plt

df = pd.read_excel('russian_data.xlsx')
df['Дата'] = pd.to_datetime(df['Дата'], format='%Y.%m.%d')
df_all_time = df #ПЕРЕМЕННАЯ АЛЬБИНЫ НЕ ТРОГАТЬ!!
#all_region_plt(df)
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
    choice = input("1. Вывести график (далее выбрать какой)\n2. Вывести статистику по временам года\n3. Проверить гипотезу \n4. Вывести динамику новых случаев для разных регионов в абсолютных значениях и в %\n5. Длина волны для регионов\n6. Проверить насколько часто встречалось такое, что на выходных 0 новых случаев\n7. Анализ динамики выбывания   \n8. Выход\n")
    if choice=="1":
        what = input("1. Количество зараженных \n2. Количество смертей  \n3. Количество выздоровлений \n4. Процент вакцинированных от общего нас. региона\n")
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
        if what == "4":
            draw_vaccination_pie_chart()
    if choice == "2":
        #в какой сезон чаще заражались?
        season_statistic(df)
    if choice == "3":
        print('Гипотеза: снижалось ли число новых случаев/смертей с ростом вакцинации?')
        print('Выберите действие:')
        what = input('1. Количество зараженных \n2. Количество смертей\n')
        if what == '1':
          action = "Заражений за день" 
        if what == '2':
          action = "Смертей за день"
        print('Выберите регион: ')
        what = input('1. Москва \n2. Санкт-Петербург\n3. Крым \n4. Оренбургская область \n5. Бурятия \n6. Ростовская область\n')
        if what == '1':
          city = "Москва"
        if what == '2':
          city = 'Санкт-Петербург'
        if what == '3':
          city = 'Крым'
        if what == '4':
          city = 'Оренбургская обл.'
        if what == '5':
          city = 'Бурятия'
        if what == '6':
          city = 'Ростовская обл.'
        hypothesis(df_all_time, city, action)
    if choice == "4":
        print('Выберите действие:')
        what = input('1. Количество зараженных \n2. Количество смертей\n3. Количество выздоровлений \n')
        if what == '1':
          action = "Заражений за день" 
        if what == '2':
          action = "Смертей за день"
        if what == '3':
          action = "Выздоровлений за день"
        print('Выберите регион: ')
        what = input('1. Москва \n2. Санкт-Петербург\n3. Крым \n4. Оренбургская область \n5. Бурятия \n6. Ростовская область\n')
        if what == '1':
          city = "Москва"
        if what == '2':
          city = 'Санкт-Петербург'
        if what == '3':
          city = 'Крым'
        if what == '4':
          city = 'Оренбургская обл.'
        if what == '5':
          city = 'Бурятия'
        if what == '6':
          city = 'Ростовская обл.'
        start_date = input('Введите начальную дату (ГГГГ.ММ.ДД): ')
        end_date = input('Введите конечную дату (ГГГГ.ММ.ДД): ')
        start_date = pd.to_datetime(start_date, format='%Y.%m.%d')
        end_date = pd.to_datetime(end_date, format='%Y.%m.%d')
        dinamics(df_all_time, city, start_date, end_date, action)
    if choice == "5":
        A=1
        #NADYAA
    if choice == "6":
        print('Выберите регион: ')
        what = input('1. Москва \n2. Санкт-Петербург\n3. Крым \n4. Оренбургская область \n5. Бурятия \n6. Ростовская область\n')
        if what == '1':
          city = "Москва"
        if what == '2':
          city = 'Санкт-Петербург'
        if what == '3':
          city = 'Крым'
        if what == '4':
          city = 'Оренбургская обл.'
        if what == '5':
          city = 'Бурятия'
        if what == '6':
          city = 'Ростовская обл.'
        cnt1, cnt2, cnt3 = check_is_weekend(df_all_time, city)
        print('Всего дней с нулевым количеством заражений в данном регионе:', cnt1)
        print('Сколько из таких дней - выходные:', cnt2)
        print('Сколько было понедельников тахих, что на выходных было 0 заражений:', cnt3)
        labels = 'Нулевое кол-во заражений', 'Выходные', 'Понедельники с нулевыми выходными'
        sizes = [cnt1, cnt2, cnt3]
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels)
        ax1.axis('equal')  
        plt.show()
    if choice =="7":
        print('Выберите регион: ')
        what = input('1. Москва \n2. Санкт-Петербург\n3. Крым \n4. Оренбургская область \n5. Бурятия \n6. Ростовская область\n')
        if what == '1':
          city = "Москва"
        if what == '2':
          city = 'Санкт-Петербург'
        if what == '3':
          city = 'Крым'
        if what == '4':
          city = 'Оренбургская обл.'
        if what == '5':
          city = 'Бурятия'
        if what == '6':
          city = 'Ростовская обл.' 
        print(city)
        reg_dynamic(df, city)
    if choice == "8":
        break
        