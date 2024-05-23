import re
import pyperclip

phoneRegex = re.compile(r'''(
 (\d{3} | \(\d{3}\))? # area code (optional(?)), either 3 digits or enclosed in parentheses
 (\s | - | \.)?       # separator (optional), can be a space, hyphen, or period
 (\d{3})              # first 3 digits
 (\s|-|\.)            # separator, must be a space, hyphen, or period
 (\d{4})              # last 4 digits
 (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension (optional), can be 'ext', 'x', 'ext.', followed by 2 to 5 digits
 )''', re.VERBOSE)  # VERBOSE = ignoring whitespace and comments within the pattern inside the text.

EmailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+     # Username part of the email address # the + isn't for string concat , it allows for more than 1 match for a char
@[a-zA-Z0-9.-]+       # Domain name part of the email address
(\.[a-zA-Z]{2,4})     # Top-level domain part of the email address
)''', re.VERBOSE)

text = str(pyperclip.paste()) # it pastes the text that I have in my computer's clipboard (CTRL+C)

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])  # .join() concats all groups into 1 string ( groups here is like i ) not the function
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in EmailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches)) #.join(matches) = it takes each element of matches, joins them together using a newline character as the separator
                              #  and returns a single string containing all the elements separated by newline characters.
else:
    print("No Phone numbers or email adresses found")

print(matches)

# Text to try on
"""
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed commodo, veF
Aliquam erat volutpat. Cras venenatis, velit eget gravida tincidunt, estn
Email: example@email.com
Phone: +123-456-7890

Pellentesque habitant morbi tristique sen
Suspendisse potenti. Nulla facilisi. Ut tempu. Ve

Email: another@example.com
Phone: +987-654-3210

Nullam imperdiet elit nec urmi. Mauris aliquet blandit dolorortor p
Phone: +555-123-4567
Email: test@example.org

"""
