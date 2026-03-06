a=int(input())
n=list(map(int,input().split()))
n.sort(reverse=True)
for c in n:
    print(c,end=" ")