def count_characters(input_string):
    # Initialize counters
    vowels = 0
    consonants = 0
    spaces = 0
    others = 0

    # Convert the string to lowercase to simplify checking
    input_string = input_string.lower()

    # Define vowels
    vowel_set = set("aeiou")

    # Iterate through each character in the string
    for char in input_string:
        if char in vowel_set:
            vowels += 1
        elif char.isalpha():  # Check if the character is a consonant
            consonants += 1
        elif char.isspace():  # Check if the character is a space
            spaces += 1
        else:  # Otherwise, it's an "other" character
            others += 1

    # Display the results
    print(f"Vowels: {vowels}")
    print(f"Consonants: {consonants}")
    print(f"Spaces: {spaces}")
    print(f"Other characters: {others}")

# Example usage
input_string = input("Enter a string: ")
count_characters(input_string)