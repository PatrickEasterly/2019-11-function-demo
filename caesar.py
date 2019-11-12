
# convert a letter
def convert_letter(letter, rotate_by=13):
    # rotate_by is an optional argument.

    # 1. Setup/configuration
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    
    # 2. Work
    position = alphabet.index(letter)
    new_position = (position + rotate_by) % 26
    new_letter = alphabet[new_position]

    # 3. Result
    return new_letter

the_new_letter = convert_letter("a")
# the_new_letter = "n"
print(the_new_letter)
# convert_letter("a", 15)