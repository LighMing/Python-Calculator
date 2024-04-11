import re
def safe_float_convert(number_string):
    # Remove spaces and check for numbers or negative numbers
    number_string = number_string.strip()
    if number_string.replace('.', '', 1).replace('-', '', 1).isdigit() and number_string.count('.') < 2:
        return float(number_string)
    else:
        print("Can not identify the numbers")
        return None

def calculate(expression):
    # Split the expression and initialize the result
    numbers = re.split('([-+*/])', expression)
    result = safe_float_convert(numbers[0])


    for i in range(1, len(numbers), 2):
        equation = numbers[i]
        num = safe_float_convert(numbers[i + 1])
        if equation == '+':
            result += num
        elif equation == '-':
            result -= num
        elif equation == '*':
            result *= num
        elif equation == '/':
            if num == 0:
                print("Error: the divisor cannot be 0")
                return None
            result /= num
        else:
            print("Can not identify the numbers")
            return None
        return result


# User input
user_input = input("Please enter the equation: ")
result = calculate(user_input)
if result is not None:
    print("the answer is:", result)

