import os

import matplotlib.pyplot as plt
import seaborn


def heatmap(dataset):

    plt.figure(figsize=(8, 6))
    plt.subplots_adjust(left=0.5)
    seaborn.heatmap(dataset, annot=True, cbar=False)
    if os.path.exists('exported') == False:
        os.mkdir('exported')
    plt.savefig('exported/fig.png')
