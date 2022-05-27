'''Module to read wing loads'''

import pandas as pd
import os
import sys

from wing_class import Wing

class Load(Wing):
    def __init__(self, b):
        super().__init__(b)

# Methods
def read_load(load_sheet_name='loads_exemple.csv'):
    #path_parent = os.path.dirname(os.getcwd())
    #os.chdir(path_parent)
    #cwd = os.path.abspath(os.getcwd())
    #load_dir = os.path.join(cwd, 'load_dir')
    #load_file = os.path.join(load_dir, load_sheet_name)
    #load_sheet = pd.read_csv(load_file)
    #load_sheet = pd.read_csv('../load_dir/loads_exemple.csv')
    load_sheet = pd.read_csv(f'load_dir/{load_sheet_name}')


def __repr__(self):
    
    pass

if __name__ == '__main__':
    read_load('loads_exemple.csv')
    print(read_load)