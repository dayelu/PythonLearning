
a = input("Please input an integer number：")

b = input("Please input another integer number：")

large = a if a >= b else b
small = b if a > b else a

print(f'The bigger number is {large}.')
print('The smaller number is {}.'.format(small))