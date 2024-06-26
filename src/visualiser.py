import os
from typing import Any

import matplotlib.pyplot as plt
import pandas as pd
import seaborn


def create_heatmap(dataset: dict[str, dict[str, Any]]):
    '''
    Creating and saving heatmaps as pictores

    Args:
        dataset (dict): dicts of dicts of pd.DataFrames
        of study group's and number of students in them
    '''

    if os.path.exists('exported') == False:
        os.mkdir('exported')

    for group in dataset.keys():
        formatted_group_list:pd.DataFrame = dataset[group]['group_list'].iloc[:, :-1].sum()\
            .to_frame().set_axis(['Кол-во студентов'], axis='columns')\
            .rename_axis('Номер пары').transpose()

        plt.title(f'Посещаемость {group}')
        seaborn.heatmap(formatted_group_list, annot=True,
                        cbar=False, linewidths=0.5)
        plt.savefig('exported/'+f'{group}.png')
        plt.cla()
        '''
        Generating heatmap with numeric annotations
        for study group without last column,
        that contains 1'st ex score
        '''

        seaborn.heatmap(formatted_group_list.div(dataset[group]['count']),
                        annot=True, cbar=False, linewidths=0.5)
        plt.savefig('exported/'+f'{group} в процентах.png')
        plt.cla()
        '''
        Generating heatmap with percentage annotations
        for study group without last column,
        that contains 1'st ex score
        '''
