#ｎ＝１０まで出力するプログラム
def Fib(n):
    a=0
    b=1
    if n==0:
        return a
    elif n==1:
        return b
    else:
        return(Fib(n-1)+Fib(n-2))
for i in range (11):
    print("f"+str(i)+"="+str(Fib(i)))
    
