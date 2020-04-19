#パスカルの三角形
nn = input('ｎ?')
n = int(nn)

pa=[0]*n
for i in range (n):
    pa[i]=[0]*n

for x in range(n):
    for y in range(n):
        if y==0:
            pa[x][y]=1
        elif x==y:
            pa[x][y]=1
        elif y>x:
            pa[x][y]=0
        elif 0<y<x:
            pa[x][y]=pa[x-1][y-1]+pa[x-1][y]

print(pa)
