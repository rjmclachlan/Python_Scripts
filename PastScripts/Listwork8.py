
y = [40, 50, 60]
x = [10, 20, 30]

# extend a list using the x[:0] don't understand it,
x = y+x
print(x)
#same as
x = [10, 20, 30]
x[:0]= y
print(x)

#same as
x = [10, 20, 30]
x += y
print(x)

#so what is the differnce betwen x=y+x, x[:0] = y, x += y
#what's the use case for each of these