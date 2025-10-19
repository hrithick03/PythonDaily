def Leap_year_check(n):
    if (n%4==0 ):
        if(n%100==0):
           return (n%400==0)
        return True
    return False
print(Leap_year_check(2024))  # True
print(Leap_year_check(1900))  # False
print(Leap_year_check(2000))  # True
print(Leap_year_check(2023))  # False
