n=int(input())
d={}
for i in range(n):
    a=input().split()
    if a[0]=="set":
        d[a[1]]=a[2]
    else:
        key=a[1]
        print(d.get(key, f"KE: no key {key} found in the document"))