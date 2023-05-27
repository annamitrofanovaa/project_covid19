# project_covid19
Выполняли: Митрофанова Анна (21.Б11), Пронина Надежда (21.Б13), Альжапарова Альбина (21.Б13)

## План действий и описания программ:
### preparing_file.py
Программа, которая фильтрует данные.
1. Скачали данные из https://datalens.yandex.ru/marketplace/f2eb8io5l5q4rp84feo1 в файл Russia.xlsx
2.  Выбираем регионы: Оренбург, Бурятия, Крым, Москва, СПб, Ростов
3.  Сортировка по дате
4.  Сохранение  обновленных данных в файл russian_data.xlsx (далее работа с ним)

### main.py
Программа, в которой реализованы все основные моменты из задания

### infection_plot.py
Функция, которая строит графики

## Задание
Дано: данные в открытом доступе (например, https://github.com/GoogleCloudPlatform/covid-19-open-data/blob/main/docs/table-epidemiology.md - о динамике новых случаев, числа смертей и https://github.com/GoogleCloudPlatform/covid-19-open-data/blob/main/docs/table-vaccinations.md - о вакцинации.. или же)
или же вот отсюда можно:
https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data
если по России, то можно с яндекс взять данные (yandex lens)

1. Загрузить данные в соответствующие Dataframes.
2. Оценить: динамику новых случаев для разных стран (за всё время и за конкретный период на выбор пользователя)
- в абсолютных значениях и в %
- длину каждой волны для разных стран (длительность подъемом и спусков)
- динамику смертности
- насколько запаздывает динамика выбывания (выздоровевшие и умершие) от числа зарегистрированных случаев
- проверить гипотезу: снижалось ли число новых случаев с ростом вакцинации, снижалось ли число смертей с ростом вакцинации
+ любой другой анализ на ваш выбор
3. все результаты визуализировать
