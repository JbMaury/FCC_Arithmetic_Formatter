def arithmetic_arranger(problems, result=True):

    # Managing errors
    error_message = has_error(problems)
    if error_message:
        print(error_message)
        return None

    first_line = []
    second_line = []
    third_line = []
    fourth_line = []

    for problem in problems:

        elements = problem.split()

        # Getting the size of the box (2+ for the operand and one  space)
        size = 2 + max(int(len(elements[0])), int(len(elements[2])))

        # Operands and result are right-aligned with space fillers
        first_operand = f"{' ' * (size-len(elements[0]))}{elements[0]}"
        second_operand = f"{elements[1]}{' ' * (size - len(elements[2]) - 1)}{elements[2]}"
        separator = f"{'-'*size}"

        # Result needed only if result parameter is given
        if result:
            num1 = int(elements[0])
            num2 = int(elements[2])
            result = num1 + num2 if elements[1] == '+' else num1 - num2
            printed_result = f"{' ' * ( size-len(str(result)))}{str(result)}"
            fourth_line.append(printed_result)

        first_line.append(first_operand)
        second_line.append(second_operand)
        third_line.append(separator)

    # Final string with added lines when the loop on each problem is over
    arranged_problems = (' '*4).join(first_line)+'\n' +\
                        (' '*4).join(second_line)+'\n' + \
                        (' '*4).join(third_line)

    # The fourth line is only added if result parameter is provided
    if result:
        arranged_problems += '\n'+(' '*4).join(fourth_line)

    print(arranged_problems)

    return arranged_problems


def has_error(problems):
    # Limit of 5 problems
    if len(problems) > 5:
        return "Error: Too many problems."
    for problem in problems:
        elements = problem.split()
        # Only addition and subtraction
        if elements[1] not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."
        # Operand can only have digits
        if not elements[0].isdigit() or not elements[2].isdigit():
            return "Error: Numbers must only contain digits."
        # No more than 4 digits per operand
        if len(elements[0]) > 4 or len(elements[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
    return False


