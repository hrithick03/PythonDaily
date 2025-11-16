def fahrenheit_to_celsius(fahrenheit):
    return round((fahrenheit - 32) * 5 / 9, 2)

def celsius_to_fahrenheit(celsius):
    return round((celsius * 9 / 5) + 32, 2)

def convert_temperature(value, scale):
    if scale.lower() == 'f':
        celsius = fahrenheit_to_celsius(value)
        print(f"{value}°F is {celsius}°C")
    elif scale.lower() == 'c':
        fahrenheit = celsius_to_fahrenheit(value)
        print(f"{value}°C is {fahrenheit}°F")
    else:
        print("Invalid scale. Use 'C' for Celsius or 'F' for Fahrenheit.")

convert_temperature(100, 'F') 
convert_temperature(37.78, 'C')  
