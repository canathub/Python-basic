#２次方程式の解を出力する
aa = input('a?')
a = int(aa)
bb = input('b?')
b = int(bb)
cc = input('c?')
c = int(cc)

xx = (-b+((b**2)-4*a*c)**1/2)/2*a
yy = (-b-((b**2)-4*a*c)**1/2)/2*a
x = float(xx)
y = float(yy)

if (b**2)-4*a*c>=0:
 print("解は"+str(x)+"と"+str(y))

else:
 print("解を求めることができない")
