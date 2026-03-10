import pandas as pd

#   Finding all subcurriculums from higher-level curriculums

def space():
    print('\n')

file_path = (r"C:\Users\andrea.macgown\OneDrive - Thermo Fisher Scientific\Desktop\TRAINING SYSTEM\OFFICIAL REPORTS FOR DEPARTMENTS\QC 10Mar2026.csv")

df = pd.read_csv(file_path)




'''
# Finding column indexes
for index, column in enumerate(df.columns):
    print(f"{index}   {column}")

0   Sub-Curriculum Title
1   Sub-Curriculum Parent ID
2   Curriculum ID
3   Curriculum Title
4   Curriculum Description
5   Item Type
6   Item ID
7   Revision Number
8   Item Title
9   Initial Period (Item)
10   Initial Number (Item)
11   Effective Date
12   Sub-Curriculum ID
13   Unnamed: 13
14   Unnamed: 14
15   Active
16   Date Created

'''