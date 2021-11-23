# coding:utf_8
import openpyxl
import pandas as pd

database = pd.read_excel (r'tournament_test.xlsx')
# name = pd.DataFrame(database, columns= ['名前'])
# gender = pd.DataFrame(database, columns=['性別'])

# print(gender)
# print(database)

#前代のデータをlistに入れるプログラム
lists = []
for i in database.iterrows():
    lists.append(i)


male = []
female = []



for n in lists:
    print(n)
    print("//////////////")
    gender = pd.DataFrame(n, columns=['性別'])
    # print(gender)
    # print("¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥")

# for n in lists:
#     if pd.DataFrame(n, columns=['性別']) == '男':
#         print(n)
#         print("男")
#         print("---------------------")
#     else:
#         print(n)
#         print("女")
#         print("---------------------")