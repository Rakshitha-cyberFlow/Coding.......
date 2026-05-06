#adding bullet points to wiki text...

import pyperclip
text = pyperclip.paste()
text = '* ' + text.replace('\n','\n*')
pyperclip.copy(text)
print(text)
