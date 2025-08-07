a=['bugati','pagani','ferrari']

print(a)
print(a[0])
print(len(a))
print(a[1:3]) 
b=[10,20,30,40]
print(b[1]+b[3])
print(b[1],a[2])
a[0]='bugatti'
print(a)
for i in a:
    print(i)
a.append("lamborghini")
a.insert(0,'koenigsegg')
print(a)
a.remove('ferrari')
print(a)
a.clear()
print(a)
# del b
# print(b)