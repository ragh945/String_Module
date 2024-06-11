def upper(x):
    cap=""
    for y in x:
        if ord(y) in range(65,91):
            cap+=y
        elif ord(y) in range(97,123):
            z=ord(y)
            k=z-32
            cap+=chr(k)
        else:
            cap+=y
    return cap

def lower(x):
    cap=""
    for y in x:
        if ord(y) in range(95,123):
            cap+=y
        elif ord(y) in range(65,91):
            z=ord(y)
            k=z+32
            cap+=chr(k)
        else:
            cap+=y
    return cap

def isupper(x):
    x1=False
    for y in x:
        if ord(y) in range(65,91):
            x1=True
    return x1

def islower(x):
    x1=False
    for y in x:
        if ord(y) in range(97,123):
            x1=True
    return x1

def isdigit(x):
    x1=True
    for y in x:
        if ord(y) not in range(48,58):
            x1=False
    return x1

def isalpha(x):
    x1=True
    for y in x:
        if ord(y) not in range(95,123) and ord(y) not in range(65,91):
            x1=False
    return x1
def isalnum(x):
    x1=True
    for y in x:
        if ord(y) not in range(95,123) and ord(y) not in range(65,91) and ord(y) not in range(48,58):
            x1=False
    return x1

def startswith(x2):
    x=input("Enter the string :")
    x1="False"
    for y in x:
        if y[0]==x2:
            x1=True
    return x1

def endswith(x2):
    x=input("Enter the string :")
    x1="False"
    for y in x:
        if y[-1]==x2:
            x1=True
    return x1

def split(x3):
    x=input("Enter the string :")
    begin=0
    list1=[]
    for y in range(len(x)):
        if x[y]==x3:
            list1.append(x[begin:y])
            begin=y+1
        elif y==len(x)-1:
            list1.append(x[begin:])
    return list1

def capitalize(x):
    cap=""
    for i in range(len(x)):
        if i<1:
            if ord(x[i]) in range(97,123):
                c=ord(x[i])
                k=c-32
                cap+=chr(k)
            elif ord(x[i]) in range(97,123) or ord(x[i]) in range(65,91) or ord(x[i]) in range(48,58) or ord(x[i]) in range(32,48) or ord(x[i]) in range(58,65):
                cap+=x[i]
        elif i>=1:
            if ord(x[i]) in range(65,91):
                c=ord(x[i])
                k=c+32
                cap+=chr(k)
            else:
                cap+=x[i]
        else:
            cap+=x[i]
    return cap

def title(a):
    s=""
    i=0
    for y in range(len(a)):
        ch=ord(a[y])
        if ch>64 and ch<91:
            s+=chr(ch+32)
        else:
            s+=chr(ch) 
    c=''
    for x in range(len(s)):
        if x==0:
            ch=ord(s[x])
            if ch>96 and ch<123:
                c+=chr(ch-32)
            else:
                c+=chr(ch)
        elif a[x-1]==' ':
            ch=ord(s[x])
            if ch>96 and ch<123:
                c+=chr(ch-32)
            else:
                c+=chr(ch)
        else:
            c+=s[x]
    return c

def swapcase(x):
    cap=""
    for y in x:
        if ord(y) in range(95,123):
            z=ord(y)
            k=z-32
            cap+=chr(k)
        elif ord(y) in range(65,91):
            z=ord(y)
            k=z+32
            cap+=chr(k)
    return cap
