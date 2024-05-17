import os

import matplotlib.pyplot as plt
import seaborn
import pandas as pd


def create_heatmap(dataset: list[pd.DataFrame]):
    
    if os.path.exists('exported') == False:
        os.mkdir('exported')
    for group in range(len(dataset)):
        if group==len(dataset)-1:
            seaborn.heatmap(dataset[group].iloc[:,:-1], annot=True, cbar=False,linewidths=0.5)
            plt.title('Посещаемость всех групп')
            plt.savefig('exported/'+'all_groups.png')
        else:
            plt.title(f'Посещаемость группы {group+1}')
            seaborn.heatmap(dataset[group][:-1].transpose(), annot=True, cbar=False,linewidths=0.5)
            plt.savefig('exported/'+f'group {group+1}.png')
        plt.cla()
    
