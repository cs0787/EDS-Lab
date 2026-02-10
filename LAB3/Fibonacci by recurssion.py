def recur_fibo(n):
    """
    Calculates the n-th Fibonacci number using recursion.
    The sequence starts with F(0) = 0 and F(1) = 1.
    """
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))

#user input and print the series
nterms = int(input("How many terms? "))

#Check if valid
if nterms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(recur_fibo(i))
