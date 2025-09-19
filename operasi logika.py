a=False
c=not a

print('data a =',a)
print('data c =',c)

#OR
a=False
b=False
c= a or b

print(a,'OR',b,'=',c)

#And
a= False
b= False
c= a and b
print(a,'and',b,'=',c)

a= True
b= False
c= a and b
print(a,'and',b,'=',c)

a= True
b= True
c= a and b
print(a,'and',b,'=',c)

#Xor
a=False
b=False
c= a ^ b
print(a,'XOR',b,'=',c)

a=False
b=True
c= a ^ b
print(a,'XOR',b,'=',c)

a=True
b=True
c= a ^ b
print(a,'XOR',b,'=',c)