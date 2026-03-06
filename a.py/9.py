a=int(input())
n=list(map(int,input().split()))
min=min(n)
max=max(n)
for c in n:
    if c==max:
        c=min
        print(c,end=" ")
    else:
        print(c,end=" ")
    