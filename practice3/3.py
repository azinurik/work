a=input()
res = []
for i in range(0, len(a), 3):
    if i=="*" or i=="-" or i=="+" or i==":":
        l,r=a.split(i)
        c=i
b=""
for i in l:
    if i=="one":
       i="1"
       b+=i
    elif i=="two":
        i="2"
        b+=i
    elif i=="thr":
        i="3"
        b+=i
    elif i=="fou":
        i="4"
        b+=i
    elif i=="fiv":
        i="5"
        b+=i
    elif i=="six":
        i="6"
        b+=i
    elif i=="sev":
        i="7"
        b+=i
    elif i=="eig":
        i="8"
        b+=i
    elif i=="nin":
        i="9"
        b+=i
    else:
        i="0"
        b+=i

