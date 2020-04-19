#行列
a=[
[1,2,3],
[4,5,6],
[7,8,9]
]

b=[
[7,8,9],
[1,2,3],
[4,5,6]
]

wa=[0]*3
for i in range (3):
    wa[i]=[0]*3

sa=[0]*3
for i in range (3):
    sa[i]=[0]*3

for x in range(3):
    for y in range(3):
        wa[x][y]=a[x][y]+b[x][y]

for x in range(3):
    for y in range(3):
        sa[x][y]=a[x][y]-b[x][y]

print(wa)
print(sa)

seki=[0]*3
for i in range (3):
    seki[i]=[0]*3

for x in range(3):
    for y in range(3):
        for z in range (3):
            seki[x][y] += a[x][z]*b[z][y]

print(seki)
