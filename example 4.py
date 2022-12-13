number = int(input('Введите число: '))

#my_list = [[1,2,3], 'kjbib', (3,6,9)]
my_list =[]
#print(*my_list)
for i in range (-number, number +1):
    my_list.append(i)
print(*my_list, sep =', ', end = ' конец строки')