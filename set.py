a={'bmw','audi','benz'}
print(a)
for i in a:
    print(i)
print("audi" in a)
print(len(a))
a.add(20)
print(a)
a.update([100,True,'bugatti'])
print(a)
# a.remove(1028)
print(a)
a.discard(20399)
print(a)

# remove =we can only remove the values in set  if the value exist otherwise it throws error
# discard =if there is nor value doesnt throw error
b={5,2,'lamborghini'}
c=a.union(b)
print(c)
c.clear()
print(c)
# del c
# print(c)