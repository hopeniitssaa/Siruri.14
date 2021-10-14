s=str(input("Scrie un sir"))
s1=""
s2=""
s3=""

print("Sirul initial este ", s)


for i in s:
    if ((ord(i)>64) and (ord(i)<90)):
        a=chr(ord(i)+1)
        s1+=a
    else:
        s1+=i      

print("Primul sir este", s1)


s2=s1
for i in s:
    b=s2.replace(("Z"), ("A"))

print("Al doilea sir este", b) 


s3=b
for i in s:
    c=l3.replace(' ','-')

print("Al treilea sir este", c)