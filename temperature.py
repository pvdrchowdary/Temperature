def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

print("Temperature Conversion Program")
print("-------------------------------")

while True:
    print("\nChoose an option:")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    print("3. Exit")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        f = float(input("Enter the temperature in Fahrenheit: "))
        c = fahrenheit_to_celsius(f)
        print("Temperature in Celsius: {:.2f}°C".format(c))
    elif choice == '2':
        c = float(input("Enter the temperature in Celsius: "))
        f = celsius_to_fahrenheit(c)
        print("Temperature in Fahrenheit: {:.2f}°F".format(f))
    elif choice == '3':
        print("Exiting the program...")
        break
    else:
        print("Invalid choice! Please choose again.")
