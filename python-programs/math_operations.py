def perform_operations (num1, num2, operation):

    result = None
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        # result = num1 / num2
        if num2 == 0:
            result = "cannot divide a number by zero"
        else:
            result = "you cannot divide a number zero"
    else:
        print(f"the operation: {operation} was not valid")

    return result


