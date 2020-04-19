
a=[
[1,2,3],
[4,5,6],
[7,8,9]
]

c=[0]*3
for i in range (3):
    c[i]=[0]*3

for x in range(3):
    for y in range(3):
        c[x][y]=a[y][x]

print(c)
