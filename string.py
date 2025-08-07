# string data typoe function and manipulation
#  "" or '' 
# multiline """ .... """
s="""hello
world
"""
print(s)
print(s[0])
print(len(s))  #to find length of string
print(s[2:9])
a=" python  "
print(a.strip()) # to remove leading space same like trim of js
print(a.lower())
print(a.upper())
b="hello world"
print(b.replace("w","v"))
print(a+b)

a="hello iam {} , i like {}"
print(a.format("salih","cars"))
