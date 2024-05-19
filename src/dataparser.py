from io import BytesIO
from typing import Any

import numpy as np
import pandas as pd


# <---------Creating list of groups--------->
def load_groups_data(file_content: bytes) -> pd.DataFrame:
    '''
    Create Pandas DataFrame from byte content of the file

    Args:
        file_content (bytes): byte content of the file
    '''
    all_data = pd.DataFrame(pd.read_excel(BytesIO(file_content)))
    return all_data


def format_groups_data(file_content: bytes) -> pd.DataFrame:
    '''
    Converting data into a convenient format

    Args:
        file_content (bytes): byte content of the file

    Return:
        pd.DataFrame: DataFrame of file's content
    '''

    all_data = load_groups_data(file_content)
    all_data = all_data.loc[:, 'Unnamed: 1':'Оценки за задания']
    all_data.columns = ['name'] + [i for i in range(1,len(all_data.columns)-1)]+['бл 1']
    '''
    Removing unnecessary columns from a dataframe.
    Columns remain with full name, all pairs and grade for the first task
    Changing column's label
    '''

    all_data.fillna(0, inplace=True)
    all_data.set_index('name', inplace=True)
    all_data.replace(
        ['отмена пары', 'отмена', 'выходной', 'отм', 'пр', 'б'], 0, inplace=True)
    '''
    Filling empty and str cells with zeros.
    Assigning a column with full name as row indexes
    '''
    all_data.to_excel('a.xlsx')
    return all_data


def create_list_of_groups(file_content: bytes) -> dict[str, dict[str, Any]]:
    '''
    Split pd.Dataframe to several DataFrames
    for each study groups and combine them to list

    Args:
        file_content (bytes): byte content of the file

    Return:
        dict_of_groups (dict): contains dicts of pd.DataFrames
        of study group's and number of students in them
    '''

    all_data = format_groups_data(file_content)
    mask_of_empty_cells = all_data.index.get_loc(0)
    zero_indexes: list[int] = list(
        np.where(mask_of_empty_cells == True)[0])[:-1]
    '''List of study group's divider's indexes'''

    dict_of_groups: dict[str, dict[str, Any]] = {}
    for i in range(len(zero_indexes)-1):
        dict_of_groups[f'Группа {i+1}']={'count': zero_indexes[i+1] - zero_indexes[i]-1}
        dict_of_groups[f'Группа {i+1}'].update({
            'group_list': all_data[zero_indexes[i]+1:zero_indexes[i+1]].astype(float)})
    '''Create dict of study groups with the number of students in them'''

    return dict_of_groups
# <----------------------------------------->
