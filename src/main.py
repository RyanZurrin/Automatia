from automata.fa.dfa import DFA
from automata.fa.nfa import NFA
from automata.pda.dpda import DPDA
from automata.fa.gnfa import GNFA
from automata.pda.npda import NPDA
from automata.tm.dtm import DTM
import automata.regex.regex as re
from pyformlang.regular_expression import Regex

reg = Regex('a*')
print(f'reg accepts: {reg.accepts("aa a")}')

# Give a DFA that recognizes all words that start with 'bba'
# example accepted: 'bba', 'bbabba', 'bbabbaabba'
# example rejected: 'ab', 'abab', 'abababaa'
ex1 = DFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4'},
    input_symbols={'a', 'b'},
    transitions={
        'q0': {'a': 'q4', 'b': 'q1'},
        'q1': {'a': 'q4', 'b': 'q2'},
        'q2': {'a': 'q3', 'b': 'q4'},
        'q3': {'a': 'q3', 'b': 'q3'},
        'q4': {'a': 'q4', 'b': 'q4'},
    },
    initial_state='q0',
    final_states={'q3'}
)
print("ex1: ")
my_input_str = 'bbababbaaaabababa'
if ex1.accepts_input(my_input_str):
    print('accepted')
else:
    print('rejected')

# Give a NFA that recognizes any string that ends in '0'
# example accepted: '0', '10', '110', '1110'
# example rejected: '1', '11', '111', '1111'
ex2 = NFA(
    states={'q0', 'q1'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': {'q0', 'q1'}, '1': {'q0'}},
        'q1': {'0': {'q1'}},
    },
    initial_state='q0',
    final_states={'q1'}
)
print("ex2: ")
my_input_str = '11010110'
if ex2.accepts_input(my_input_str):
    print('accepted')
else:
    print('rejected')


