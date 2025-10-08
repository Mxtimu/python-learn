# weight converter program
# formula : 1 pound = 0,453592 kilograms
# so to get kg = 1 lb(pound)* 0,453592
# formula : 1 kg = 2.20462 pounds
#so to get 1lbs = 1kgs * 2.20462

weight  = float(input("What is your weight? "))
unit = input("Kilograms or Pounds?  (K or L):")

if unit == "K" or "k" or "kg":
    final_weight = weight * 2.205
    unit = "Lbs."
    print(f"You weight is: {round(final_weight, 1)} {unit}")
elif unit == "L":
    final_weight = weight / 2.205
    unit = "kgs."
    print(f"Your weight is: {round(final_weight, 1)} {unit}")
else:
    print(f"{unit} was not valid...")



