def Largest_Number(n):
    max=0
    while n!=0:
        r=n%10
        n=n//10
        if r>max:
            max=r
    return(max)

print(Largest_Number(125978))