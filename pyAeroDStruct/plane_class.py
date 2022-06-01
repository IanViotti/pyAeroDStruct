import pandas as pd
import numpy as np

from .utils import *

import os

class Plane():
    def __init__(self, b, MTOW, n_step = 1000):
        
        # Check b
        if not isinstance(b, float) and not isinstance(b,int) or not b > 0 :
            raise ValueError(
                'span must be of type float or int and a positive number'
                )  
        
        # Check n_step
        if not isinstance(n_step, int) or not n_step > 1 :
            raise ValueError(
                'n_step must be of type int and a greater than 1'
                )   
        
        
        self._b = b
        self._MTOW = MTOW
        self._n_step = n_step
        self._chord = None
        self._cm = None
        self._y = None

    @property
    def y(self):
        '''Creates an array representing y coordenate from the wingroot to wingtip.
        
        Parameters
        ----------
        None

        Returns
        -------
        y: np.ndarray
            array representing distance from fuselage to wingtip.
        '''
        self._y = np.linspace(0, self._b, self._n_step)
        return self._y

    @property   
    def chord(self, chord_sheet_name='chord_exemple.csv'):
        '''Read chord input along span from an .csv file.

        Paramters
        ---------
        chord_sheet_name: str
            .csv file name in wich the chord is stored. See file
            exemple in data directory for file format.

        Returns
        -------
        chord_array: np.ndarray
            chord value alon wing span.
        self: Plane
            Object of the Plane class.
        '''
        chord_sheet = pd.read_csv(f'data/{chord_sheet_name}', sep=';')
        chord_array = chord_sheet['Real Chord [m]'].to_numpy()
        self._chord = scale_array(chord_array, self._n_step)
        return self._chord

    @property
    def cm(self, cm_sheet_name='cm_exemple.csv'):
        '''Read cm input along span from an .csv file.

        Paramters
        ---------
        cm_sheet_name: str
            .csv file name in wich the cm is stored. See file
            exemple in data directory for file format.

        Returns
        -------
        cm: list
            chord value alon wing span.
        self: Plane
            Object of the Plane class.
        '''
        cm_sheet = pd.read_csv(f'data/{cm_sheet_name}', sep = ';')
        cm_array = cm_sheet['cm ac'].to_numpy()
        self._cm = scale_array(cm_array, self._n_step)
        return self._cm



    def __repr__(self):
        repr1 = 'Air craft parameters \n'
        repr2 = f' Span: {self._b}'
        repr3 = f'\n MTOW: {self._MTOW}'
        return repr1 + repr2 + repr3



if __name__ == '__main__':
    b = 2.4
    wing1 = Plane(b)
    print(wing1)