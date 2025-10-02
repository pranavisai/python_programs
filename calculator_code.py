from art import logo

print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations_dict = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    number1 = float(input("Please provide the first number:"))
    should_use_first = True

    while should_use_first:
        for i in operations_dict:
            print(i)
        operation = input("Pick an operation:")

        number2 = float(input("Please provide the second number:"))

        result = operations_dict[operation](number1, number2)

        print(result)
        answer = input("Do you want to use the result as the first number? Yes/No").lower()
        if answer == "yes":
            number1 = result
        else:
            should_use_first = False
            calculator()

calculator()









