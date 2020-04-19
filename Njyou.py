#ｍのｎ乗を求める
m = int(input("m?"))
n = int(input("n?"))

if n == 0:
    print(str(m)+"の"+str(n)+"乗は１")

else:
    a = 1
    for i in range (n):
        a = a*m
    print(str(m)+"の"+str(n)+"乗は"+str(a))
