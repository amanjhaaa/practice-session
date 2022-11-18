t = int(input("Entr the number of testcases:"))
for i in range(t):
    test = 'YES'
    n = int(input("Enter the number of spot :"))
    s = list(map(int,input().split(' ')))
    distance = 6
    for j in range(len(s)):
        distance =distance+1
        if s[j] ==1:
            if distance < 6:
                test ='NO'
                break
            else:
                distance = 0
    print(test)                