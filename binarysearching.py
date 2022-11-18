import time

number = int(input("Amount of number that should be given in list:"))
list1 = []
for x in range(number):
    k = int(input())
    list1.append(k)
print(list1)

#midElement = (number+1)//2
#mid = midElement
start = time.time()
searchingElement = int(input("Enter the element for the searching:"))
found = False
begning =0
end = number-1
location = 0
while (begning <= end and not found):
    mid = (begning + end)//2
    if  searchingElement == list1[mid]:
        print("Search is successful")
        print("\n")
        location = mid
        print("position of the item is ",location)
        found = True
    elif searchingElement < list1[mid]:
        end = mid - 1
    else:
        begning = mid + 1
    
    
if found == False:
    print("Search is not successful")
endd = time.time()
print("Time taken for binary search :",endd - start) 