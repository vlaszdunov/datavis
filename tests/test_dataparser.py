from src.dataparser import *
import pandas as pd
import pytest

byte_test_data = open('tests/test_data.xlsx', 'rb').read()
test_data = pd.read_excel('tests/test_data.xlsx')

byte_formatted_test_data = open('tests/test_formatted_data.xlsx', 'rb').read()
formatted_test_data = pd.DataFrame(pd.read_excel(
    'tests/test_formatted_data.xlsx')).set_index('name')


def test_loading_data():
    test_function = load_groups_data(byte_test_data)
    assert test_function.equals(test_data)


# def test_formatting_data():
#     test_function_2 = format_groups_data(byte_test_data)
#     assert test_function_2.equals(formatted_test_data)
