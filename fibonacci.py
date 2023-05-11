def fibo(n): # n is the nth Fibonacci no. in the sequence
    fib = {} # dict to store earlier values
    for k in range(1, n + 1): # iterating each time
    if k <= 1 : 
                f = 0
    if k == 2 : 
            f = 1
    else:
        f = fib[k - 1] + fib[k - 2] # looking up in the fib{}
fib[k] = f
return fib[n] # returns the nth Fibonacci number

n = int(input('Enter n = '))
print('%dth fibo no. is = %d' %(n, fibo(n))) # calling n printing
