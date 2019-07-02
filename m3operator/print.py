print('Python', "C", 'Java')

#change seperator by ','
print('Python', "C", 'Java', sep=',')

#change end unit by '#', which disable auto-line
print('Python', "C", 'Java', sep=',', end='#')

a,b,c=123,123.45,'python'
print(a,b,c)

#change end unit by ' ', which disable auto-line but seperate two output w/ a space
print('Hello', end=' ')
print('world!')