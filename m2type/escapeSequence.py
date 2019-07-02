x= 'python is a ' \
   '"simple" language'
print(x)

x= 'python is a ' \
'"simple" language'
print(x)

x= 'python is a \'simple\' language'
print(x)

x= 'python is a \\simple\\ language'
print(x)

x= 'python is a \n simple language'
print(x)

# add space in order to form the partition in 4X
x= 'python\tis\ta\tsimple\tlanguage'
print(x)

# backspace & delete previous unit
x= 'python\bis\ba\bsimple\blanguage'
print(x)

# raw string: escape "ESCAPE"
x= 'python\n.txt'
print(x)
x= 'python\\n.txt'
print(x)
x= r'python\n.txt'
print(x)