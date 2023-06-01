import re

def has_sequential_letters(string):
    pattern = r'abcdefghijklmnopqrstuvwxyz'
    matches = re.finditer(r'(?i)[a-z]{3,}', string)
    
    span = [match.span() for match in matches]
    print(span)
    return True

# Example usage
string = "abcabcgh"
if has_sequential_letters(string):
    print("Sequential letters found in the string.")
else:
    print("No sequential letters found in the string.")

