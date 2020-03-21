# C to Pascal translator
# Sebastian Dabek, Magdalena Zajac
# Formal Languages and Compilers
# Spring 2020

import sys
import ply.lex as lex
from config import file_location

tokens = (
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'NUMBER',
    'COMMA',
    'SEMICOLON',
    'LEFTBRACE',
    'RIGHTBRACE',
    'ASSIGN',
    'EQUAL',
)

#reserved = {
#    'while' : 'WHILE',
#    'else' : 'ELSE',
#    'switch':'SWITCH',
#    'case':'CASE',
#    'do' : 'DO',
#    'break': 'BREAK',
#    'return' : 'RETURN',
#    'float' : 'FLOAT',
#    'double' : 'DOUBLE',
#    'char' : 'CHAR',
#    'printf':'PRINTF',
#    'scanf' : 'SCANF'
#}

t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r'\,'
t_SEMICOLON = r'\;'
t_LEFTBRACE = r'\{'
t_RIGHTBRACE = r'\}'
t_ASSIGN = r'='
t_EQUAL = r'=='
#t_WHILE = r'while'
#t_ELSE = r'else'
#t_SWITCH = r'switch'
#t_CASE = r'case'
#t_DO = r'do'
#t_BREAK = r'break'
#t_RETURN = r'return'
#t_FLOAT = 'float'
#t_DOUBLE = r'double'
#t_CHAR = r'char'
#t_PRINTF = r'printf'
#t_SCANF = r'scanf'

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

try:
    with open(file_location, 'r') as reader:
        lexer.input(reader.read())
        for token in lexer:
            print("line %d: %s(%s)" %(token.lineno, token.type, token.value))

except OSError as error:
    print("Error: {0}".format(error))

except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
