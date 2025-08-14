# In Python, lists allow us to store multiple items in a single variable. For example, if you need to store the ages of all the students in a class, you can do this task using a list.

# Lists are similar to arrays (dynamic arrays that allow us to store items of different data types) in other programming languages.
# Python lists are very flexible. We can also store data of different data types in a list
# List Characteristics
# In Python, lists are:

# Ordered - They maintain the order of elements.
# Mutable - Items can be changed after creation.
# Allow duplicates - They can contain duplicate values.
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