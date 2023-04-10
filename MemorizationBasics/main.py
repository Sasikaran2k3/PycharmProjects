a=0
b=1
n=999
def Fib(n,memo={}):
    if n<=2:
        return 1
    else:
        if n in memo:
            return memo[n]
        else:
            memo[n] = (Fib(n - 1, memo)) +(Fib(n - 2, memo))
            return memo[n]
print(Fib(n))

for i in range(2,n+1):
    c=a+b
    a=b
    b=c
print(c)