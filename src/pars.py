import pandas as pd


class Parse:
    study_group_1=pd.DataFrame()
    study_group_2=pd.DataFrame()

    @staticmethod
    def __init__() -> None:
        all_data=pd.DataFrame(pd.read_excel('Downloaded\students_info.xlsx'))
        all_data.rename(columns={'Unnamed: 0':"index"},inplace=True)
        all_data.rename(columns={'Unnamed: 1':"name"},inplace=True)

        Parse.study_group_1=all_data.loc[1:22,'name':'итоги']
        Parse.study_group_2=all_data.loc[24:45,'name':'итоги']
        Parse.study_group_2=Parse.study_group_2.drop(44,axis=0)

        Parse.study_group_1.columns=['name']+[i for i in range(1,17)]
        Parse.study_group_2.columns=['name']+[i for i in range(1,17)]

        Parse.study_group_1.fillna(0,inplace=True)
        Parse.study_group_1.replace(['отмена пары','отмена','выходной','отм'],0,inplace=True)
        Parse.study_group_2.fillna(0,inplace=True)
        Parse.study_group_2.replace(['отмена пары','отмена','выходной','отм'],0,inplace=True)

        Parse.study_group_1=Parse.study_group_1.set_index("name")
        Parse.study_group_2=Parse.study_group_2.set_index("name")