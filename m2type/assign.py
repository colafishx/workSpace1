x=10
y=x
z=x+y
print(x,y,z)
print(id(x), id(y), id(z))

a,b,c=10,20,30
print(a,b,c)
print(id(a), id(b), id(c))
#when 2 variables were assigned w/ same value, they possess same id (!= location in memory)

a=b=c=10
print(a,b,c)
print(id(a), id(b), id(c))

import keyword
print(keyword.kwlist)