
number_lst = [1,2,3,4,5,6,7,8,9,10]
number_lst.sort()
first=0
last=len(number_lst)-1
mid = (first+last)//2
item = int(input("Enter the number to be search:  "))
found = False

while (first <= last and not found):
    mid = (first + last) // 2
    if number_lst[mid] == item:
        print(f"found at location {mid}")
        found = True
    else:
        if item < number_lst[mid]:
            last = mid - 1
        else:
            first = mid + 1

if found == False:
    print("Number not found")


