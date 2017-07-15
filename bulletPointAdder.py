#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()
lines = text.split(sep='\n') # THis is a list of stings
# TODO: Separate lines and add stars.

#pyperclip.copy(text)
for item in range(len(lines)): # Number of items in list
    lines[item] = '* ' + lines[item]

print(lines)
