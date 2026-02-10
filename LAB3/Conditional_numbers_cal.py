import math
m=int(input("Enter marks")) #input by user
if(0<m<10): #condition for single digit
    print(m**2)
elif(10<m<100): #condition for double digit
    print(math.sqrt(m))
else:
    print(math.cbrt(m)) #else statement
    

