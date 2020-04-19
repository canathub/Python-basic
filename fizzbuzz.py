#１～１００までを出力（３の倍数の時fizz,５の倍数のときbuzz,１５の倍数fizzbuzz）

for i in range(1,101):
    if i%15==0:
        print("fizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")

    print(i)
