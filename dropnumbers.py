# Write a Python program to print the first n Lucky Numbers. Go to the editor
# Lucky numbers are defined via a sieve as follows.
# Begin with a list of integers starting with 1 :
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 39,
           30]
x = len(my_list)
count = 1
while x > 10:
    for i in my_list:
        try:
            my_list.pop(i + 2)
        except IndexError:
            x = len(my_list)

print(my_list)
