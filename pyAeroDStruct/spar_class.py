import numpy as np

class Spar():
    def __init__(self, i_r, o_r):
        self._i_r = i_r
        self._o_r = o_r
        self._A = None
        self._I = None
        self._taper = None

    def add_tappering(self, type):
        if type == 'continuous':
            pass
        if type == 'discrete':
            pass
        pass 

    def area(self):
        self._A = np.pi*self._o_r**2 - np.pi*self._i_r**2
        return self._A

    def moment_of_inertia(self):
        self._I = np.pi*self._o_r**2/4 - np.pi*self._i_r**4/4
        return self._I
    
    def t_stress(self):
        pass

    def c_stress(self):
        pass

    def avg_s_stress(self):
        pass

    def max_s_stress(self):
        pass

    def __repr__(self):
        pass

if __name__ == '__main__':
    pass