#find the frequency of values in a list.

bowling_scores=[165,189,206,206,185,189,219,225,300,219]
bowling_scores.sort()

dictionary_values = {x:bowling_scores.count(x) for x in bowling_scores}
print(dictionary_values)


#another way
b = {}
for item in bowling_scores:
    b[item] = b.get(item, 0) + 1
print(b)

#3rd way
import collections
ctr = collections.Counter(bowling_scores)
print(ctr)

#4th way (right now this makes the most sense to me)
dict={}
for i in bowling_scores:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)

#test script to see what happens I just put stuff in.
list_test=[1,2,3,4,5]
dict2 = {}
for i in list_test:
    dict2[i]=i

print(dict2)