#/usr/bin/env python3

import ply.yacc as yacc
import ZPLLexer
import sys

tokens = ZPLLexer.tokens

def ZPLParser():
    start = 'command_list'

    def p_command_list(p):
        ''' command_list : command
                         | command_list command
        '''
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[2]]
        

    def p_command(p):
        ''' command : COMMAND_CHAR
                    | COMMAND_CHAR DATA_CHAR
        '''
        if len(p) == 3:
            p[0] = (p[1], p[2])
        else:
            p[0] = (p[1],)

    def p_error(p):
        print("Syntax error in input!")
        print(p)
        print("line = ", p.lexer.lineno)
        sys.exit(1)


    parser = yacc.yacc()
    return parser
