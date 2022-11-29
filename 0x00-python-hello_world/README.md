<h1>0x00. Python - Hello, World</h1>

<p>Introduction to python. Scripting between bash and python3. Setting up python and the very basics.</p>

New commands / functions used:
python3, pip install pep8, pep8 script.py, import sys, sys.stderr.write(), sys.exit, string[3:-1]

Description of Files
0-run
A shell script that runs a Python script. The name of the script is stored in the environmental variable $PYFILE
1-run_inline
A shell script that runs python code. The python code will be saved in the environment variable $PYCODE
2-print.py
A python script that prints exactly ``"Programming is like building a multilingual puzzle``
3-print_number.py
Complete a source code to print the integer stored in the variable ``number``, followed by ``Battery Street`` followed by a new line
4-print_float.py
Complete the source code in order to print the float stored in the variable ``number`` with a precision of 2 digits.
5-print_string.py
Complete the source code in order to print 3 times a string stored in the variable ``str`` followed by its first 9 characters.
6-concat.py
Complete the source code to print ``Welcome to Holberton School!``. No Loops or conditional statements. Use the variables ``str1`` and ``str2``. Code should be exactly 5 lines long.
7-edges.py
Complete the source code.
8-concat_edges.py
Complete the source code to print ``object-oriented programming with Python`` followed by a new line.
9-easter_egg.py
Write a Python script that prints "The Zen of Python" by Tim Peters, followed by a new line.
100-write.py
Write a Python script that prints out exactly: ``and that piece of art is useful - Dora Korpar, 2015-10-19``. Use the function ``write`` from the ``sys`` module. Do not use ``print``, and print it to stderr. Script should exit with status code 1.
101-compile
Write a script that compiles a Python script file. The Python file name will be stored in the environment variable ``$PYFILE`` The output file name is ``$PYFILEc`` (ex: ``PYFILE=my_main.py`` => ``my_main.pyc``)
102-magic_calculation.py
Write the python function def magic_calculation(a, b): that does exactly as the following Python bytecode:

  3           0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE