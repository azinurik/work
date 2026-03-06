def func(j):
    c=0
    for i in range(len(j)):
        s=int(j[i])
        if s%2!=0:
            c+=1
    if c>0:
        return "Not valid"
    else:
       return "Valid"
j=input()
print(func(j))

