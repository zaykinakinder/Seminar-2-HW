numbers = input ('Insert numbers:')
count = int(input('Введите точность:'))

print(numbers)
numbers = numbers.split('.')
print (numbers)

print (numbers[0]+'.'+numbers[1][0:count])

