a = 3
b = 5

# fizzbuzz redo
# in the rare chance I get asked to code this?
# Version 1
for i in range(1, 101):
    if i % (a * b) == 0:
        print('fizzbuzz')
    if i % 3 == 0:
        print('fizz')
    if i % 5 == 0:
        print('buzz')
    else:
        print(i)

# Version 2
for n in range(1, 101):
    print("Fizz"*(n % a == 0) + "Buzz"*(n % b == 0) or n)

# Version 1 seems clearer to explain.
# is Version 2 more python?  Is there a peformance difference?