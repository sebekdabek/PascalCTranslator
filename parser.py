import sys
import ply.lex as lex
import ply.yacc as yacc

reserved = (
    'BREAK', 'CASE', 'CHAR', 'CONST', 'CONTINUE', 'DEFAULT', 'DO', 'DOUBLE',
    'ELSE', 'ENUM', 'FLOAT', 'FOR', 'IF', 'INT', 'LONG', 'RETURN',
    'SHORT', 'SIGNED', 'SIZEOF', 'STATIC', 'STRUCT', 'SWITCH','UNSIGNED',
    'VOID', 'WHILE', 'END', 'FUNCTION', 'PROCEDURE', 'PROGRAM', 'VAR', 'BEGIN',
)

tokens = reserved + (
    'ID', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN',
    'LBRACKET', 'RBRACKET', 'LBRACE', 'RBRACE', 'COMMA', 'DOT',
    'SEMI', 'COLON', 'ICONST', 'FCONST', 'SCONST', 'CCONST',
)


t_ignore = ' \t\x0c'

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_DOT = r'\.'
t_SEMI = r';'
t_COLON = r':'
t_ICONST = r'\d+([uU]|[lL]|[uU][lL]|[lL][uU])?'
t_FCONST = r'((\d+)(\.\d+)(e(\+|-)?(\d+))? | (\d+)e(\+|-)?(\d+))([lL]|[fF])?'
t_SCONST = r'\"([^\\\n]|(\\.))*?\"'
t_CCONST = r'(L)?\'([^\\\n]|(\\.))*?\''

reserved_map = {}

for r in reserved:
    reserved_map[r.lower()] = r


def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_ID(t):
    r'[A-Za-z_][\w_]*'
    t.type = reserved_map.get(t.value, "ID")
    return t


def t_comment(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')


def t_error(t):
    print("Illegal character %s" % repr(t.value[0]))
    t.lexer.skip(1)


def p_program_start(t):
	'program : header SEMI block DOT'
	t[0] = Node('program',t[1],t[3])

def p_header(t):
	'header : PROGRAM identifier'
	t[0] = t[2]

def p_block(t):
	"""block : variable_declaration_part procedure_or_function statement_part
	"""
	t[0] = Node('block',t[1],t[2],t[3])


def p_variable_declaration_part(t):
	"""variable_declaration_part : VAR variable_declaration_list
	 |
	"""
	if len(t) > 1:
		t[0] = t[2]

def p_variable_declaration_list(t):
	"""variable_declaration_list : variable_declaration variable_declaration_list
	 | variable_declaration
	"""
	# function and procedure missing here
	if len(t) == 2:
		t[0] = t[1]
	else:
		t[0] = Node('var_list',t[1],t[2])

def p_variable_declaration(t):
	"""variable_declaration : identifier COLON type SEMI"""
	t[0] = Node('var',t[1],t[3])



def p_procedure_or_function(t):
	"""procedure_or_function : proc_or_func_declaration SEMI procedure_or_function
		| """

	if len(t) == 4:
		t[0] = Node('function_list',t[1],t[3])


def p_proc_or_func_declaration(t):
	""" proc_or_func_declaration : procedure_declaration
               | function_declaration """
	t[0] = t[1]


def p_procedure_declaration(t):
	"""procedure_declaration : procedure_heading SEMI block"""
	t[0] = Node("procedure",t[1],t[3])


def p_procedure_heading(t):
	""" procedure_heading : PROCEDURE identifier
	| PROCEDURE identifier LPAREN parameter_list RPAREN"""

	if len(t) == 3:
		t[0] = Node("procedure_head",t[2])
	else:
		t[0] = Node("procedure_head",t[2],t[4])


def p_function_declaration(t):
	""" function_declaration : function_heading SEMI block"""
	t[0] = Node('function',t[1],t[3])


def p_function_heading(t):
	""" function_heading : FUNCTION type
	 	| FUNCTION identifier COLON type
		| FUNCTION identifier LPAREN parameter_list RPAREN COLON type"""
	if len(t) == 3:
		t[0] = Node("function_head",t[2])
	elif len(t) == 5:
		t[0] = Node("function_head",t[2],t[3])
	else:
		t[0] = Node("function_head",t[2],t[4],t[7])


def p_parameter_list(t):
	""" parameter_list : parameter COMMA parameter_list
	| parameter"""
	if len(t) == 4:
		t[0] = Node("parameter_list", t[1], t[3])
	else:
		t[0] = t[1]

def p_parameter(t):
	""" parameter : identifier COLON type"""
	t[0] = Node("parameter", t[1], t[3])

def p_type(t):
	""" type : ICONST
	| FCONST
	| SCONST
	| CCONST """
	t[0] = Node('type',t[1].lower())

def p_statement_part(t):
	"""statement_part : BEGIN statement_sequence END"""
	t[0] = t[2]

def p_statement_sequence(t):
	"""statement_sequence : statement SEMI statement_sequence
	 | statement"""
	if len(t) == 2:
		t[0] = t[1]
	else:
		t[0] = Node('statement_list',t[1],t[3])

def p_statement(t):
	"""statement : statement_part
	 |
	"""
	if len(t) > 1:
		t[0] = t[1]


def p_identifier(p):
    """identifier : ID"""
    p[0] = p[1]


def p_sign(p):
    """sign : PLUS
            | MINUS"""
    if p[0] == '+':
        p[0] = p[1]
    elif p[0] == '-':
        p[0] = p[2]


def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")


lexer = lex.lex()
parser = yacc.yacc()
reader = open("inputFiles/helloworld.c", 'r')
text = reader.read()
parser.parse(text, lexer=lexer)
