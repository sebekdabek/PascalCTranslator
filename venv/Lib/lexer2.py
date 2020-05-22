import sys
from ply import lex
from ply import yacc

states = (
    ('foo', 'exclusive'), ('bar', 'inclusive')
)

reserved = {
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'while': 'WHILE',
    'return': 'RETURN'
}

tokens = [
             'PLUS',
             'MINUS',
             'TIMES',
             'DIVIDE',
             'LPAREN',
             'RPAREN',
             'LBRACE',
             'RBRACE',
             'NUMBER',
             'ID',
             'VAR',
         ] + list(reserved.values())

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'{'
t_RBRACE = r'}'

literals = ['+', '-', '*', '/', '(', ')']


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_ID(t):
    r'[a-zA-Z_]\w*'
    t.type = reserved.get(t.value, 'ID')
    return t


t_ignore = '  \t'
t_foo_NUMBER = r'\d+'
t_bar_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'


def t_foo_newline(t):
    r'\n'
    t.lexer.lineno += 1


# obsluga numerow linii
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# blad przy napotkaniu nowej linii
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# starting foo state
def t_begin_foo(t):
    r'start foo'
    t.lexer.begin('foo')


# getting back to initial
def t_foo_end(t):
    r'end_foo'
    t.lexer.begin('INITIAL')


# from yacc
# def p_expression_binop(p):
#     """expression  : expression LITERALS expression"""
#     if p[2] == '+':
#         p[0] = p[1] + p[3]
#     elif p[2] == '-':
#         p[0] = p[1] - p[3]
#     elif p[2] == '*':
#         p[0] = p[1] * p[3]
#     elif p[2] == '/':
#         p[0] = p[1] / p[3]

# Expression part
precedence = (
    ("right", '='),
    ("left", '+', '-'),
    ("left", '*', '/'),
)


def p_error(p):
    print("parsing error\n")


def p_start(p):
    """start : EXPRESSION
             | start EXPRESSION"""
    if len(p) == 2:
        print("p[1]=", p[1])
    else:
        print("p[2]=", p[2])


def p_expression_number(p):
    """EXPRESSION : NUMBER"""
    p[0] = p[1]


def p_expression_var(p):
    """EXPRESSION : VAR"""
    val = symtab.get(p[1])
    if val:
        p[0] = val
    else:
        p[0] = 0
        print("%s not used\n" % p[1])


def p_expression_assignment(p):
    """EXPRESSION : VAR '=' EXPRESSION"""
    p[0] = p[3]
    symtab[p[1]] = p[3]


def p_expression_sum(p):
    """EXPRESSION : EXPRESSION '+' EXPRESSION
                  | EXPRESSION '-' EXPRESSION"""
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]


def p_expression_mul(p):
    """EXPRESSION : EXPRESSION '*' EXPRESSION
                  | EXPRESSION '/' EXPRESSION"""
    if p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]


def p_expression_group(p):
    """EXPRESSION : '(' EXPRESSION ')'"""
    p[0] = p[2]


# End of expression part


# def p_error(p):
#     print("syntax error in line %d" % p.lineno)


# def p_production(p):
#     'production : some production ...'
#     raise SyntaxError

# main part
lexer = lex.lex()
fh = open("C:/Users/sebek/PycharmProjects/PascalCTranslator-2/inputFiles/example.c", 'r')
lexer.input(fh.read())
for token in lexer:
    print("line {0}: {1}({2})".format(token.lineno, token.type, token.value))

print(10 * '=')

# lexer = lex.lex()
parser = yacc.yacc()
text = fh.read()
parser.parse(text, lexer=lexer)
