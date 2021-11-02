
#create a new list that interwines these 3 lists:
list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [10, 20, 30, 40, 50, 60, 70]
list3 = [100, 200, 300, 400, 500, 600, 700]

#Use zip function to create a single interwoven list.
one_list = list(zip(list1, list2, list3))

#create a blank list
two_line, single_line = [], []

#Flatten the list with 3 lines:
for x in one_list:
    for y in x:
        two_line.append(y)

#Use a single line to flatten list.
[single_line.append(y) for x in one_list for y in x]

#print results
print(two_line)
print(single_line)

#In general, which way should be used as a best practice?