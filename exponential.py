import math

x = int(input('Input the value of x: '))
sp = int(input('Input the value of the stopping point: '))

c = 0
sum = 0
while c <= sp:
    sum = sum + ((x**c)/ math.factorial(c))
    print(sum)
    c += 1
    
print('e^x:',sum)
 
