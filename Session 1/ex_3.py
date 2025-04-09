def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


print("Welcome to the temperature converter!")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
choice = input("Please select an option (1/2): ")
if choice == "1":
    celsius = float(input("Please enter the temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is equal to {fahrenheit}°F")
elif choice == "2":
    fahrenheit = float(input("Please enter the temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F is equal to {celsius}°C")
else:
    print("Invalid choice. Please select 1 or 2.")
