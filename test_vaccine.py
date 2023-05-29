# import requests
# from bs4 import BeautifulSoup

# url = "https://gogov.ru/articles/covid-v-stats"

# response = requests.get(url)
# html = response.text

# soup = BeautifulSoup(html, "html.parser")
# table = soup.find("table", {"id": "m-table"})

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
#             print(data)
# else:
#     print("Таблица не найдена.")



import pandas as pd
import matplotlib.pyplot as plt


def draw_vaccination_pie_chart():
    data = {'Region': ['Москва', 'Санкт-Петербург', 'Ростовская обл.', 'Крым', 'Оренбургская обл.', 'Бурятия'],
                    'Percentage': [49.0, 57.3, 49.7, 50.4, 45.4, 51.8]
                    }
    dfN = pd.DataFrame(data)
    percentages = dfN['Percentage'].tolist()
    regions = dfN['Region'].tolist()
    plt.pie(percentages, labels=regions, autopct='%1.1f%%')
    plt.title('Процент вакцинированных от общего населения по регионам')
    plt.show()



