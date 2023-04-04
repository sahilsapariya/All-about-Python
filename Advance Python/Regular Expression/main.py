import re

# We will accept the only string which will have only uppercase 
# letters from starting and ending of string
# and have at least one character in string.
# only that string will be accepted.
pattern = re.compile("^[A-Z]+$")

# Search: It will find the match object 
# that matches from any where in the string.
print(pattern.search("Hello world"))  # None
print(pattern.search("HELLO WORLD"))  # None
print(pattern.search("HELLOWORLD"))   # returns Match object.


# find the string that have lowercase characters.
# no other characters.
pattern = re.compile("[a-z]+")

# Match:  If required search pattern appears
# from start of the string then it will return the 
# result. else it returns None.
print(pattern.match("Hello World"))   # None
print(pattern.match("hello world"))   # returns Match object
print(pattern.match("HELLOWORLD"))    # None

# Now search the string that starts from any thing
# but contains only spaces, uppercase and lowercase 
# characters. 
pattern = re.compile("^[a-zA-Z\s]+$")

print(pattern.search("Hello World"))  # returns match object.
print(pattern.search("HELLO WORLD"))  # returns Match object.
print(pattern.search("HELLOWORLD"))   # returns Match object.
print(pattern.search("HELLO8 WORLD")) # None



# Let's create a game that checks the 
# entered string is valid according to the condition.

# Conditions:
# 1. 3 lowercase letters
# 2. 3-5 digits
# 3. one symbol
# 4. up to two uppercase characters (optional)

# Solution:
# We are going to define function for it.
# which check the input string and then returns valid response.

def checkString(text):
  # *step 1: define the pattern code.
  pattern = re.compile("^[a-z]{3}[0-9]{3,5}[^a-zA-Z0-9]{1}[A-Z]{0,2}$")

  if pattern.search(text): return 1
  return 0

print(checkString("sah53!SA"))  # 0
print(checkString("shs513.AA"))  # 1
print(checkString("sHaH"))  # 0

# # game is completed.


# Now, check the length of the string is exactly 10
# no matters what input is.
pattern = re.compile("^.{10}$")
print(pattern.search("          "))   # true
print(pattern.search("0123456789"))   # true
print(pattern.search("abcdefghijk"))  # None
print(pattern.search("abc> <zyx."))   # true



# Now let's make email validating

pattern = re.compile("^[a-zA-Z0-9\.\-_]+@{1}[a-zA-Z]+\.{1}[a-zA-Z]{2,3}$")

print(pattern.search("sahilsapriay03@gmail.com"))     # valid
print(pattern.search("mail.mymail@gmail.com"))        # valid
print(pattern.search("my_mail.e-mail@yahoo.com"))     # valid
print(pattern.search("my_mail.e-mail@yahoo.travel"))  # Not valid because .travel 
                                                      # does not fit to 2 to 3 letters


# Write a code for checking the indian phone numbers.

my_text = """
This is a indian phone number: +91 7894631232
This is another number: +91 1593574658
"""
pattern = re.compile(r'\+91\s\d{10}\b')
matches = pattern.finditer(my_text)

for item in matches:
  span = item.span()
  print(my_text[span[0]:span[1]])

# output:
# +91 7894631232
# +91 1593574658