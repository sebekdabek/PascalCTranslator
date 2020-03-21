# C to Pascal Parser
Project for Formal Languages and Compilers 2020

## How to run
*Below instructions explain how to do this on **Linux***
### Before you start
To run this project you will need:
1. **PLY (Python Lex-Yacc)**<br>
More information and installation instructions [here](http://www.dabeaz.com/ply/index.html).
2. **Python3**<br>
More information and installation instructions [here](https://www.python.org/downloads/).

To run parser run below command
```shell
python3 parser.py
```
To compile and run C program run below commands in inputFiles folder
```shell
gcc -Wall calc.c -o calc && ./calc
```
## How it works
In the first part of *parser.py* program we are doing lexical analysis of subset of C language. Files to parse are taken form inputFiles folder. We've created simple programs to test the parser:
- hello-world.c<br>
program is displaying "Hello world" message in the console
- calc.c<br>
program is performs simple mathematical operations like addition, substraction, multiplication and division
