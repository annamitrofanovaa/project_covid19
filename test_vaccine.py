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
import numpy as np

dfN = pd.read_excel("vaccination_by_hand.xlsx")

def draw_vaccination_pie_chart():
    percentages = dfN['% от населения'].tolist()
    regions = dfN['Регион'].tolist()
    plt.pie(percentages, labels=regions, autopct='%1.1f%%')
    plt.title('Процент вакцинированных от общего населения по регионам')
    plt.show()


def draw_relation_fully_not_fully():
    dfN['привито, чел.'] = dfN['привито, чел.'].str.replace('\xa0', '').astype(int)
    dfN['полностью привито, чел.'] = dfN['полностью привито, чел.'].str.replace('\xa0', '').astype(int)

    fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(10, 12))
    fig.subplots_adjust(hspace=0.4)

    for i, row in dfN.iterrows():
        region = row['Регион']
        vaccinated = row['привито, чел.']
        fully_vaccinated = row['полностью привито, чел.']

        # Determine the position of the subplot in the grid
        row_idx = i // 2
        col_idx = i % 2

        # Plotting the bars for vaccinated and fully vaccinated individuals
        ax = axes[row_idx, col_idx]
        ax.bar(['Привито', 'Полностью привито'], [vaccinated, fully_vaccinated], color=['grey', 'green'])
        ax.set_title(region)
        ax.set_xlabel(' ')
        ax.set_ylabel('Количество людей')

    fig.suptitle('Статус вакцинации по регионам')
    plt.tight_layout()
    plt.show()




