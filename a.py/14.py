a=int(input())
n=list(map(int,input().split()))
s={}
for i in n:
    if i in s:
        s[i]+=1
    else:
        s[i]=1
mx=0
d=n[0]
for i in n:
    if s[i]>mx:
        mx=s[i]
        d=i
    elif s[i] == mx and i < d:
        d = i
print(d)