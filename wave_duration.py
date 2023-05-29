# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# def estimate_wave_duration(df, region):
#     region_data = df[df['Регион'] == region].copy()

#     dates = region_data['Дата'].values
#     cases = region_data['Заражений за день'].values

#     # Вычисляем пороговое значение для определения начала и конца волны
#     threshold = 0.09
#     threshold_value = cases.max() * (1 - threshold)

#     # Находим индексы, где происходит переход через пороговое значение
#     crossings = np.where(np.diff(np.sign(cases - threshold_value)))[0]
#     # print(crossings)
#     if len(crossings) >= 2:
#         # Извлекаем индексы начала и конца волны
#         wave_start = crossings[0]
#         wave_end = crossings[-1]

#         wave_period = region_data.iloc[wave_start:wave_end+1]['Дата']
#         decline_period = region_data.iloc[wave_end:]['Дата']


#         plt.plot(region_data['Дата'], region_data['Заражений за день'], color='blue', label='Заражений за день')
#         plt.plot(region_data.iloc[wave_start:wave_end+1]['Дата'], region_data.iloc[wave_start:wave_end+1]['Заражений за день'], color='green', label='Период роста')
#         plt.plot(region_data.iloc[wave_end:]['Дата'], region_data.iloc[wave_end:]['Заражений за день'], color='red', label='Период спада')
#         plt.xlabel('Дата')
#         plt.ylabel('Заражений за день')
#         plt.title('Анализ волны заболеваемости')
#         plt.legend()
#         plt.show()


#         return wave_period, decline_period
#     else:
#         return None, None

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def estimate_wave_duration(df, region):
    region_data = df[df['Регион'] == region].copy()

    dates = region_data['Дата'].values
    cases = region_data['Заражений за день'].values

    # Вычисляем пороговое значение для определения начала и конца волны
    threshold = 0.09
    threshold_value = cases.max() * (1 - threshold)

    # Находим индексы, где происходит переход через пороговое значение
    crossings = np.where(np.diff(np.sign(cases - threshold_value)))[0]

    if len(crossings) >= 2:
        wave_periods = []
        decline_periods = []

        for i in range(len(crossings) - 1):
            wave_start = crossings[i]
            wave_end = crossings[i + 1]

            decline_start = wave_end
            if i < len(crossings) - 2:
                decline_end = crossings[i + 2]
            else:
                decline_end = len(cases) - 1

            wave_periods.append(region_data.iloc[wave_start:wave_end + 1]['Дата'])
            decline_periods.append(region_data.iloc[decline_start:decline_end + 1]['Дата'])

        plt.plot(region_data['Дата'], region_data['Заражений за день'], color='blue', label='Заражений за день')

        for i, wave_period in enumerate(wave_periods):
            decline_period = decline_periods[i]

            plt.plot(wave_period, region_data.loc[wave_period.index, 'Заражений за день'], color='green', label=f'Волна {i + 1}')
            plt.plot(decline_period, region_data.loc[decline_period.index, 'Заражений за день'], linestyle='--', linewidth=2, label=f'Спад {i + 1}')

            if i > 0:
                prev_wave_period = wave_periods[i - 1]
                prev_decline_period = decline_periods[i - 1]
                plt.plot(prev_decline_period, region_data.loc[prev_decline_period.index, 'Заражений за день'], linestyle='--', linewidth=2, label=f'Спад {i}')
            
        plt.xlabel('Дата')
        plt.ylabel('Заражений за день')
        plt.title('Анализ волны заболеваемости')
        plt.legend()
        plt.show()

        return wave_periods, decline_periods
    else:
        return None, None


# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# def estimate_wave_duration(df, region):
#     region_data = df[df['Регион'] == region].copy()

#     dates = region_data['Дата'].values
#     cases = region_data['Заражений за день'].values

#     # Вычисляем пороговое значение для определения начала и конца волны
#     threshold = 0.05
#     threshold_value = cases.max() * (1 - threshold)

#     wave_periods = []
#     decline_periods = []
#     wave_start = 0

#     for i in range(1, len(cases)):
#         if cases[i] > cases[i - 1]:
#             if i - wave_start >= 2:
#                 wave_periods.append(region_data.iloc[wave_start:i]['Дата'])

#         elif cases[i] < cases[i - 1]:
#             if cases[i - 1] > threshold_value and i - wave_start >= 2:
#                 decline_periods.append(region_data.iloc[wave_start:i]['Дата'])
#                 wave_start = i

#     if wave_start < len(cases) - 1 and len(cases) - wave_start >= 2:
#         wave_periods.append(region_data.iloc[wave_start:len(cases)]['Дата'])

#     plt.plot(region_data['Дата'], region_data['Заражений за день'], color='blue', label='Заражений за день')

#     for i, wave_period in enumerate(wave_periods):
#         decline_period = decline_periods[i] if i < len(decline_periods) else None

#         plt.plot(wave_period, region_data.loc[wave_period.index, 'Заражений за день'], label=f'Волна {i+1}')
        
#         if decline_period is not None:
#             plt.plot(decline_period, region_data.loc[decline_period.index, 'Заражений за день'], linestyle='--', linewidth=2, label=f'Спад {i + 1}')

#     plt.xlabel('Дата')
#     plt.ylabel('Заражений за день')
#     plt.title('Анализ волны заболеваемости')
#     plt.legend()
#     plt.show()

#     return wave_periods, decline_periods


