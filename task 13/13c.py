t=int(input());a=[];c=[]
for i in range(t) :
    x=int(input())
    a.append(x)
for i in a :
    b=[]
    for j in range(1,i+1) :
        if i%j==0 :
            b.append(j)
    c.append(b)            