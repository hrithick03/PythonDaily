def print_table(n, upto=10):
    for i in range(1, upto + 1):
        print(f"{n} x {i} = {n * i}")
number = int(input("Enter a number: "))
print_table(number)
