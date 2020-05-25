import sys

import ply.lex as lex

# Reserved words
reserved = (
    'BREAK', 'CASE', 'CHAR', 'CONST', 'CONTINUE', 'DEFAULT', 'DO', 'DOUBLE',
    'ELSE', 'ENUM', 'FLOAT', 'FOR', 'IF', 'INT', 'LONG', 'RETURN',
    'SHORT', 'SIGNED', 'SIZEOF', 'STATIC', 'STRUCT', 'SWITCH','UNSIGNED',
    'VOID', 'WHILE',
)

tokens = reserved + (
    # Literals (identifier, integer constant, float constant, string constant,
    # char const)
    'ID', 'TYPEID', 'ICONST', 'FCONST', 'SCONST', 'CCONST',

    # Operators (+,-,*,/,|,&, !, ||, &&, <, <=, >, >=, ==, !=)
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'OR', 'AND', 'NOT', 'XOR', 'LOR', 'LAND', 'LNOT',
    'LT', 'LE', 'GT', 'GE', 'EQ', 'NE',

    # Assignment (=, +=, -=)
    'EQUALS', 'PLUSEQUAL', 'MINUSEQUAL',

    # Increment/decrement (++,--)
    'PLUSPLUS', 'MINUSMINUS',

    # Delimeters ( ) [ ] { } , . ; :
    'LPAREN', 'RPAREN',
    'LBRACKET', 'RBRACKET',
    'LBRACE', 'RBRACE',
    'COMMA', 'PERIOD',
    'SEMI', 'COLON',

    # Ellipsis (...)
    'ELLIPSIS',

    #Pascal
    'ASSIGNMENT', 'DOT', 'END', 'FUNCTION', 'PROCEDURE', 'PROGRAM', 'VAR',
)

# Completely ignored characters
t_ignore = ' \t\x0c'

# Newlines
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

# Operators
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_OR = r'\|'
t_AND = r'&'
t_NOT = r'~'
t_XOR = r'\^'
t_LOR = r'\|\|'
t_LAND = r'&&'
t_LNOT = r'!'
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_EQ = r'=='
t_NE = r'!='

# Assignment operators
t_EQUALS = r'='
t_PLUSEQUAL = r'\+='
t_MINUSEQUAL = r'-='

# Increment/decrement
t_PLUSPLUS = r'\+\+'
t_MINUSMINUS = r'--'

# Delimeters
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_PERIOD = r'\.'
t_SEMI = r';'
t_COLON = r':'
t_ELLIPSIS = r'\.\.\.'

#Pascal
t_DOT = r'\.'
t_ASSIGNMENT = r':='
t_END = r'END'
t_FUNCTION = r'FUNCTION'
t_PROCEDURE = r'PROCEDURE'
t_PROGRAM = r'PROGRAM'
t_VAR = r'VAR'

# Identifiers and reserved words
reserved_map = {}

for r in reserved:
    reserved_map[r.lower()] = r

def t_ID(t):
    r'[A-Za-z_][\w_]*'
    t.type = reserved_map.get(t.value, "ID")
    return t

# Integer literal
t_ICONST = r'\d+([uU]|[lL]|[uU][lL]|[lL][uU])?'

# Floating literal
t_FCONST = r'((\d+)(\.\d+)(e(\+|-)?(\d+))? | (\d+)e(\+|-)?(\d+))([lL]|[fF])?'

# String literal
t_SCONST = r'\"([^\\\n]|(\\.))*?\"'

# Character constant 'c' or L'c'
t_CCONST = r'(L)?\'([^\\\n]|(\\.))*?\''

# Comments
def t_comment(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

# Preprocessor directive (ignored)
def t_preprocessor(t):
    r'\#(.)*?\n'
    t.lexer.lineno += 1

def t_error(t):
    print("Illegal character %s" % repr(t.value[0]))
    t.lexer.skip(1)

lexer = lex.lex()

try:
    with open("inputFiles/calc.c", 'r') as reader:
        text = reader.read()
        lexer.input(text)
        for token in lexer:
            print("line %d: %s(%s)" %(token.lineno, token.type, token.value))

except OSError as error:
    print("Error: {0}".format(error))

except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
