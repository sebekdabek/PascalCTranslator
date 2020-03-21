# C to Pascal translator
# Sebastian Dabek, Magdalena Zajac
# Formal Languages and Compilers
# Spring 2020

import sys
import ply.lex as lex
import ply.yacc as yacc;

## Lexer part
literals = [ '+','-','*','/','(',')',',' ]

reserved = {
    'while' : 'WHILE',
    'else' : 'ELSE',
    'switch':'SWITCH',
    'case':'CASE',
    'do' : 'DO',
    'break': 'BREAK',
    'default': 'DEFAULT',
    'return' : 'RETURN',
    'float' : 'FLOAT',
    'double' : 'DOUBLE',
    'char' : 'CHAR',
    'printf':'PRINTF',
    'scanf' : 'SCANF'
}

tokens = [
    'NUMBER',
    'SEMICOLON',
    'LEFTBRACE',
    'RIGHTBRACE',
    'ASSIGN',
    'EQUAL',
] + list(reserved.values())

t_SEMICOLON = r'\;'
t_LEFTBRACE = r'\{'
t_RIGHTBRACE = r'\}'
t_ASSIGN = r'='
t_EQUAL = r'=='
t_WHILE = r'while'
t_ELSE = r'else'
t_SWITCH = r'switch'
t_CASE = r'case'
t_DO = r'do'
t_BREAK = r'break'
t_RETURN = r'return'
t_FLOAT = 'float'
t_DOUBLE = r'double'
t_CHAR = r'char'
t_PRINTF = r'printf'
t_SCANF = r'scanf'
t_DEFAULT = r'default'

t_ignore = ' \t'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("line %d: illegal character '%s'" %(t.lineno, t.value[0]) )
    t.lexer.skip(1)

lexer = lex.lex()

## Parser part
def p_error(p):
    print(  "syntax error in line %d" % p.lineno)

#parser = yacc.yacc()

## Main
try:
    with open("inputFiles/calc.c", 'r') as reader:
        lexer.input(reader.read())
#        parser.parse(reader.read(), lexer=lexer)
        for token in lexer:
            print("line %d: %s(%s)" %(token.lineno, token.type, token.value))

except OSError as error:
    print("Error: {0}".format(error))

except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
