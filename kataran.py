#カタラン数を求める
nn = input('ｎ?')
n = int(nn)

#パスカルの三角形
pa=[0]*(2*n+1)
for i in range (2*n+1):
    pa[i]=[0]*(2*n+1)

for x in range(2*n+1):
    for y in range(2*n+1):
        if y==0 or x==y:
            pa[x][y]=1
        elif y<x:
            pa[x][y]=pa[x-1][y-1]+pa[x-1][y]

#カタラン数を示す
ka=[0]*n
for i in range(n):
    ka[i]=pa[2*(i+1)][i+1]/((2*(i+1)+2)/2)
    print(i+1,":",ka[i])
