
#flatten nested list,though not everything may be a list
#four ways

flatten_list = [[2,3,1],[1,3],[9],[7,9,0]]
flatten_mix_list = [[2,3,1],[1,3],9,[7,9,0]]
print(flatten_list)
new_list = []

for x in flatten_mix_list:
    if isinstance(x, list):
        for y in x:
            new_list.append(y)
    else:
        new_list.append(y)

print(new_list)

#another way to do it (if they are all lists inside the list)
def flatten(f_list):
    return [x for y in f_list for x in y]
print(flatten(flatten_list))

# onemore
a = [x for y in flatten_list for x in y]
print(a)

# I guess this work also
print(f"{[x for y in flatten_list for x in y]}")

#lastone (But I have not stuided itertools)
import itertools
print(list(itertools.chain(*flatten_list)))

