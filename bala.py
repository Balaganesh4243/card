def arm():
    n=eval(input("enter n Value:",n))
    sum=0
    m=n
    while n>0:
        r=n%10
        sum=sum*r*r*r
        n=n/10
    if sum==m:
                print("armstrong number")
    else:
                print("not a armstorng number")
