# swapping without using 3rd variable 

a = 10

b = 20 

print(f'Before swapping : a : {a}  b : {b}')


a = a + b
b = a - b
a = a - b

print(f'After swapping : a : {a}  b : {b}')