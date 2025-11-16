import math
def find_gcd_lcm(a, b):
    gcd = math.gcd(a, b)             
    lcm = (a * b) // gcd              
    return gcd, lcm
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
gcd, lcm = find_gcd_lcm(num1, num2)
print(f"GCD (HCF) of {num1} and {num2} is: {gcd}")
print(f"LCM of {num1} and {num2} is: {lcm}")
