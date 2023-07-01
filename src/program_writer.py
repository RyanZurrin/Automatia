# python program that writes another python program and saves it then executes it
# then reades it back in and modifies it and saves it again and executes it in a loop

import os
import sys
import time
import random
import string
import subprocess
import importlib
import importlib.util

global counter

def main():
    counter = 0
    while True:
        # create a new python program
        # write it to a file
        # execute it
        # read it back in
        # modify it
        # write it to a file
        # execute it
        # repeat
        file_name = 'add_x.py'

        # create a new python program and write it to a file
        with open(file_name, 'w') as f:
            f.write('def add_x(x):\n')
            f.write(f'    return x + {counter}\n')

        # execute the python program
        spec = importlib.util.spec_from_file_location('add_x', file_name)
        add_x = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(add_x)
        print(add_x.add_x(1))

        # read the python program back in
        with open(file_name, 'r') as f:
            lines = f.readlines()

        # modify the python program 1 + 1 = 2 then 1 + 2 = 3 then 1 + 3 = 4 etc
        lines[1] = f'    return x + {random.randint(1, 100)}' + '\n'

        # write the modified python program to a file
        with open(file_name, 'w') as f:
            f.writelines(lines)

        # execute the modified python program
        spec = importlib.util.spec_from_file_location('add_x', file_name)
        add_x = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(add_x)
        print(add_x.add_x(1))

        counter += 1


        # wait a random amount of time
        time.sleep(random.randint(1, 5))


if __name__ == '__main__':
    main()