print('{} is {} year(s) old!'.format('Mary', 35))
print('{0} is {1} year(s) old!'.format('Judy', 25))
print('{1} is {0} year(s) old!'.format(30, 'Tom'))
print('{name} is {age} year(s) old!'.format(name='Jack', age=15))
print('{name} is {age} year(s) old!'.format(age=60,name='Alfie'))
print('{0} is {age} year(s) old!'.format('Allen', age=40))

print('{} {} {}'.format(123,12345.678, 'python'))
print('{0} {1} {2}'.format(123,12345.678, 'python'))
print('{0:b} {1:<10.2f} {2}'.format(123,12345.678, 'python'))
print('{:#X} {:<10.2f} {:>10s}'.format(123,12345.678, 'python'))