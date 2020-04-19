import random
#１から６の出力回数を表示
dice=[0]*6

n=1000
for i in range(n):
    work=random.randint(1,6)
    dice[work-1]+=1

for i in range(1,7):
    print(i,dice[i-1])
