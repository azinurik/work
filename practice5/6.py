def simple_generator(n):
    a,b=0,1
    for i in range(n):
            yield a
            a,b=b,a+b
        
n=int(input())
my_gen = simple_generator(n)
for i in my_gen:
    if i!=0:
        print(",",end="")
    print(i,end="")
