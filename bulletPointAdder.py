#! python3
# adding bullet points to text in a clipboard
import pyperclip
text = pyperclip.paste()
lines = text.split('\n')
for i in range(0, len(lines)):
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines)
pyperclip.copy(text)