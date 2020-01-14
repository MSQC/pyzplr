#!/usr/bin/env python3

import ply.lex as lex
import re

tokens = [
        'DATA_CHAR',
        'COMMAND_CHAR',
        'NEWLINE',
        ]

t_DATA_CHAR    = r'[^^~]+'
t_COMMAND_CHAR = r'[~^][A-Z0-9bd]{2}'
#reserved = {
#}
#
#tokens += list(reserved.values())

def t_NEWLINE(t):
    r'[\r\n]+'
    pass

def t_error(t):
    print("Illegal character '%s' (%d)" % (t.value[0], ord(t.value[0])))
    t.lexer.skip(1)

def ZPLLexer():
    return lex.lex()

