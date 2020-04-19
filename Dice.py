import random
#１から６の出力回数を表示
dice=[]

n=1000
count1=0
count2=0
count3=0
count4=0
count5=0
count6=0
for i in range(n):
    x=random.randint(1,6)
    if x==1:
        count1+=1
    elif x==2:
        count2+=1
    elif x==3:
        count3+=1
    elif x==4:
        count4+=1
    elif x==5:
        count5+=1
    elif x==6:
        count6+=1

dice.append(count1)
dice.append(count2)
dice.append(count3)
dice.append(count4)
dice.append(count5)
dice.append(count6)

print("1",dice[0])
print("2",dice[1])
print("3",dice[2])
print("4",dice[3])
print("5",dice[4])
print("6",dice[5])
