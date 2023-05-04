from art import logo
# from replit import clear
import click


# Add
def add(n1,n2):
    return n1 + n2

# Subtract
def subtract(n1,n2):
    return n1 - n2

# Multiply
def multiply(n1,n2):
    return n1 * n2

# Division
def divide(n1,n2):
    return n1 / n2

def clrscr():
    click.clear()
    
# Dicitonary of different operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# Evalulaion of numbers by performing operations chosen by user.
def evaluation(num1,num2,operation_selected):
    calculation_method = operations[operation_selected]
    answer = calculation_method(num1,num2)
    print(f"{num1} {operation_selected} {num2} = {answer}")
    return answer

# recusively calling to start new calculation.
def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    
    for operator in operations:
        print(operator)
        
    repeat = "y"
    while repeat == "y":
    
        operation_selected = input("\nChoose an operation: ")
        num2 = float(input("What's the second number?: "))
        answer = evaluation(num1,num2,operation_selected)
        repeat = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start new calculation or 'exit' to close the calculator.: ").lower()
        if repeat == "y":
            num1 = answer
        elif repeat == "exit":
            clrscr()
            return
        else:
            clrscr()
            calculator()
            

calculator()
        
            
        

   
        
        
