import os
from typing import Any

import matplotlib.pyplot as plt
import pandas as pd
import seaborn


def create_heatmap(dataset: dict[str, dict[str, Any]]):
    '''
    Creating and saving heatmaps as pictores

    Args:
        dataset (list): list of study group's pd.DataFrames
    '''

    if os.path.exists('exported') == False:
        os.mkdir('exported')

    for group in dataset.keys():
        # if dataset[group] == len(dataset)-1:
        #     seaborn.heatmap(dataset[group]['group_list'].iloc[:, :-1],
        #                     annot=True, cbar=False, linewidths=0.5)
        #     '''
        #     Generating heatmap for dataset[group] without last column,
        #     that contains 1'st ex score
        #     '''

        #     plt.title('Посещаемость всех групп')
        #     plt.savefig('exported/'+'all_groups.png')

        plt.title(f'Посещаемость группы {group}')
        seaborn.heatmap(dataset[group]['group_list'].iloc[:, :-1],
                        annot=True, cbar=False, linewidths=0.5)
        plt.savefig('exported/'+f'{group}.png')
        plt.cla()
