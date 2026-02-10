import math
m=int(input("Enter marks"))
if(0<m<10):
    print(m**2)
elif(10<m<100):
    print(math.sqrt(m))
else:
    print(math.cbrt(m))
