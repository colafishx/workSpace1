x= "Hello World"
print(x)

x= 'Hello World'
print(x)

x= 'python is a "simple" language'
print(x)

x= "python is a 'simple' language"
print(x)

x= 'python is a ' \
   '"simple" language'
print(x)

x= 'python is a ' \
'"simple" language'
print(x)

x= """python is a
"simple" language"""
print(x)

x= """python is a
    "simple" language"""
print(x)

x= '''python is a
'simple' language'''
print(x)
print(type(x))

x=int(input())

print('Insert an integer')
if x > 4:
   print(x,'> 4')
else:
   print('you must be kidding!')