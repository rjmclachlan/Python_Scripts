#from @MikeDriscoll
names = {"Mike", "Pinky", "Brain", "Dot"}
other = {"Brain", "Yakko", "Wakko", "Rita"}
print(names-other)
#only 'Brain' is removed because that is the other thing matching.

#another pop quick from #MikeDriscoll.  he links to a webpage that explains sets.
#it took a while to understand
names = {"Mike", "Pinky", "Brain", "Dot"}
other = {"Brain", "Yakko", "Wakko", "Rita"}
print(names | other)
print(names ^ other)
print((names | other) - (names ^ other))

#True is considered 1 in this case
print((lambda a,b : a*b)(5,4)-True)


#create a new list that interwines these 3 lists:
list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [10, 20, 30, 40, 50, 60, 70]
list3 = [100, 200, 300, 400, 500, 600, 700]

merge=[]
#this code only works in the lists are the same size.  need to think about if different sizes
#add error codes.  Probably try and except code.
get_lengthes = len(list1), len(list2), len(list3)
limit = max(get_lengthes)
print(limit)
for i in range(0,limit):
    merge.append(list1[i])
    merge.append(list2[i])
    merge.append(list3[i])

print(merge)