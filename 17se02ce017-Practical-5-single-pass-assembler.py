#!/usr/bin/env python
# coding: utf-8

# In[8]:


i = open('17SE02CE017-exp5_input.txt', 'r').readlines() 
op = open('17SE02CE017-exp5_optab.txt', 'r').readlines() 
output=open('17SE02CE017-output5.txt', 'w')
optab = {}; 
l=[];
m=[];
n=[];
a=[];
opcode = [];
object_code=[]

for line in op:
    line=line.split() 
    optab.update({line[0]:line[1]}) 

for line in i:
    if 'START' in line: 
        start=line.split()[2]
        x=int(start, 16)
        a.append('')
    else: 
        a.append(str(hex(x)[2:]))
        x+=3
for line in i:
    line = line.split()
    if len(line) == 3:
        l.append(line [0])
        m.append(line[1])
        n.append(line[2])
    elif len(line)==2:
        l.append('') 
        m.append(line[0])
        n.append(line[1])
    else:
        m.append(line[0])
for i in m:
    if i == 'START':
        continue 
    if i in optab:
        x = str(optab[i])
        y = str(a[l.index(n[m.index(i)])])
        object_code.append('^' + str(x + y))
ob=''.join(object_code)
leng=len(object_code) 
x =str(hex(leng*3)[1:])
if 'x' in x:
    x =x.replace('x', '0')

output.write('H^' + l[0] + '^' + a[1] + '^' + a[len(a)-1][2:]+ '\n')
output.write('T^' + a[1] + '^' + x + ob + '\n') 
output.write('E^' + '00' + a[1]+ '\n')
output.close()


# In[ ]:




