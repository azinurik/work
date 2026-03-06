def simple_generator(n):
    a=[]
    for i in range(n+1):
        a.append(i)
    a.reverse()
    for i in range(n+1):
        yield a[i]
        
n=int(input())
my_gen = simple_generator(n)
for i in my_gen:
        print(i)