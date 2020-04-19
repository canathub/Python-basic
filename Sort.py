import random
#基本ソート
a=[]
max_v=0

for i in range(5):
    x=random.randint(1,100)
    a.append(x)

print("入れ替え前",a)

for i in range(5):
    if a[i]>a[0]:
        max_v=a[i]
        a[i]=a[0]
        a[0]=max_v

print("入れ替え後",a)
