import string  # Import the string module for predefined character sets


def caesar(text, shift, alphabets):
    # Function to shift the characters in the alphabet by the given shift value

    def shift_alphabets(alphabet):
        # String Manipulation: Shift characters in the alphabet
        # Slicing the alphabet into two parts and swapping them to create a shifted version
        shifted = alphabet[shift:] + alphabet[:shift]
        return shifted

    # Tuples and Lists: Apply the shift function to each alphabet in the list
    # Map each alphabet in the 'alphabets' list to its shifted version
    shifted_alphabets = tuple(map(shift_alphabets, alphabets))

    # String Manipulation: Combine all alphabets into a single string
    # Join the list of alphabets into a single string that represents the full set of characters
    final_alphabet = ''.join(alphabets)

    # String Manipulation: Combine all shifted alphabets into a single string
    # Join the list of shifted alphabets into a single string
    final_shifted_alphabet = ''.join(shifted_alphabets)

    # String Translation: Create a translation table
    # str.maketrans creates a mapping table from original alphabet to shifted alphabet
    table = str.maketrans(final_alphabet, final_shifted_alphabet)

    # String Translation: Apply the translation table to the input text
    # text.translate(table) uses the table to replace characters in the text
    return text.translate(table)


# Sample text to be encrypted
plain_text = "This is Mr.smart. Hello again!"

# Define alphabets used in the translation
# List of character sets that include lowercase, uppercase letters, punctuation, and whitespace
alphabets = [
    string.ascii_lowercase,  # Lowercase letters (e.g., 'abcdefghijklmnopqrstuvwxyz')
    string.ascii_uppercase,  # Uppercase letters (e.g., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    string.punctuation,  # Punctuation characters (e.g., '.,;:!?')
    string.whitespace  # Whitespace characters (e.g., space, tab, newline)
]

# Function call: Perform Caesar cipher encryption with a shift of 3
# Encrypt the plain_text using the Caesar cipher with a shift of 3
print(caesar(plain_text, 3, alphabets))
