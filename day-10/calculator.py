def add(a,b):
    return a + b;

def subtract(a,b):
    return a - b;

def multiply(a,b):
    return a * b;

def divider(a,b):
    return a/ b;

operations = {
    "*": multiply,
    "+": add,
    "-": subtract,
    "/": divider
}
should_continue = True

fist_number = int(input("What's the first number?: "))
while should_continue:
    selected_operation = input('''
    +
    -
    *
    /
    Pick an operation: ''')
    second_number = int(input("What's the next number?: "))

    answer = operations[selected_operation](fist_number, second_number);
    print(f"{fist_number} {selected_operation} {second_number} = {answer}");
    continue_with_number = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ");
    if continue_with_number == 'y':
        fist_number = answer;
    else:
       should_continue = False  
       print("\n" * 20) 
 
