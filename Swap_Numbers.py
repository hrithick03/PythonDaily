def swap_numbers(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b
def main():
    a, b = swap_numbers(80, 65)
    print("Swapped values: a =", a, ", b =", b)
if __name__ == "__main__":
    main()