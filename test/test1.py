#import this
a = ['a', 'b', 'c', 'd', 'e']
del a[0]
print(sorted(a, reverse=True))
for i in a:
    print(i)

a = [i**2 for i in range(1, 11)]

if 1 in a:
    print('V')
else:
    print("x")

print(a[0:3])
print(a)