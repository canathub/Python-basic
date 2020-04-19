#フィボナッチ数列
def fib(n):
    a=0
    b=1
    if n==0:
        return a
    elif n==1:
        return b
    else:
        return fib(n-1)+fib(n-2)

for i in range(11):
    print("f"+str(i)+"="+str(fib(i)))
