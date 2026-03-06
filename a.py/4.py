a=int(input())
n=list(map(int,input().split()))
sum=0
for c in n:
    if c>0:
        sum+=1
print(sum)