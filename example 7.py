#3n+1
number = int(input('Введите число:'))
my_list =[]
for i in range (1, number+1):
    k=str(3*i+1)
   # my_list.append(str(i)+':'+k)
    my_list.append(f'{i}: {3*i+1}')
print(my_list)