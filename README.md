# C to Pascal Parser
Project for Formal Languages and Compilers 2020
*Authors: Sebastian Dabek, Magdalena Zajac*

The purpose of this project was to create a simple C to Pascal translator.

This project was created based on [PLY official documentation](https://www.dabeaz.com/ply/) and [university materials](http://home.agh.edu.pl/~mkuta/tklab/ply/ply.html). For grammar rules we've followed [this lex specification](https://www.lysator.liu.se/c/ANSI-C-grammar-l.html) for C and [this yacc specification](http://www.moorecad.com/standardpascal/pascal.y) for Pascal. Also, very useful for comparison of the syntax of this two programming languages was [this article](http://www.cs.gordon.edu/courses/cs320/handouts/C_C++_Syntax_vs_Pascal.html).

## How to run parser

### Before you start
To run this project you will need:
1. **PLY (Python Lex-Yacc)**<br>
More information and installation instructions [here](http://www.dabeaz.com/ply/index.html).

PLY offers several benefits:
- extensive error checking facilities to catch common mistakes
- LR-parsing, which is reasonably efficient and well suited for larger grammars
- there are no separate Lex and Yacc files — everything is in Python
- free software and may be distributed under the terms of the Lesser GPL
2. **Python3**<br>
More information and installation instructions [here](https://www.python.org/downloads/).

To run program run below command
```shell
python3 main.py
```
## How it works
In the first part of *main.py* program we are doing lexical analysis of subset of C language. Files to parse are taken form inputFiles folder. We've created simple programs to test the parser:
- hello-world.c<br>
program is displaying "Hello world" message in the console
- calc.c<br>
program is performs simple mathematical operations like addition, substraction, multiplication and division

To compile and run C program (e.g calc.c) run below commands in inputFiles folder
```shell
gcc -Wall calc.c -o calc
./calc   #Linux
calc     #Windows
```
The subset of C language was chosen to translate above programs.

## General comments
Using available materials about C grammar rules it was very easy to do the lexical analysis of the C programs. The biggest problem occurred while defining parser rules for Pascal. It turned out to be a very complicated process.
