from automata.fa.dfa import DFA
from automata.fa.nfa import NFA
from automata.pda.dpda import DPDA
from automata.fa.gnfa import GNFA
from automata.pda.npda import NPDA
from automata.tm.dtm import DTM
import automata.regex.regex as re
from pyformlang.regular_expression import Regex

# NPDA which matches palindromes consisting of 'a's and 'b's
# (accepting by final state)
# q0 reads the first half of the word, q1 the other half, q2 accepts.
# But we have to guess when to switch.
npda = NPDA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'a', 'b'},
    stack_symbols={'A', 'B', '#'},
    transitions={
        'q0': {
            '': {
                '#': {('q2', '#')},
            },
            'a': {
                '#': {('q0', ('A', '#'))},
                'A': {
                    ('q0', ('A', 'A')),
                    ('q1', ''),
                },
                'B': {('q0', ('A', 'B'))},
            },
            'b': {
                '#': {('q0', ('B', '#'))},
                'A': {('q0', ('B', 'A'))},
                'B': {
                    ('q0', ('B', 'B')),
                    ('q1', ''),
                },
            },
        },
        'q1': {
            '': {'#': {('q2', '#')}},
            'a': {'A': {('q1', '')}},
            'b': {'B': {('q1', '')}},
        },
    },
    initial_state='q0',
    initial_stack_symbol='#',
    final_states={'q2'},
    acceptance_mode='final_state'
)
print("npda: ")
my_input_str = 'abbaabba'
if npda.accepts_input(my_input_str):
    print('accepted')
else:
    print('rejected')
# print the diagram of the NPDA
print(npda.show_diagram('D:\src\DFA\ex6.png'))

# Give a PDA that recognizes language { a^n b^n | n >= 0}
# ex1:
#   accepted_states:
#     - "3"
#   edges:
#     - char: a
#       dst: "1"
#       pop: null
#       push: a
#       src: "1"
#     - char: null
#       dst: "3"
#       pop: $
#       push: null
#       src: "2"
#     - char: b
#       dst: "2"
#       pop: a
#       push: null
#       src: "2"
#     - char: null
#       dst: "2"
#       pop: null
#       push: null
#       src: "1"
#     - char: null
#       dst: "1"
#       pop: null
#       push: $
#       src: "0"
#   start_state: "0"

ex1 = NPDA(
    states={'0', '1', '2', '3'},
    input_symbols={'a', 'b'},
    stack_symbols={'a', 'b', '$'},
    transitions={
        '0': {
            '': {
                '$': {('1', '$')},
            },
        },
        '1': {
            'a': {
                '$': {('1', ('a', '$'))},
            },
            'b': {
                'a': {('2', '')},
            },
            '': {
                '$': {('3', '')},
            },
        },
        '2': {
            'a': {
                'a': {('2', '')},
            },
            'b': {
                'a': {('2', '')},
            },
            '': {
                '$': {('2', '')},
            },
        },
    },
    initial_state='0',
    initial_stack_symbol='$',
    final_states={'3'},
    acceptance_mode='final_state'
)

print("ex2: ")
my_input_str = 'aabb'
if ex1.accepts_input(my_input_str):
    print('accepted')
else:
    print('rejected')

# Give a PDA that recognizes language { a^n b^2n | n >= 0}


# Give a PDA that recognizes the language { w | 'w' contains a's and b's and w = reverse(w)}


# Give a PDA that that recognizes the following language: given a string
# containing only 'o' and 'c', letter 'c' can only appear after a
# corresponding letter 'o' appears. There must exist as many o's as c's.


# Give a PDA that recognizes { a^i b^j c^k ∣ i=j ∨ i=k }