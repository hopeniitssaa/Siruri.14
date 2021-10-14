s="A B C D E F H I J K L M N O P" 
s1=""
s2=""
s3=""
for i in s:
        a=chr(ord(i)+1)
        s1+=a
        b=s1.replace('!', ' ')
        x=b.replace('[', 'A')
print('Primul sir este', x)
