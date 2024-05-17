import os

import matplotlib.pyplot as plt
import seaborn



def create_heatmap(dataset):
    plt.figure(figsize=(10, 8))
    # plt.subplots(figsize=(8,6))
    plt.subplots_adjust(left=0.5)
    # plt.title('группа 1')
    seaborn.heatmap(dataset, annot=True, cbar=False,
                    square=True, annot_kws={'fontsize': 6})
    if os.path.exists('exported') == False:
        os.mkdir('exported')
    plt.savefig('exported/fig.png')
