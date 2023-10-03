def mian():
    numbers = get_numbers()
    square_numbers(numbers)
    display_numbers(numbers)


def get_numbers():
    # Function to get a list of numbers
    numbers = []
    number = input("Enter a list of numbers separated by comma: ")
    number_list = number.split(",")

    for number in number_list:
        try:
            numbers.append(float(number))
        except ValueError:
            print(f"Skipping invalid input: {number}")
    return numbers


def square_numbers(numbers):
    # Function to square each number in list
    for i in range(len(numbers)):
        numbers[i] = numbers[i] ** 2


def display_numbers(numbers):
    # Function to display the square numbers
    print("Squared numbers: ")
    for number in numbers:
        print(number)


mian()