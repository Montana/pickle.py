#!/usr/bin/python3

import _pickle as pickle
import dill as dill
print(pickle.__doc__)

def main():
    FILENAME = 'pickle.pkl'

    data = dict({ 'montana': [11,22,33,44,55], 'jake': {'a': 'apple', 'b': 'banana'} })
    with open(FILENAME, 'wb') as file1:
        file1.write(pickle.dumps(data))

    with open(FILENAME, 'rb') as file2:
        data = pickle.load(file2)
        print(f"montanas numbers: {data['montana']}")    

print('pickle.py\n---------')
main()
print("----\nDONE")
