#角谷の予想
x = input("n?")
n = int(x)

print(int(n))

count = 0
if n < 1:
    print("1以上の整数を入力してください")

else:
    while n > 1:
        if n % 2 == 0:
            n = n / 2
            print(int(n))
            count += 1
        elif n % 2 == 1:
            n = n * 3 + 1
            print(int(n))
            count += 1

print("１になるまでの回数は"+str(count)+"回")
