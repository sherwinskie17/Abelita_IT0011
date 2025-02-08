# Part (a): Using nested for loops
def pattern_a():
    rows = 5  # Number of rows in the pattern
    for i in range(1, rows + 1):  # Outer loop for rows
        # Print leading spaces
        for j in range(rows - i):
            print(" ", end="")
        # Print numbers
        for k in range(1, i + 1):
            print(k, end="")
        # Move to the next line
        print()

# Call the function
pattern_a()