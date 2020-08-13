'''
3.5.1 calculator
'''
from operator import mul
from functools import reduce


class Exp(object):
    '''
    >>> Exp('add', [1,2])
    Exp('add',[1, 2])
    >>> str(Exp('add',	[1,	Exp('mul',	[2,	3,	4])]))
    'add(1, mul(2, 3, 4))'
    '''

    def __init__(self, operator, operands):
        self.operator = operator
        self.operands = operands

    def __repr__(self):
        return f'Exp({repr(self.operator)},{repr(self.operands)})'

    def __str__(self):
        operands_strs = ', '.join(str(i) for i in self.operands)
        return f'{self.operator}({operands_strs})'


def calc_eval(exp):
    """Evaluate a Calculator expression."""
    if type(exp) in (int, float):
        return exp
    elif type(exp) == Exp:
        arguments = list(map(calc_eval, exp.operands))
        return calc_apply(exp.operator, arguments)


def calc_apply(operator, args):
    '''
    >>>	calc_apply('+',	[1,	2, 3])
    6
    >>> calc_apply('-',[1,2,3])
    -4
    >>>	calc_apply('*', [])
    1
    >>>	calc_apply('/',	[40, 5])
    8.0
    '''
    if operator in ('add', '+'):
        return sum(args)
    if operator in ('sub', '-'):
        if len(args) == 0:
            raise TypeError(operator + 'require more args')
        if len(args) == 1:
            return -args[0]
        return sum(args[:1] + [-arg for arg in args[1:]])
    if operator in ('mul', '*'):
        return reduce(mul, args, 1)
    if operator in ('div', '/'):
        if len(args) != 2:
            raise TypeError(operator + '2')
        numer, denom = args
        return numer/denom


def read_eval_print_loop():
    '''run a read-eval-print loop for'''
    while True:
        try:
            expression_tree = calc_parse('calc> ')
            print(calc_eval(expression_tree))
        except (SyntaxError, TypeError, ZeroDivisionError) as err:
            print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError):
            print('cal end')
            return


def calc_parse(line):
    ''' parse a line of expr'''
    tokens = tokenize(line)
    expression_tree = analyze(tokens)
    if len(tokens) > 0:
        raise SyntaxError('Extra tokens: ' + ' '.join(tokens))
    return expression_tree


def tokenize(line):
    '''convert a string into a list of tokens
    >>> tokenize('add(2, mul(4,	6))')
    ['add', '(', '2', ',', 'mul', '(', '4', ',', '6', ')', ')']
    '''
    spaced = line.replace('(', ' ( ').replace(')', ' ) ').replace(',', ' , ')
    return spaced.split()


def analyze(tokens):
    '''create a tree of nested lists
    >>>	expression	=	'add(2,	mul(4,	6))'
    >>>	analyze(tokenize(expression))
    Exp('add',[2, Exp('mul',[4, 6])])
    >>>	str(analyze(tokenize(expression)))
    'add(2, mul(4, 6))'
    '''
    token = analyze_token(tokens.pop(0))
    if type(token) in (int, float):
        return token
    else:
        tokens.pop(0)
        return Exp(token, analyze_operands(tokens))


def analyze_operands(tokens):
    '''input: list
    '''
    operands = []
    while tokens[0] != ')':
        if operands:
            tokens.pop(0)
        operands.append(analyze(tokens))
    tokens.pop(0)
    return operands


def analyze_token(token):
    '''
    return the value of token if can be analyzed as a number
    '''
    try:
        return int(token)
    except(TypeError, ValueError):
        try:
            return float(token)
        except(TypeError, ValueError):
            return token


if __name__ == "__main__":
    from doctest import testmod
    testmod()
