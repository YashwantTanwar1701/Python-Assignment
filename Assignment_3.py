#!/usr/bin/env python
# coding: utf-8

# 1. Why are functions advantageous to have in your programs?
# 
# Functions are advantageous in Python programs for modularity, reusability, abstraction, and encapsulation. They allow you to break down a program into smaller, manageable components, making the code easier to understand, maintain, and debug. Functions promote code reuse, as you can call the same function multiple times from different parts of the program without duplicating code.

# 2. When does the code in a function run: when it's specified or when it's called?
# The code in a function runs when the function is called, not when it's specified. Defining a function merely creates a function object and binds it to a name. The actual execution of the function's code block occurs when the function is called with appropriate arguments.

# 3. What statement creates a function?
# The def statement is used to create a function in Python. It specifies the name of the function, followed by a parameter list (if any), and a colon. The indented block of code following the def statement defines the body of the function.

# 4. What is the difference between a function and a function call?
# A function is a block of code that performs a specific task when called. It is defined using the def statement. A function call is the act of executing the code inside a function. To call a function, you use the function's name followed by parentheses containing any required arguments.

# 5. How many global scopes are there in a Python program? How many local scopes?
# In a Python program, there is one global scope and multiple local scopes. Global variables are accessible throughout the entire program, while local variables are only accessible within the function or code block where they are defined.

# 6. What happens to variables in a local scope when the function call returns?
# In Python, variables defined in a local scope (inside a function) are destroyed when the function call returns. They are no longer accessible once the function completes its execution.

# 7. What is the concept of a return value? Is it possible to have a return value in an expression?
# The return value is the value that a function sends back to the caller after completing its task. It is specified using the return statement. A return value can be of any data type, and it is possible to use a return value in an expression.

# 8. If a function does not have a return statement, what is the return value of a call to that function?
#  If a function does not have a return statement, the return value of a call to that function is None. This is Python's way of indicating that the function did not explicitly return any value.

# 9. How do you make a function variable refer to the global variable?
# To make a function variable refer to a global variable, you can use the global keyword followed by the variable name inside the function. This tells Python to use the global variable instead of creating a new local variable with the same name.

# 10. What is the data type of None?
# The data type of None is NoneType. None represents the absence of a value or the lack of a return value from a function.

# 11. What does the sentence import areallyourpetsnamederic do?
# The statement import areallyourpetsnamederic imports a module named areallyourpetsnamederic into the current Python script or session. It allows you to access the functions, classes, and variables defined in the areallyourpetsnamederic module.

# 12. If you had a bacon() feature in a spam module, what would you call it after importing spam?
# If you had a bacon() function in a module named spam, you would call it after importing spam using the syntax: spam.bacon(). This syntax specifies the module name (spam) followed by the function name (bacon()), separated by a dot.

# 13. What can you do to save a programme from crashing if it encounters an error?
# To prevent a program from crashing if it encounters an error, you can use error handling techniques such as try and except blocks. By wrapping potentially error-prone code inside a try block and providing error-handling logic in the corresponding except block, you can gracefully handle errors and prevent the program from terminating unexpectedly.

# 14. What is the purpose of the try clause? What is the purpose of the except clause?
# 
# Try Clause: The purpose of the try clause is to specify a block of code that may potentially raise an exception or error. Python attempts to execute the code inside the try block, and if an error occurs, it jumps to the corresponding except block.
# Except Clause: The purpose of the except clause is to handle exceptions or errors raised in the preceding try block. You can specify the type of exception to catch, or you can use a generic except block to catch all exceptions. The code inside the except block is executed when an exception occurs in the try block, allowing you to handle the error gracefully.
