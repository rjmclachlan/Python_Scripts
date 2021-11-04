import datetime

a = 3
b = 5

# fizzbuzz redo
# in the rare chance I get asked to code this?
# Version 1

range_list = [10, 100, 1_000, 10_000, 100_000, 1_000_000, 10_000_000, 100_000_000, 1_000_000_000]
data_v1, data_v2 = [] , []

for item in range_list:
    speed_one, speed_two = [], []
    ct1 = datetime.datetime.now()
    for i in range(1, item):
        if i % (a * b) == 0:
            speed_one.append('fizzbuzz')
        if i % 3 == 0:
            speed_one.append('fizz')
        if i % 5 == 0:
            speed_one.append('buzz')
        else:
            speed_one.append(i)
        ct2 = datetime.datetime.now()
    data_v1.append(ct2-ct1)


    for n in range(1, item):
        speed_two.append("Fizz" * (n % a == 0) + "Buzz" * (n % b == 0) or n)
        ct3 = datetime.datetime.now()
    data_v2.append(ct3-ct2)
print(item , "complete")

print(data_v1)
print(data_v2)

