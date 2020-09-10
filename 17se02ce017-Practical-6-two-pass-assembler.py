#!/usr/bin/env python
# coding: utf-8

# In[17]:


file=open("17SE02CE017-exp6_input.txt","r")
cont=file.readlines()
file.close()
opt={}
for j in cont:
    s=j[:-1].split (' ')
    opt(s[0])=s[1]
file=open("17SE02CE017-exp6_optab.txt","r")
cont=file.readlines()
file.close()
u=0
d={}
for j in cont:
    d[u]=j[:-1].split('')
    u=u+1
for p in d:
    v=' '.joint(d[p])
    print(v)
start=1000
locctr=0
print ("")
key ["RESW", "RESB", "BYTE","WORD" ]
if d[0][1] == 'START':
    locctr=1000
    start=1000
else:
    locctr=0
    start=0
var={}
inter=[]
name=d[0][0]
r=0
for j in range (l,u):
    if (d[j][0]==""):
        if(d[j][1]=="END"):
            break
        if(d[j][1] in opt):
            locctr=locctr+3
    if (d[j][0]!=" "):
        r=r+1
        if (d[j][1]=="RESW"):
            locctr=locctr+3*int(d[j][2])
        elif(d[j][1]=="RESB"):
            locctr=locctr+int(d[j][2])
        elif(d[j][1]=="WORD"):
            locctr=locctr+3
        elif(d[j][1]=="BYTE"):
            locctr=locctr+len(d[j][2])
        var[d[j][0]]=locctr
    inter.append(locctr)
    print(d[j][1],locctr)
print(" ")
size=hex(locctr-start)[2:].upper()
if(len(size)==1) :
    size="0"+size
u=u-1
st=""
for j in range (1,u-r):
    k=""
    if(d[j][1] in opt):
        k=opt[d[j][1]]
    else:
        k="00"
    if(d[j][2] in var):
        f=hex(var(d[j][1]-start)[2:].upper()
        if(len(f)==1):
            f="l"+"O" (3-len(f))+f
        k=k+f
    else:
        k=k+"0"*4
    st=st+k+"^"
st=st[:-1]
print("H^"+name+"^OO"+str(start) +"^"+size)
size=hex((u-r-1)*3)[2:].upper()
if(len(size)==1):
    size="0"+size
print("T^"+str(start)+"^" +size+"^"+st)
print("E^00"+str(start))
        


# In[ ]:




