import math
def lcm(n):
    ans = 1
    for i in range(1,n+1):
        ans=(ans*i)//math.gcd(ans,i)
    return ans
a=[]
t=int(input())
for i in range(t) :
    x=int(input())
    a.append(x)
for j in a :
    print(lcm(j))
