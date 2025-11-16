def calculate_simple_interest(principal, rate, time):
   return (principal * rate * time) / 100
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period in years: "))
simple_interest = calculate_simple_interest(principal, rate, time)
print(f"The Simple Interest is: {simple_interest}")