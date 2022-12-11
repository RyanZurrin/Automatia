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
# ex1.show_diagram('D:\src\DFA\minitest2_graphs\ex1.png')

# Give a DFA that recognizes all words that contain substring 'b' and end with 'aa'
# example accepted: 'baa', 'abbaaa', 'abbaabbaaa'
# example rejected: 'ab', 'abab', 'aaaaaaaa'
ex2 = DFA(
    states={'q0', 'q1', 'q2', 'q3'},
    input_symbols={'a', 'b'},
    transitions={
        'q0': {'a': 'q0', 'b': 'q1'},
        'q1': {'a': 'q2', 'b': 'q1'},
        'q2': {'a': 'q3', 'b': 'q1'},
        'q3': {'a': 'q3', 'b': 'q1'},
    },
    initial_state='q0',
    final_states={'q3'}
)
print("ex2: ")
my_input_str = 'baa'
if ex2.accepts_input(my_input_str):
    print('accepted')
else:
    print('rejected')
# ex2.show_diagram('D:\src\DFA\minitest2_graphs\ex2.png')

# Give a DFA that recognizes all words that have a length divisible by 3
# example accepted: 'aba', 'aabbaa', 'baaaaab'
# example rejected: 'aabb', 'abaaa', 'abaaaab'
ex3 = DFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'a', 'b'},
    transitions={
        'q0': {'a': 'q1', 'b': 'q1'},
        'q1': {'a': 'q2', 'b': 'q2'},
        'q2': {'a': 'q0', 'b': 'q0'},
    },
    initial_state='q0',
    final_states={'q0'}
)
print("ex3: ")
my_input_str = 'abbaa'
if ex3.accepts_input(my_input_str):
    print('accepted')
else:
    print('rejected')
# ex3.show_diagram('D:\src\DFA\minitest2_graphs\ex3.png')

# Give an NFA that recognizes all words that do not contain 'ab' and have at most 4 characters
# example accepted: 'a', 'ba', 'baa', 'bbbaaaa'
# example rejected: 'ab', 'abab', 'abababaa'
ex4 = NFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9'},
    input_symbols={'a', 'b'},
    transitions={
        'q0': {'a': {'q2'}, 'b': {'q1'}},
        'q1': {'a': {'q4'}, 'b': {'q3'}},
        'q2': {'a': {'q4'}, 'b': {'q9'}},
        'q3': {'a': {'q6'}, 'b': {'q5'}},
        'q4': {'a': {'q6'}, 'b': {'q9'}},
        'q5': {'a': {'q8'}, 'b': {'q7'}},
        'q6': {'a': {'q8'}, 'b': {'q9'}},
        'q7': {'a': {'q9'}, 'b': {'q9'}},
        'q8': {'a': {'q9'}, 'b': {'q9'}},
        'q9': {'a': {'q9'}, 'b': {'q9'}},
    },
    initial_state='q0',
    final_states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8'}
)
print("ex4: ")
my_input_str = 'aaaaa'
if ex4.accepts_input(my_input_str):
    print('accepted')
else:
    print('rejected')
# ex4.show_diagram('D:\src\DFA\minitest2_graphs\ex4.png')

# Give an NFA that recognizes all words that contain substring 'aba' and the character at position 2 is 'a' (using base 1)
# example accepted: 'aabaa', 'babbaba', 'aaaabaa'
# example rejected: 'ab', 'abab', 'abababaa'
ex5 = NFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8'},
    input_symbols={'a', 'b'},
    transitions={
        'q0': {'a': {'q1'}, 'b': {'q2'}},
        'q1': {'a': {'q3'}, 'b': {'q5'}},
        'q2': {'a': {'q3'}, 'b': {'q4'}},
        'q3': {'a': {'q3'}, 'b': {'q6'}},
        'q4': {'a': {'q4'}, 'b': {'q4'}},
        'q5': {'a': {'q5'}, 'b': {'q5'}},
        'q6': {'a': {'q7'}, 'b': {'q8'}},
        'q7': {'a': {'q7'}, 'b': {'q7'}},
        'q8': {'a': {'q3'}, 'b': {'q8'}},
    },
    initial_state='q0',
    final_states={'q7'}
)
print("ex5: ")
my_input_str = 'baaaba'
if ex5.accepts_input(my_input_str):
    print('accepted')
else:
    print('rejected')
# ex5.show_diagram('D:\src\DFA\minitest2_graphs\ex5.png')

# Give an NFA that recognizes all words that are in ((ab)*) || b
# example accepted: 'b', 'ab', 'abab', 'ababab' ... etc
# example rejected: 'a', 'aa', 'ba','baa', 'bab' ... etc
ex6 = NFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4'},
    input_symbols={'a', 'b'},
    transitions={
        'q0': {'a': {'q3'}, 'b': {'q1'}},
        'q1': {'a': {'q2'}, 'b': {'q2'}},
        'q2': {'a': {'q2'}, 'b': {'q2'}},
        'q3': {'a': {'q2'}, 'b': {'q4'}},
        'q4': {'a': {'q3'}, 'b': {'q2'}},
    },
    initial_state='q0',
    final_states={'q0', 'q1', 'q4'}
)
print("ex6: ")
my_input_str = 'ababab'
if ex6.accepts_input(my_input_str):
    print('accepted')
else:
    print('rejected')
# ex6.show_diagram('D:\src\DFA\minitest2_graphs\ex6.png')

# Give an NFA that recognizes all words that have at least 3 characters or are in (a{})*
# example accepted: 'aaa', 'aab', 'abaa', 'baaaa', 'aaaaa', or {}
# example rejected: 'b', 'ab', 'bb', 'ba', 'aa', 'a'
ex7 = NFA(
    states={'q0', 'q1', 'q2', 'q3'},
    input_symbols={'a', 'b'},
    transitions={
        'q0': {'a': {'q1'}, 'b': {'q1'}},
        'q1': {'a': {'q2'}, 'b': {'q2'}},
        'q2': {'a': {'q3'}, 'b': {'q3'}},
        'q3': {'a': {'q3'}, 'b': {'q3'}},
    },
    initial_state='q0',
    final_states={'q0', 'q3'}
)
print("ex7: ")
my_input_str = ''
if ex7.accepts_input(my_input_str):
    print('accepted')
else:
    print('rejected')
# ex7.show_diagram('D:\src\DFA\minitest2_graphs\ex7.png')
