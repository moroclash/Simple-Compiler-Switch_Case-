import ply.lex as lex
import ply.yacc as yacc



recervied = {'switch' : 'SWITCH' , 'case' : 'CASE' , 'break' :'BREAK', 'finally':'FINALLY' , 'print' :'PRINT' }
tokens = ["colon", "name","lparen" , "rparen" , "blparen" , "erparen" , "number","dqutation" ,"equal","simicolon"] + list(recervied.values())

t_simicolon=r'\;'
t_equal = r'\='
t_ignore = r' /t'
t_colon = r'\:'
t_lparen = r'\('
t_rparen  = r'\)'
t_blparen = r'\{'
t_erparen = r'\}'
t_dqutation = r'\"'

def t_name(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    t.type = recervied.get(t.value , 'name')
    return t



def t_tab(t):
    r'\t'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_number(s):
    r'\d+'
    s.value = int(s.value)
    return s


def t_error(d):
    print("error in lex")
    d.lexer.skip(1)


lexer = lex.lex()

#-------------------------------
#lexer.input("dsad")
#while True:
#    tok = lexer.token()
#    if not tok:
#      break
#    print(tok)
#-------------------------------


def p_switch_begin(p):
    '''
       switch_begin : switch_s
                    | none
    '''

def p_none(p):
    '''
        none :
    '''

def p_switch_s(p):
    '''
        switch_s : SWITCH lparen name rparen blparen  CASELIST inter_finally erparen
                 | SWITCH lparen name rparen blparen  erparen
    '''
def p_CASELIST (p):
    '''
       CASELIST : inter_case simicolon
                | inter_case simicolon CASELIST
    '''

def p_term(p):
    '''
        term : name
             | number
             | dqutation term dqutation
    '''
def p_exp(p):
    '''
        exp : PRINT  lparen term rparen
            | none
            | name equal term
            | switch_s
    '''

def p_inter_case(p):
    '''
       inter_case : CASE term colon exp BREAK
    '''

def p_inter_finally(p):
    '''
       inter_finally : FINALLY colon exp
                     | none
    '''

def p_error(p):
    try:
        print("Syntax Error in '%s'" , p.value)
    except:
        print("Syntax Error")

parser = yacc.yacc()

#-----------------------------
file = open('data.txt');
data = file.read()
#-----------------------------

parser.parse(data)
