def sum_even_numbers():
    input_str = input("Enter numbers separated by spaces: ")
    numbers = [int(x) for x in input_str.split()]
    
    even_sum = sum(num for num in numbers if num % 2 == 0)
    
    print(f"Sum of even numbers: {even_sum}")

sum_even_numbers()