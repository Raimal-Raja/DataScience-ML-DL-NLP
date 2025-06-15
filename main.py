## file handling and exception handling
# try:
#     file = open('example.txt', 'r')
#     content = file.read()
#     a=b
#     print(content)
# except FileNotFoundError:
#     print('The file does not exists')
    
# except Exception as e:
#     print(e)
    
# finally:
#     if 'file' in locals() and not file.closed():
#         file.close()
#         print('file closed')


## Generators
# def sqaure(n):
#     for i in range(3):
#         yield i**2
        
# print(sqaure(3))
# for i in sqaure(3):
#     print(i)


# Decorators
# def welcome():
#     return "Welcome to the welcome function"

# wel = welcome()

# del wel
# print(wel)

# list = [1,2,34]
# print(list)

import pandas as pd
import matplotlib.pyplot as plt
# path = 'example.csv'
# data_file = pd.read_csv(path)
# print(data_file.head(2))


# df = pd.read_csv('annual-enterprise.csv')
# # print(file_data)

# df['missing_values'] = df['value'].fillna(df['value'].mean())

# print(df)

# data = [1,2,2,3,3,3,4,4,4,4,5,5,5,5]
# plt.hist(data,bins=5,color='blue', edgecolor='black')
