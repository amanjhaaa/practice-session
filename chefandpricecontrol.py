T = int(input())
if not (T>=1 and T<=100):
    raise ValueError("Test case did not meet constraint.")
    
for j in range(0,T):
    N = str(input())
    itemlist = input()
    temp = N.split(" ")
    N = int(temp[0])
    K = int(temp[1])
    if not (K>=1 and K<=1000):
        raise ValueError("Ceiling Price did not meet constraint.")
    itemlist = itemlist.split(" ")
    pricelist = []
    for i in itemlist:
        pricelist.append(int(i))
    if not (N>=1 and N<=10000):
        raise ValueError("items did not meet constraint.")
    loss = 0
    for i in pricelist:
        if not (i >=1 and i <=1000):
           raise ValueError("Ceiling Price did not meet constraint.")
        if i > K:
            loss = loss + (i - K)
    print(loss)
    

