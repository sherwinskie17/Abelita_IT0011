# Part (b): Using nested while loops
def pattern_b():
    rows = 5  # Number of rows in the pattern
    i = 1  # Initialize outer loop counter
    while i <= rows:
        # Print leading spaces
        j = 1
        while j < i:
            print(" ", end="")
            j += 1
        # Print numbers
        k = 1
        while k <= (2 * i - 1):
            print(i, end="")
            k += 1
        # Move to the next line
        print()
        i += 1

# Call the function
pattern_b()