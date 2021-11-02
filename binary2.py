
numberslist = [1,4,7,9,12,45,67,54,34,89,65,32]
numberslist.sort()
first=0
last=len(numberslist)-1
mid=(first+last)//2
item=int(input("Give me a number between 1 and 100:  "))
found=False

while (first <= last and not found):
    mid = (first + last) // 2
    if numberslist[mid] == item:
        print(f"Congrats you found it at location: {mid}")
        found = True
    else:
        if item < numberslist[mid]:
            last = mid - 1
        else:
            first = mid + 1

if found == False:
    print("Number not found")
