import csv
import string
import random
from collections import defaultdict
arquivo = open('1617FedSchoolCodeList.xlsx - 4th Quarter FSC.csv', encoding = "ISO-8859-1")

lines = arquivo.readlines()

# print("Id, SchoolCode and SchoolName")
# for l in lines:sss
#     print(l)
#     coluna = l.split(',')
#     print("id: " + coluna[0])
#     print("schoolCode: " + coluna[1])
#     print("SchoolName: " + coluna[2])
#     print("*******************************")
#
# [i for i,x in enumerate([1,2,3,2]) if x==2] # => [1, 3]

# print("city equals a 'CLEVELAND'")
# for l in lines:
#     coluna = l.split(',')
#     if 'CLEVELAND' in coluna:
#         print('achou', ('CLEVELAND' in coluna))

# print("SchoolName start with 'A'")
# for l in lines:
#     coluna = l.split(',')
#     if 'CLEVELAND' in coluna:
#         print('achou', ('CLEVELAND' in coluna))


print("StateCode equals a 'PR'")
for l in lines:
    coluna = l.split(',')
    if 'PR' in coluna[5]:
        print('Estado encontrado!')


print("SchoolName, City and StateCode equal '44106'")
for l in lines:
    coluna = l.split(',')
    print("SchoolName: " + coluna[2])
    print("City: " + coluna[4])
    print("StateCode: " + coluna[5])
    if '44106' in coluna[6]:
        print('find zipcode')

