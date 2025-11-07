def is_prime():
    num = int(input("Enter a number to check: "))
    if num < 2:
        print(f"{num} is not a prime number")
        return
        
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not a prime number")
            return
            
    print(f"{num} is a prime number")

is_prime()