import pandas as pd

all_data=pd.DataFrame(pd.read_excel('Downloaded\students_info.xlsx'))

all_data.rename(columns={'Unnamed: 0':"index"},inplace=True)
all_data.rename(columns={'Unnamed: 1':"name"},inplace=True)

study_group_1=all_data.loc[1:22,'name':'итоги']
study_group_2=all_data.loc[23:45,'name':'итоги']

study_group_1.columns=['name']+[i for i in range(1,17)]
study_group_2.columns=['name']+[i for i in range(1,17)]
a=study_group_1.isin(['отмена пары','отмена','выходной',''])

a.to_csv('a.csv')


study_group_1.to_csv('group_1.csv')
study_group_2.to_csv('group_2.csv')
