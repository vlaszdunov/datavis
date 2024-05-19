import pandas as pd
from io import BytesIO
import numpy as np


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
    all_data.columns = ['name'] + [i for i in range(1, 17)]+['бл 1']
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
    Аilling empty and str cells with zeros.
    Assigning a column with full name as row indexes
    '''
    return all_data


def create_list_of_groups(file_content: bytes) -> list[pd.DataFrame]:
    '''
    Split pd.Dataframe to several DataFrames
    for each study groups and combine them to list

    Args:
        file_content (bytes): byte content of the file

    Return:
        list_of_groups (list): List of pd.DataFrames with study group's data
    '''

    all_data = format_groups_data(file_content)
    mask_of_empty_cells = all_data.index.get_loc(0)
    zero_indexes: list[int] = list(np.where(mask_of_empty_cells == True)[0])[:-1]
    '''List of study group's divider's indexes'''

    dict_of_groups: dict[str,pd.DataFrame]={}
    all_data.insert(len(all_data.columns),'count',1)
    print(all_data)
    # for i in range(len(zero_indexes)-1):
    #     dict_of_groups[f'Группа {zero_indexes[i]+1}'] = all_data[zero_indexes[i]+1:zero_indexes[i+1]].astype(float).assign(count=[1 for i in range(all_data.count())])
    # list_of_groups: list[pd.DataFrame] = [all_data[zero_indexes[i]+1:zero_indexes[i+1]]
    #                                       .astype(float) for i in range(len(zero_indexes)-2)]
    # print(dict_of_groups)
    exit()
    '''Create list of study groups'''

    # list_of_groups.append(pd.concat(list_of_groups, axis=0)
    #                       .set_axis([f'Группа {i}' for i in range(1, len(list_of_groups)+1)],
    #                                 axis='index'))
    # '''Appending pd.Dataframe with all study groups to group's list'''
    return list_of_groups
# <----------------------------------------->
