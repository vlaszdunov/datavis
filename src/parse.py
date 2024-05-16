import pandas as pd
from io import BytesIO


class Parser:
    study_group_1: pd.DataFrame
    study_group_2: pd.DataFrame

    def __init__(self, file_content: bytes) -> None:
        all_data = pd.DataFrame(pd.read_excel(BytesIO(file_content)))

        all_data = all_data.iloc[:, 1:19]
        all_data.fillna(0, inplace=True)

        all_data.columns = [
            'name'] + [i for i in range(1, 17)]+['бл 1']

        all_data.set_index('name', inplace=True)

        all_data.replace(
            ['отмена пары', 'отмена', 'выходной', 'отм', 'пр', 'б'], 0, inplace=True)

        self.study_group_1 = all_data.iloc[24:44]
        self.study_group_1 = self.study_group_1.astype(float)

        self.study_group_2 = all_data.iloc[1:23]
        self.study_group_2 = self.study_group_2.astype(float)
