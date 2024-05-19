from src.dataparser import *
import pandas as pd
import pytest

byte_test_data = open('tests/test_dataset/test_data.xlsx', 'rb').read()
test_data = pd.read_excel('tests/test_dataset/test_data.xlsx')


formatted_test_data = pd.DataFrame(pd.read_excel(
    'tests/test_dataset/test_formatted_data.xlsx')).set_index('name')

test_data_group_1 = pd.DataFrame(pd.read_excel(
    'tests/test_dataset/test_formatted_data_group_1.xlsx')).set_index('name').astype(float)
test_data_group_2 = pd.DataFrame(pd.read_excel(
    'tests/test_dataset/test_formatted_data_group_2.xlsx')).set_index('name').astype(float)
test_data_group_3 = pd.DataFrame(pd.read_excel(
    'tests/test_dataset/test_formatted_data_group_3.xlsx')).set_index('name').astype(float)

test_dict_data = {'Группа 1': {'count': 22, 'group_list': test_data_group_1},
                  'Группа 2': {'count': 20, 'group_list': test_data_group_2},
                  'Группа 3': {'count': 1, 'group_list': test_data_group_3}}


def test_loading_data():
    test_function = load_groups_data(byte_test_data)
    assert test_function.equals(test_data)


def test_formatting_data():
    test_function_2 = format_groups_data(byte_test_data)
    assert test_function_2.equals(formatted_test_data)


def test_splitting_data():
    test_function_3 = create_list_of_groups(byte_test_data)
    assert test_function_3.keys()==test_dict_data.keys()
    assert test_function_3['Группа 1'].keys()==test_dict_data['Группа 1'].keys()
    assert test_function_3['Группа 2'].keys()==test_dict_data['Группа 2'].keys()
    assert test_function_3['Группа 3'].keys()==test_dict_data['Группа 3'].keys()
    
    assert test_function_3['Группа 1']['count']==test_dict_data['Группа 1']['count']
    assert test_function_3['Группа 2']['count']==test_dict_data['Группа 2']['count']
    assert test_function_3['Группа 3']['count']==test_dict_data['Группа 3']['count']

    assert test_function_3['Группа 1']['group_list'].equals(test_dict_data['Группа 1']['group_list'])
    assert test_function_3['Группа 2']['group_list'].equals(test_dict_data['Группа 2']['group_list'])
    assert test_function_3['Группа 3']['group_list'].equals(test_dict_data['Группа 3']['group_list'])