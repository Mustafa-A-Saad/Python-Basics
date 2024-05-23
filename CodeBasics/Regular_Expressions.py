#Semi Regular Expressions
def isPhoneNumber(text):
    if len(text) != 12:
        return False

    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != "-":
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != "-":
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)): # start from 0
    chunk = message[i:i + 12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)

# Regex = Regular Expressions ( instead of above )
import re # Regex Modulue
# \d = a digit character (0-9)
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}') # r'' is a raw string which ignores escape functions and prints the blacklash
#print(phoneNumRegex) # regex object
mo = phoneNumRegex.search("My number is 415-555-4242.") # if a pattern is found the sreach function returns a Match object which can use the .group()
print("Phone number found "+ mo.group()) # .group return the actual matched text from the searched string.


# Steps to create Regular Expressions( Regex )
# 1. Import the regex module with import re.
# 2. Create a Regex object with the re.compile() function. (Remember to use a raw string.)
# 3. Pass the string you want to search into the Regex object’s search() method.
# This returns a Match object.
# 4. Call the Match object’s group() method to return a string of the actual
# matched text.

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') # the ( ) puts them in groups
mo = phoneNumRegex.search('My number is 415-555-4242.')
print(mo.group(1))
print(mo.group(2))
print(mo.group()) # = to group(0)
print(mo.groups()) # in plural form , puts them in tuples value
areaCode , Number = mo.groups() #
print(areaCode)

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)') # the \( includes the parenthesis ( )
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
print(mo.group(1))
print(mo.group(2))

#Pipe
heroRegex = re.compile(r'Batman|SuperMan') # it searchs for either one of them
mo = heroRegex.search("Batman is better than SuperMan")
print(mo.group()) # prints the first one occur

batRegex = re.compile(r'Bat(mobile|man|bat)') # search for Bat as a prefix
mo = batRegex.search("The Batmobile lost its wheel")
print(mo.group())
print(mo.group(1)) # matches only the thing inside the parenthesis

batRegex = re.compile(r'Bat(wo)?man') # regex should find a match whether or not that bit of text is there whatever inside the ()?
mo = batRegex.search("Batman is my fav")
print(mo.group())

mo = batRegex.search("Batwoman my fav")
print(mo.group())