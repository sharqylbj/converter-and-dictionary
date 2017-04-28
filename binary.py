# function converting decimal to binary
def binary(decimal_exampl):
    decimal_exampl = int(decimal_exampl)
    binary_number = ""
    while decimal_exampl > 1:
        if decimal_exampl % 2 == 1:
            binary_number = "1" + binary_number
            decimal_exampl -= 1
        elif decimal_exampl % 2 == 0:
            binary_number = "0" + binary_number
        decimal_exampl /= 2
    if decimal_exampl == 1:
        binary_number = "1" + binary_number
    return binary_number


def decimal(binary_exampl):
    # defining a variable for computing
    decimal_number = 0
    binary_exampl = str(binary_exampl)
    # loop converts each digit in binary number, result is
    for digit in binary_exampl:
        decimal_number = decimal_number*2 + int(digit)
    return decimal_number

init_string = input("""Enter number you wish to convert,
followed by a space and 2 or 10, for current system:
""")
# creating a list of two elements - number and chosen system
numbers = init_string.split(' ')
print (numbers)

# converting from binary
if numbers[0].isdigit() is True and numbers[1] == "2":
    # creating integer variable from entered
    numbr = int(numbers[0])
    print (decimal(numbr))
# converting from decimal
elif numbers[0].isdigit() is True and numbers[1] == "10":
    # creating integer variable from entered
    numbr = numbers[0]
    print (binary(numbr))
