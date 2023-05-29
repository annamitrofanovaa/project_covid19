# import requests
# from bs4 import BeautifulSoup

# url = "https://gogov.ru/articles/covid-v-stats"

# # Отправляем GET-запрос и получаем HTML-страницу
# response = requests.get(url)
# html = response.text

# # Создаем объект BeautifulSoup для парсинга HTML
# soup = BeautifulSoup(html, "html.parser")

# # Находим таблицу по ее идентификатору или классу
# table = soup.find("table", {"id": "m-table"})

# # Проверяем, что таблица найдена
# if table:
#     # Получаем все строки таблицы
#     rows = table.find_all("tr")

#     # Проходим по каждой строке таблицы
#     for row in rows:
#         # Получаем все ячейки в текущей строке
#         cells = row.find_all("td")

#         # Извлекаем данные из ячеек и обрабатываем их
#         for cell in cells:
#             data = cell.text.strip()
#             # Обрабатываем данные по вашему усмотрению
#             print(data)
# else:
#     print("Таблица не найдена.")



import pandas as pd
import matplotlib.pyplot as plt

def draw_vaccination_pie_chart(df):
    percentages = df['Percentage'].tolist()
    regions = df['Region'].tolist()

    # Создаем круговую диаграмму
    plt.pie(percentages, labels=regions, autopct='%1.1f%%')

    # Добавляем заголовок диаграммы
    plt.title('Процент вакцинированных от общего населения по регионам')

    # Отображаем диаграмму
    plt.show()


data = {
    'Region': ['Москва', 'Санкт-Петербург', 'Ростовская обл.', 'Крым', 'Оренбургская обл.', 'Бурятия'],
    'Percentage': [49.0, 57.3, 49.7, 50.4, 45.4, 51.8]
}
dfNadya = pd.DataFrame(data)
draw_vaccination_pie_chart(dfNadya)

