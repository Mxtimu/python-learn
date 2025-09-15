# calculator using if statements

num1 = float(input("What Number would you like to select? "))
operator = input("what operator would you like to use? ")
num2 = float(input("What Number would you like to select? "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))

elif operator == "-":
    result = num1 - num2
    print(round(result, 3))

elif operator == "/":
    result = num1 / num2
    print(round(result, 3))

elif operator == "*":
    result = num1 * num2
    print(round(result, 3))

else:
    print(f"you did not enter anything in num1 or num2 or you are missing an operator")