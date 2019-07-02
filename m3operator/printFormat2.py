a=12345

print("/"+format(a,'>9d')+"/")
print("/"+format(a,'<9d')+"/")
print("/"+format(a,'^9d')+"/")
print("/"+format(a,'*^9d')+"/")
print("/"+format(a,'*>9d')+"/")
print("/"+format(a,'*<9d')+"/")
print("/"+format(a,'+^9d')+"/")
print("/"+format(a,'<b')+"/")
print("/"+format(a,'E')+"/")
print("/"+format(a,'o')+"/")
print("/"+format(a,'#X')+"/")

a=12345.678
# add comma to the thousand digit
print("/"+format(a,'*^12,.1f')+"/")

a='python'
print("/"+format(a,'*^10s')+"/")
print("/"+format(a,'*>10s')+"/")
print("/"+format(a,'*<10s')+"/")

