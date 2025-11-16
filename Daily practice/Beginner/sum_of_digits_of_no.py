def sum_of_digit(n):
    sum=0
    while (n!=0):
        rem=n%10
        n=n//10
        sum=sum+rem
    return sum
print(sum_of_digit(1238798))