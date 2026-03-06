n=int(input())
co=0
for i in range(1,n):
    if(n%i==0):
        co+=1
if co<3:
    print("YES")
else:
    print("NO")