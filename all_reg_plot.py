import pandas as pd
import matplotlib.pyplot as plt

def all_region_plt(df):

  
    df_grouped = df.groupby('Дата')['Заражений'].sum().reset_index()
    # построение графика
    plt.plot(df_grouped['Дата'], df_grouped['Заражений'])
    plt.xlabel('Дата')
    plt.ylabel('Количество зараженных')
    plt.title('Динамика заражений в 6-ти регионах')
    plt.show()