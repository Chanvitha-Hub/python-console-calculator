def calculate(operands, operators):
    result = operands[0]
    for i in range(1, len(operands)):
        if operators[i - 1] == '+':
            result += operands[i]
        elif operators[i - 1] == '-':
            result -= operands[i]
        elif operators[i - 1] == '*':
            result *= operands[i]
        elif operators[i - 1] == '/':
            result /= operands[i]
    return result


def validate_operator(operator):
    return operator in ['+', '-', '*', '/']


def validate_number(number):
    try:
        float(number)
        return True
    except ValueError:
        return False


def get_input(num_operands, num_operators):
    operands = []
    operators = []
    for i in range(num_operands):
        operand = input(f"Enter operand {i + 1}: ")
        if not validate_number(operand):
            return [], []
        operands.append(float(operand))

    for i in range(num_operators):
        operator = input(f"Enter operator {i + 1} (+, -, *, /): ")
        if not validate_operator(operator):
            return [], []
        operators.append(operator)

    return operands, operators


def print_commands():
    print("\nCalculator commands:\n")
    print("+ : Addition")
    print("- : Subtraction")
    print("* : Multiplication")
    print("/ : Division")
    print("q : Quit the calculator")


def main():
    print_commands()

    while True:
        try:
            num_operands = int(input("\nEnter the number of operands: "))
            num_operators = num_operands - 1
            # print("\n")
            operands, operators = get_input(num_operands, num_operators)

            if not operands or not operators:
                print("Invalid input. Please try again.")
                continue

            result = calculate(operands, operators)
            print("\nResult: ", result)

        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
        except Exception as e:
            print("An error occurred:", str(e))

        print("-----")

        option = input("Press Enter to continue or 'q' to quit: ")
        if option == 'q':
            print("Exiting the calculator.")
            break
        else:
            # print("\n" * 100)  # Clear the previous output
            pass





if __name__ == "__main__":
    main()
