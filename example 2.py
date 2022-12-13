from decimal import Decimal as D

numbers = float(input('Insert the length'))

numbers0 =(numbers*100)/10

numberD = (D(str(numbers))*100)/10

def digit_after_dot_counter (num:float):
     count =0 
     div = 1
     while True:
        if num*div !=int(num*div):
            count +=1
            div*=10
        else: break 
     return count

print(digit_after_dot_counter(numbers))
print(numbers0)
print(numberD)