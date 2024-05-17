import pandas as pd
from io import BytesIO
import numpy as np


# <---------Creating list of groups--------->
def load_groups_data(file_content: bytes) -> pd.DataFrame:
    all_data = pd.DataFrame(pd.read_excel(BytesIO(file_content)))
    return all_data


def format_groups_data(file_content: bytes) -> pd.DataFrame:
    all_data = load_groups_data(file_content)
    all_data = all_data.loc[:, 'Unnamed: 1':'Оценки за задания']
    all_data.fillna(0, inplace=True)

    all_data.columns = [
        'name'] + [i for i in range(1, 17)]+['бл 1']

    all_data.set_index('name', inplace=True)

    all_data.replace(
        ['отмена пары', 'отмена', 'выходной', 'отм', 'пр', 'б'], 0, inplace=True)
    return all_data


def create_list_of_groups(file_content: bytes) -> list[pd.DataFrame]:
    all_data = format_groups_data(file_content)
    mask_of_empty_cells = all_data.index.get_loc(0)
    zero_indexes: list[int] = list(np.where(mask_of_empty_cells == True)[0])

    list_of_groups: list[pd.DataFrame] = [all_data[zero_indexes[i]+1:zero_indexes[i+1]].astype(float).sum().to_frame()
                                          for i in range(len(zero_indexes)-1)]
    return list_of_groups
