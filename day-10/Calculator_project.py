def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2




operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}
print(r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
""")



process = False
while not process:
    f_number = int(input("What's the first number?: "))
    choose_operation = input("+\n-\n*\n/\nPick an operation:")
    s_number = int(input("What's the next number?: "))
    operation = operations[choose_operation]
    result = operation(f_number, s_number)
    print(f"{f_number} {choose_operation} {s_number} = {result}")
    process = True
    while process:
        calculation = input(f"Type 'y to continue calculating with {result} , or type 'n' to start a new calculation:")
        if calculation == "y":
            process = True
            f_number = result
            choose_operation = input("+\n-\n*\n/\nPick an operation:")
            s_number = int(input("What's the next number?: "))
            operation = operations[choose_operation]
            print(f"{f_number} {choose_operation} {s_number} = {operation(f_number, s_number)}")
            f_result = operation(f_number, s_number)
            f_number = f_result

        elif calculation == "n":
            process = False









