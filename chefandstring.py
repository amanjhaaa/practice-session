testcase = int(input())

for x in range(testcase):
    s1=input()
    s2=input()
    count=0
    l2=len(s2)
    for i in range(len(s1)):
        if s1[i]==s2[0]:   
            end=i+l2
            sub1=s1[i:end]
            if s2==sub1:
                count+=1
    print (count)
