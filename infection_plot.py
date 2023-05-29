import pandas as pd
import matplotlib.pyplot as plt

def infection_plt(dataframe, what_to_do, chart_name):
    dataframe = dataframe.sort_values(['Регион', 'Дата'])
    region_data = {}
    
    for index, row in dataframe.iterrows():
        region = row['Регион']
        date = row['Дата']
        zaraza = row[what_to_do]
        
        if region not in region_data:
            region_data[region] = [[zaraza, date]]
        else:
            region_data[region].append([zaraza, date])
    
    # график для каждого региона
    for region, data in region_data.items():
        # даты и население для данного региона
        dates = [row[1] for row in data]
        zarazas = [row[0] for row in data]
        
        plt.plot(dates, zarazas, label=region)
    
    plt.legend()
    plt.xlabel('Дата')
    plt.xticks(rotation=45)
    plt.ylabel(chart_name)
    
    plt.show()
    
    