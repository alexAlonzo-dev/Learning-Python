programming_dictionary = {
    "Algorithm": "A set of defined steps or instructions to solve a problem or perform a task.",
    "Variable": "A named space in memory used to store data that can change during program execution.",
    "Function": "A reusable block of code that performs a specific task and may take inputs and return a result.",
    "Conditional": "A control structure that executes different blocks of code depending on whether a condition is true or false.",
    "Loop": "A structure that repeats a block of code while a certain condition is met (e.g., for or while).",
    "Class": "A blueprint for creating objects in object-oriented programming, encapsulating data and behavior.",
    "Object": "An instance of a class that represents an entity with attributes (data) and methods (behavior).",
    "Debugging": "The process of identifying and fixing errors or bugs in the code.",
    "Compiler": "A program that translates source code written in a high-level language into machine code.",
    "Framework": "A set of tools and libraries that simplifies application development by providing structure and conventions.",
    "API": "Application Programming Interface, a set of functions and protocols for building and interacting with software applications.",
    "Database": "An organized system for storing, managing, and retrieving data efficiently.",
    "Recursion": "A programming technique where a function calls itself to solve a problem in smaller parts.",
    "Git": "A distributed version control system that tracks changes in source code during development.",
    "Deprecated": "A code element that still works but is no longer recommended for use and may be removed in the future."
}

#Getting values from dictionary
print(programming_dictionary.get("Algorithm"))
print(programming_dictionary["API"])

#ADDING VALUes
programming_dictionary[1] = "This is an integer"
print(programming_dictionary[1])

#To delete a dictionary only set to an empty dictionariy
# programming_dictionary = {}

#Edit an item in a dictionary
programming_dictionary[1] = "This number is an integer, maybe your favorite number"

#Next will print only keys
for some in programming_dictionary:
    print(some)

#Next will print keys and values
for key in programming_dictionary:
    print(f"Keys: {key} -> Value: {programming_dictionary[key]}")