
for i in range(int(input())):
    n, x, s = map(int, input().split())
    coin = x
    for i in range(s):
        a, b = map(int, input().split())
        if coin == a:
            coin = b
        elif coin == b:
            coin = a
    print(coin)
