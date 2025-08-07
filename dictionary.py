a={'name':'salih','age':23,'phone':123}
print(a)
print(a['name'])
print(a.get('phone'))
a['name']='hello'
print(a)
for i in a:
    print(i)
for i in a:
    print(a[i])
for i,j in a.items():
    print(i,j)
print(len(a))
a['email']='dekwd'
print(a)
a.pop('email')
print(a)
del a['age']
print(a)
a.clear()
print(a)
# del a
# print(a)