T = int(input("Enter the number of testcases"))
for x in range(T):
    N = int(input("Enter the number of element in the seriies:"))
    seq = [0,0]
    if N == 1:
        print(1)
    elif N == 2:
        print(2)
    else:
        while len(seq)!=N:
            last = len(seq)-1
            first = last
            for i in range(len(seq)-2,-1,-1):
                if(seq[i]==seq[last]): 
                    first = i
                    break
            seq.append(last-first)
        print(seq.count(seq[n-1]))
        