# myGlossary_Start.py
# A quick glossary app using a dictionary data type

from tkinter import *

# key press function:

def change_text():
    second_text.delete('1.0',END)
    definition = first_text.get().lower()
    if definition not in my_glossary:
        second_text.insert(INSERT, "Word not found.")
    else:
        second_text.insert(INSERT, my_glossary[definition])

##### main:
window = Tk()
window.title("My Coding Club Glossary")

# create label
my_label = Label (window, width = 100, height = 1, text = "Enter the word you want defining:")
my_label.grid(row = 0, column = 0, sticky=W)

# create text entry box
first_text = Entry (window, width = 100, background='light green')
first_text.grid(row = 1, column = 0)

# Add a submit button:
my_button = Button (window, text = 'Submit', width = 100, command = change_text)
my_button.grid(row = 2,column = 0, sticky=W)

# create another label
second_label = Label (window, text = "Definition:")
second_label.grid (row = 4, column = 0, sticky = W)


# create text box
second_text = Text (window, width = 100, background='light green')
second_text.grid(row = 5, column = 0)

# The dictionary:
my_glossary = {
    'algorithm': 'Step by step instructions to perform a task that a computer could understand.',
    'argument': 'A piece of information that is required by a function so that it can perform its task. Usually a string or number. my_function(arguments go here)',
    'binary number': 'A number represented in base 2.',
    'bug': 'A piece of code that is causing a program to fail to run properly or at all.',
    'casting': 'The process of converting one data-type into another. For example, sometimes a number may stored as text but need to be converted in to an integer. This can be done like this: int("3")',
    'commenting': 'Some text in a computer program that is for the human reader and is ignored by the computer when running the program. In python all comments begin with a hash symbol #',
    'comparative operator': 'Sometimes called logic operators, they allow us to compare data in a program. They include == and >',
    'constant': 'A number that does not change. It is good practice to name constants in capitals e.g. SPEED_OF_LIGHT',
    'container': 'Container data types store groups or other data types which may include more containers; the containers used in Python Next Steps are tuples, lists and dictionaries',
    'data type': 'Different types of information stored by the computer, for example floats, integers, strings, tuples, lists and dictionaries.',
    'debugging': 'The process of finding bugs in a program.',
    'default': 'A value given to an argument or variable as a starting point.',
    'dictionary': 'An unordered container data type that can store values of other data types as key:value pairs.',
    'equals operator': 'The equals sign is used to assign a value to a variable in coding, for example n=2 assigns the value 2 to the variable n.',
    'escape': 'When characters that have certain meanings in Python are required in strings they have to be “escaped” so that the computer knows they do not have their usual meaning. This is done by putting a slash in front of them e.g. \\',
    'execute': 'Another word meaning run. To execute some code is to run it.',
    'float': 'A number data-type that can have a decimal value.',
    'frame': 'A tkinter widget that can contain groups of other widgets, used to help organise the layout of complicated user interfaces.',
    'for loop': 'A kind of loop that is useful for iterating through container data types.',
    'function': 'A reusable piece of code',
    'global variable': 'A variable that is usable anywhere in a program.',
    'GUI': 'Stands for Graphical User Interface. A window with buttons and text entry boxes is an example of a graphical user interface.',
    'hacking': 'Taking some previously written code and re-writing bits to make it do something different.',
    'IDE': 'Stands for Integrated Development Environment. IDLE is an example of one. They are special text editors with useful tools built in for programmers.',
    'IDLE': 'Stands for Integrated DeveLopment Environment. This is the IDE that comes with a normal Python 3 install.',
    'index': 'The number that references a value in a string, tuple or list. Each item in the container data type is indexed from 0 for the first item, 1 for the next etc.',
    'infinite loop': 'A piece of code that keeps running forever. This is usually a bad thing.',
    'integer': 'A number data-type that cannot have a decimal value and must be a whole number.',
    'interactive mode': 'This is when we use IDLE to try out snippets of code without saving them.',
    'key': 'The equivalent of an index in a string, tuple or list but for a dictionary. It is defined by the programmer and can, for example, be a string, integer or even a tuple in a key:value pair.',
    'list': 'An ordered container data type which can hold values of any type and can have elements added or removed. Like tuples each element is indexed from 0.',
    'local variable': 'A variable that is defined inside a function and is only usable inside that function.',
    'logical operator': 'See comparative operator.',
    'loop': 'a piece of code that keeps repeating until a certain condition is met.',
    'mathematical operator': 'An operator that performs some mathematical function on some numbers. e.g. multiplication or addition',
    'method': 'The name given to a function in a class.',
    'module': 'A saved python file whose functions can be used by another program.',
    'modulus': 'A mathematical operator that is used to return the remainder from a division calculation. e.g. 22%7 returns 1',
    'operator': 'A symbol that performs a simple function on some code such as multiplying two numbers or comparing them to see if they are equal. See also comparative operator and mathematical operator.',
    'ordered containers': 'Ordered containers are container data types where the values stored are indexed together with their position in the container, e.g. tuples and lists; a dictionary is an example of an unordered container.',
    'output': 'Data that is sent from a program to a screen or printer etc.',
    'parameter': 'Another word for argument.',
    'refactoring': 'The process of changing the structure of code so it less repetitive, more readable, easier to maintenance, etc.',
    'return': '1. The value a function will produce after it has been run. (It is also a Python keyword.)\n2. The "end of line" key on a keyboard, sometimes called the enter key.',
    'script mode': 'This is when we use IDLE to help us write code that we will save in a file.',
    'slice': 'The process of extracting sections of a string or container variable – sometimes called array slicing.',
    'statement': 'Used in this book to mean a snippet of code. Strictly speaking it is a piece of code that represents a command or action. e.g. a print statement',
    'string': 'Text data, which can be stored in a variable.',
    'syntax error': 'An error produced when a computer fails to run a program because it cannot recognise the format of the code supplied. e.g. a syntax error would be produced if a bracket had not been closed.',
    'tkinter': 'A package of classes that are often imported in to Python programs that give methods that are useful for producing windows, drawing images and producing animations.',
    'tuple': 'An ordered container data type whose values are indexed from 0. Its contents cannot be changed.',
    'value': 'Anything that can be stored in a variable such as the elements in a container data type.',
    'variable': 'A name that refers to a place in a computer’s memory where data is stored. More loosely, it can also be used to refer to that data.',
    'while loop': 'A kind of loop that repeats code while a comparative statement returns True.',
    'widget': 'An element of a GUI such as a button or text entry box.'
    }

##### Run mainloop
window.mainloop()
