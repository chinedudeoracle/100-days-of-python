from art import logo

#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
}

def calculator():
    print(logo)

    num1 = float(input("What is the first number?: "))
    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        calculation_function = operations[operation_symbol]
        num2 = float(input("What is the next number?: "))
        answer = calculation_function(n1=num1, n2=num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ").lower() == "n":
            should_continue = False
            calculator()
        else:
            num1 = answer

calculator()