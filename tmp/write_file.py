content = """Hello World
Python is a wonderful language
and not hard to learn at all!

You can use Python for many things!
I.e for data analysis.

Using UTF-8 you can even write special characters like æ,ø,å etc.
"""

fileHandler = open('text2.txt', 'w', encoding='UTF-8')

for line in content:
    fileHandler.write(line)


"""
Mode	Description
'w'	Open a text file for writing. If the file exists, the function will truncate all the contents as soon as you open it. If the file doesn't exist, the function creates a new file.
'a'	Open a text file for appending text. If the file exists, the function append contents at the end of the file.
'+'	Open a text file for updating (both reading & writing).
"""