# C to Pascal translator
# Sebastian Dabek, Magdalena Zajac
# Formal Languages and Compilers
# Spring 2020

import sys
import ply.lex as lex
import ply.yacc as yacc

## Lexer part
literals = ['+', '-', '*', '/', '(', ')', ',', ';', ":", "#", ' ']

reserved = {
    'while': 'WHILE',
    'else': 'ELSE',
    'switch': 'SWITCH',
    'case': 'CASE',
    'do': 'DO',
    'break': 'BREAK',
    'default': 'DEFAULT',
    'return': 'RETURN',
    'float': 'FLOAT',
    'double': 'DOUBLE',
    'char': 'CHAR',
    'int' : 'INT'
}

tokens = [
             'NUMBER',
             'SEMICOLON',
             'LEFTBRACE',
             'RIGHTBRACE',
             'ASSIGN',
             'EQUAL',
             'INCLUDE',
             # 'EMPTY',
             'VARIABLE',
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
t_DEFAULT = r'default'
t_INCLUDE = r'include'
t_INT = r'int'
t_ignore = '\t'

chars = []

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Obsluga numerow linii
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_string(t):
    r"""".*?\""""
    print("Found string in line {} - String {}".format(t.lineno, t.value))

def t_header(t):
    r'<.*?>'
    print("Found header in line {} - Header {}".format(t.lineno, t.value))

def t_error(t):
    print("line %d: illegal character '%s'" % (t.lineno, t.value[0]))
    chars.append(t.value[0])
    t.lexer.skip(1)

lexer = lex.lex(optimize=1)

## Parser part
def p_error(p):
    print("Syntax error in line %d" % p.lineno)

parser = yacc.yacc()

def has_balanced_parentheses(s):
    if not s: return True
    result = parser.parse(s, lexer=lexer)
    return s == result

## Main
try:
    with open("C:/Users/sebek/PycharmProjects/PascalCTranslator-2/inputFiles/example.c", 'r') as reader:
        lexer.input(reader.read())
        #        parser.parse(reader.read(), lexer=lexer)
        for token in lexer:
            if token.value != ' ':
                print("line %d: %s - %s" % (token.lineno, token.type, token.value))
            else:
                continue
        print("Combined Strings: ", chars)

except OSError as error:
    print("Error: {0}".format(error))

except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
