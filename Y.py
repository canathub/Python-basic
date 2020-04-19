#Yをつくる

for y in range(11):
    for x in range(13):
        if y<5 and x==y:
            print("#",end="")

        elif x>=8 and x+y==12:
            print("#",end="")

        elif x==6 and y>=6:
            print("#",end="")

        else:
            print(" ",end="")

    print()
