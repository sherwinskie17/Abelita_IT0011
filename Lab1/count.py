def sum_of_digits(input_string):
    # Initialize a variable to store the sum
    total_sum = 0

    # Iterate through each character in the string
    for char in input_string:
        if char.isdigit():  # Check if the character is a digit
            total_sum += int(char)  # Convert the character to an integer and add it to the sum

    # Display the result
    print(f"Sum of digits: {total_sum}")

# Example usage
input_string = input("Enter a string with digits: ")
sum_of_digits(input_string)