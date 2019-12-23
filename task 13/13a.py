t=int(input());a=[];c=[]
for i in range(t) :
    x=int(input())
    a.append(x)
for i in a :
    b=[]
    for j in range(i) :
        if j%3==0 or j%5==0 :
            b.append(j)
    c.append(b)
for i in c :
    print(sum(i))
