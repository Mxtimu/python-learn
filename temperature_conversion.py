# this is a temperature conversion program

temperature_number = int(input("What is the current temperature (number only) "))
temperature_unit = input("Celsius or Fahrenheit (C or F): ")

if temperature_unit == "C":
    temperature_conversion = round(int((temperature_number * 9/5) + 32), 1)
    new_temperature_unit = "F"
    print(f"The temperature is {temperature_conversion} {new_temperature_unit}")

elif temperature_unit == "F":
    temperature_conversion = round(int((temperature_number - 32)* 5/9), 1)
    new_temperature_conversion = "C"
    print(f"The temperature is {temperature_conversion} {new_temperature_conversion}")
else:
    print("You did not enter the correct symbol")