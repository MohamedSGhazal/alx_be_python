global FAHRENHEIT_TO_CELSIUS_FACTOR
FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)

global CELSIUS_TO_FAHRENHEIT_FACTOR
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)

global FREEZING_POINT_DIFFERENCE
FREEZING_POINT_DIFFERENCE = 32

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temperature = int(input("Enter the temperature to convert: "))
temperature_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().lower()

if temperature_type == "c":
    print(f"{temperature}°C is {convert_to_fahrenheit(temperature)}°F") 
elif temperature_type == "f":
    print(f"{temperature}°F is {convert_to_celsius(temperature)}°C")
else:
    print(f"Invalid temperature. Please enter a numeric value.")