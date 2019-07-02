a=123

print('%d' % a)
#no use for the repr() since 123 is a number rather than string
print('%r' % a)

#add % to the end of the number or string
print('%d%%' % a)

#add + to the number when it >0
print('%+d' % a)

#form 5 digits & fill empty with space
print('%5d' % a)

#form 5 digits & fill empty with 0
print('%05d' % a)

#the format won't change the value by cutting the digits
print('%2d' % a)

#'-'means 'lean left'
print('%-5d' % a)

# alter the number to hex
print('%x' % a)
# alter the number to hex (Capital)
print('%X' % a)

# alter the number to hex & show the hexa-format
print('%#x' % a)
print('%#X' % a)

# alter the number to oct
print('%o' % a)
print('%#o' % a)

a=12345.678
print('%f' % a)
print('%.2f' % a)
print('%10.2f' % a)
print('%-10.2f' % a)
print('%010.2f' % a)
print('%e' % a)
print('%E' % a)
print('%.2e' % a)
print('%10.2e' % a)
print('%-10.2e' % a)

a='python'
print('%s' % a)
print('%10s' % a)
print('%-10s' % a)
print('%s%%' % a)
print('%r' % a)
print('%10s%10s%10s' % (a, a, a))
print('%10s%10s%10s' % (a, 'Java', 'C++'))

a=-123
#no use for the + since current a <0
print('%+d' % a)