from automata.fa.dfa import DFA
from automata.fa.nfa import NFA
from automata.pda.dpda import DPDA
from automata.fa.gnfa import GNFA
from automata.pda.npda import NPDA
from automata.tm.dtm import DTM
# dfa = DFA(
#     states={'q0', 'q1', 'q2'},
#     input_symbols={'0', '1'},
#     transitions={
#         'q0': {'0': 'q0', '1': 'q1'},
#         'q1': {'0': 'q0', '1': 'q2'},
#         'q2': {'0': 'q2', '1': 'q1'},
#     },
#     initial_state='q0',
#     final_states={'q1'}
# )
# other_dfa = DFA(
#     states={'q0', 'q1', 'q2', 'q3'},
#     input_symbols={'0', '1'},
#     transitions={
#         'q0': {'0': 'q3', '1': 'q1'},
#         'q1': {'0': 'q3', '1': 'q2'},
#         'q2': {'0': 'q3', '1': 'q2'},
#         'q3': {'0': 'q3', '1': 'q3'},
#     },
#     initial_state='q0',
#     final_states={'q2'}
# )


# Give a DFA that recognizes all words that end with 'ba'
# example accepted: 'abba', 'ba', 'abbaabba'
# example rejected: 'ab', 'abab', 'abababaa'
ex1 = DFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'a', 'b'},
    transitions={
        'q0': {'a': 'q0', 'b': 'q1'},
        'q1': {'a': 'q2', 'b': 'q1'},
        'q2': {'a': 'q0', 'b': 'q1'},
    },
    initial_state='q0',
    final_states={'q2'}
)
print("ex1: ")
my_input_str = 'abbbaa'
if ex1.accepts_input(my_input_str):
    print('accepted')
else:
    print('rejected')

# ex1.read_input('abba')
# # dfa.read_input('011')
# print(ex1.read_input_stepwise('bbaaba'))
# # step through the input string and print the current state
# # after each step
# for step in ex1.read_input_stepwise('abba'):
#     print(step)
# print(ex1.validate())
#
# minimal_dfa = ex1.minify()
# print(ex1.transitions)
# print(minimal_dfa.transitions)

minimal_dfa_with_old_names = ex1.minify(retain_names=True)

# Give a DFA that recognizes all words that do not contain 'aa'
# example accepted: 'ab', 'abab', 'abababaa'
# example rejected: 'abba', 'ba', 'abbaabba'
ex2 = DFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'a', 'b'},
    transitions={
        'q0': {'a': 'q1', 'b': 'q0'},
        'q1': {'a': 'q2', 'b': 'q0'},
        'q2': {'a': 'q2', 'b': 'q2'},
    },
    initial_state='q0',
    final_states={'q0', 'q1'}
)
print("ex2: ")
my_input_str = 'abbbabbabbab'
if ex2.accepts_input(my_input_str):
    print('accepted')
else:
    print('rejected')

# Give a DFA that recognizes all words that have at least 4 characters
# example accepted: 'abba', 'baaaba', 'abbaabba'
# example rejected: 'ab', 'a', 'aab'
ex3 = DFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4'},
    input_symbols={'a', 'b'},
    transitions={
        'q0': {'a': 'q1', 'b': 'q1'},
        'q1': {'a': 'q2', 'b': 'q2'},
        'q2': {'a': 'q3', 'b': 'q3'},
        'q3': {'a': 'q4', 'b': 'q4'},
        'q4': {'a': 'q4', 'b': 'q4'},
    },
    initial_state='q0',
    final_states={'q4'}
)
print("ex3: ")
my_input_str = 'abba'
if ex3.accepts_input(my_input_str):
    print('accepted')
else:
    print('rejected')

# Give an NFA that recognizes all words that the character at position 2 is 'a' (using base 1)
# example accepted: 'babbbb', 'aaabbabab', 'baaaaa' (position 2 is 'a')
# example rejected: 'abba', 'bba', 'abbaabba' (position 2 is not 'a')
ex4 = NFA(
    states={'q0', 'q1', 'q2', 'q3'},
    input_symbols={'a', 'b'},
    transitions={
        'q0': {'a': {'q1'}, 'b': {'q1'}},
        'q1': {'a': {'q2'}, 'b': {'q3'}},
        'q2': {'a': {'q2'}, 'b': {'q2'}},
        'q3': {'a': {'q3'}, 'b': {'q3'}},
    },
    initial_state='q0',
    final_states={'q2'}
)
print("ex4: ")
my_input_str = 'baab'
if ex4.accepts_input(my_input_str):
    print('accepted')
else:
    print('rejected')

# Give an NFA that recognizes all words that start with 'a' and end with 'b'
# example accepted: 'ab', 'aab', 'aaab', 'ababbb', 'abababab' (start with 'a' and end with 'b')
# example rejected: 'ba', 'bba', 'abbaabba' (start with 'b' or end with 'a')
ex5 = NFA(
    states={'q0', 'q1', 'q2', 'q3'},
    input_symbols={'a', 'b'},
    transitions={
        'q0': {'a': {'q1'}, 'b': {'q3'}},
        'q1': {'a': {'q1'}, 'b': {'q2'}},
        'q2': {'a': {'q1'}, 'b': {'q2'}},
        'q3': {'a': {'q3'}, 'b': {'q3'}},
    },
    initial_state='q0',
    final_states={'q2'}
)
print("ex5: ")
my_input_str = 'abab'
if ex5.accepts_input(my_input_str):
    print('accepted')
else:
    print('rejected')
