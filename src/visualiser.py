import os

import matplotlib.pyplot as plt
import seaborn
import pandas as pd



def create_heatmap(dataset:list[pd.DataFrame]):
    # plt.figure(figsize=(10, 8))
    # # # plt.subplots(figsize=(8,6))
    # plt.subplots_adjust(left=0.5)
    # # plt.title('группа 1')
    if os.path.exists('exported') == False:
        os.mkdir('exported')
    for group in range(len(dataset)):
        seaborn.heatmap(dataset[group], annot=True, cbar=False)
        plt.savefig('exported/'+f'group {group+1}.png')
