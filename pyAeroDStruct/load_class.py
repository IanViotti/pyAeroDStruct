'''Module to read wing loads'''

import os
import sys

import pandas as pd
import scipy.integrate as it

from .utils import scale_array

class Load():
    def __init__(self, plane):
        self._plane = plane
        self._n_step = plane._n_step
        self._y = plane._y
        self._lift = None
        self._V = None
        self._M = None
    
    
    def read_lift(self, load_sheet_name = 'lift_exemple.csv'):
        '''Read lift distribution along span from an .csv file.

            Paramters
            ---------
            lift_sheet_name: str
                .csv file name in wich the lift is stored. See file
                exemple in data directory for file format.

            Returns
            -------
            _lift: np.ndarray
                lift value along wing span.
            self: Load
                Object of the Load class.
            '''
        lift_sheet = pd.read_csv(f'data/load_dir/{load_sheet_name}', sep=';')
        chord_array = lift_sheet['Lift Load[N/m]'].to_numpy()
        self._lift = scale_array(chord_array, self._n_step)
        return self._lift

    def stender_lift(self, MTOW):
        '''Calculates lift distribution based on Stender method.
            This method is a simplification of lift distribution that
            can be used in preliminary project for low AR wings.

            Paramters
            ---------
            MTOW: float
                Maximum take-off weight of the plane.

            Returns
            -------
            _lift_stender: np.ndarray
                lift value along wing span.
            self: Load
                Object of the Load class.
            '''
        # To be implemented
        pass
    
    def V(self, wingtip_shear_force = 0):
        '''Calculates shear force along wing.
            Shear force is calculated by integrating lift
            from wingtip to wingroot.

            Paramters
            ---------
            wingtip_shear_force: float, optional
                Forces acting on wing tip due to wingtip devices.

            Returns
            -------
            _V: np.ndarray
                Shear force value along wing span.
            self: Load
                Object of the Load class.
            '''
        y = self._y
        lift = self._lift[::-1]
        self._V = -it.cumtrapz(lift, y, initial = -wingtip_shear_force)[::-1]
        return self._V

    def M(self, wingtip_bending_moment = 0):
        '''Calculates bending moment along wing.
            Bending moment is calculated by integrating 
            shear force from wingtip to wingroot. 

            Paramters
            ---------
            wingtip_bending_moment: float, optional
                Bending moment acting on wingtip due to wingtip devices.

            Returns
            -------
            M: np.ndarray
                Bending moment value alon wing span.
            self: Load
                Object of the Load class.
            '''
        y = self._y
        V = self._V[::-1]
        self._M = it.cumtrapz(V, y, initial = -wingtip_bending_moment)[::-1]
        return self._M

    def __repr__(self):
        string = 'To implement'
        return string

if __name__ == '__main__':
    load1 = Load.read_load('loads_exemple.csv')
    print('Load:')
    print(load1)