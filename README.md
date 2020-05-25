# C to Pascal Parser
Project for Formal Languages and Compilers 2020

This project was created based on [PLY official documentation](https://www.dabeaz.com/ply/) and [university materials](http://home.agh.edu.pl/~mkuta/tklab/ply/ply.html). For grammar rules we've followed [this lex specification](https://www.lysator.liu.se/c/ANSI-C-grammar-l.html) for C and [this yacc specification](http://www.moorecad.com/standardpascal/pascal.y) for Pascal.

## How to run parser

### Before you start
To run this project you will need:
1. **PLY (Python Lex-Yacc)**<br>
More information and installation instructions [here](http://www.dabeaz.com/ply/index.html).
2. **Python3**<br>
More information and installation instructions [here](https://www.python.org/downloads/).

To run program run below command
```shell
python3 main.py
```
## How it works
In the first part of *parser.py* program we are doing lexical analysis of subset of C language. Files to parse are taken form inputFiles folder. We've created simple programs to test the parser:
- hello-world.c<br>
program is displaying "Hello world" message in the console
- calc.c<br>
program is performs simple mathematical operations like addition, substraction, multiplication and division

To compile and run C program (e.g calc.c) run below commands in inputFiles folder
```shell
gcc -Wall calc.c -o calc
./calc #Linux
calc   #Windows
```
The subset of C language was chosen to translate above programs.
