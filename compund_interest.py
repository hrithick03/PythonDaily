def calculate_compound_interest(principal, rate, time):
   amount = principal * (pow((1 + rate / 100), time))
   compound_interest = amount - principal
   return compound_interest
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))
ci = calculate_compound_interest(principal, rate, time)
print(f"Compound Interest after {time} years is: {ci:.2f}")