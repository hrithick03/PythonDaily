
def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def print_prime_range():
    start = int(input("Enter start of range: "))
    end = int(input("Enter end of range: "))
    
    print(f"Prime numbers between {start} and {end} are:")
    
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")

print_prime_range()