from temperature_module import to_fahrenheit, to_celsius, to_kelvin

def main():
    print("Temperature Conversion Program")
    print("1. Celsius → Fahrenheit")
    print("2. Fahrenheit → Celsius")
    print("3. Celsius → Kelvin")

    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        c = float(input("Enter temperature in Celsius: "))
        print(f"{c}°C = {to_fahrenheit(c):.2f}°F")

    elif choice == 2:
        f = float(input("Enter temperature in Fahrenheit: "))
        print(f"{f}°F = {to_celsius(f):.2f}°C")

    elif choice == 3:
        c = float(input("Enter temperature in Celsius: "))
        print(f"{c}°C = {to_kelvin(c):.2f}K")

    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()