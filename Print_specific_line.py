'''<<<<< METHOD 1 >>>>>'''
import linecache
line = linecache.getline('quotes.txt', 5)
print(line)

'''<<<<< METHOD 2 >>>>>'''
# line_number = 5
# with open('quotes.txt', 'r') as f:
#     for i, line in enumerate(f):
#         if i == line_number - 1:
#             print(line)
#             break

'''<<<<< METHOD 3 >>>>>'''
# line_number = 5
# try:
#     with open('quotes.txt', 'r') as f:
#         for i, line in enumerate(f):
#             if i == line_number - 1:
#                 print(line)
#                 break
# except IndexError as e:
#     print(e)
