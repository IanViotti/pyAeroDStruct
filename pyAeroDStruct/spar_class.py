import numpy as np

class Spar():
    def __init__(self, plane):
        
        # Plane parameters initializaton
        self._y = plane.y
        # Geometry proprieties initialization
        self._geometry_prop = []
        # Taper data initialization
        self._taper = []
    	
        self._r_y = []
        self._A_y = []
        self._I1_y = []
        self._I2_y = []
        self._J12_y = []

    def define_geometry(self, **kwargs):
        '''Defines cross section geometry and its geometric proprieties.
        
        Parameters
        ----------
        geometry: string
            Geometry type of the cross sectiob. Hollowed circular, Full circular, 
            D cell and Box are supported.
        radius: int, float
            Outer radius of a circular section. Must be a positive number.
        inner_radius: int, float
            Inner radius of a hollowed ciruclar section. Must be a positive number 
            and inferior to radius.
        
        Returns
        -------
        A: float
            Cross section area.
        I1: float
            Cross section moment of inertia on axis 1 (horizontal).
        I2: float
            Cross section moment of interia on axis 2 (vertical).
        J12: float
            Cross section polar moment of inercia.
        '''

        geometry = kwargs.get('geometry')
  
        if geometry == 'Hollowed circular':           
            r = kwargs.get('radius')
            ir = kwargs.get('inner_radius')
            A = np.pi * r **2 - np.pi* ir ** 2
            I1 = (np.pi * r ** 4 / 4) - (np.pi * ir ** 4 / 4)
            I2 = I1
            J12 = I1 + I2
            geometry_dict= {'r': r, 
                "ir": ir, 
                'A': A, 
                "I1": I1, 
                "I2": I2,   
                "J12": J12
                }
            self._geometry_prop.append(geometry_dict)

        if geometry == 'Full circular':
            r = kwargs.get('radius')
            print(kwargs)
            A = np.pi * r ** 2 
            I1 = (np.pi * r ** 4 / 4)
            I2 = I1
            J12 = I1 + I2
            geometry_dict = {'r': r, 
                'A': A, 
                "I1": I1, 
                "I2": I2,   
                "J12": J12
                }
            self._geometry_prop.append(geometry_dict)

        else:
            return 'To be implemented'

    def add_tappering(self, tapper_type, pos_y, pos_y_end = None, **kwargs):
        '''' Definies a tapparing to the spar. This tapparing 
        can be continuous or discrete.

        Parameters
        ----------
        tapper_type: string
            Type of tappering. Can be continuous or discrete.
        pos_y: float
            Position in y coordinate in wich the tappering happens
            in discrete ones and where it stars in continuous ones.
        pos_y_end: float
            Position in y coordinate where continuous tappering ends.
        **kwags:
            **kwargs used in Spar.define_geometry() function for 
            defined geometry type after tappering. After-tappering 
            geometry type must be the same as the one after if tappering
            type is continuous.
        
        Returns
        -------
        None
        '''
        if tapper_type != 'continuous' and  tapper_type != 'discrete':
            raise ValueError(
                'Please input tapper type as continuous or discrete only'
            )
        elif tapper_type == 'continuous':
            raise NotImplementedError
        elif tapper_type == 'discrete':
            self._taper.append(pos_y)
        
        # Define geometry after tappering
        self.define_geometry(**kwargs)

        return None
    
    def geometry_y(self):
        '''Stores geometry proprieties along y coordinate.

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        
        # Go through each spar section
        section_i = 0
        for y_i in self._y:
            if (section_i < len(self._taper) and 
            y_i > self._taper[section_i] 
            ):
                # Update section number
                section_i += 1  

            # Append geometry proprieties for each section
            self._A_y.append(self._geometry_prop[section_i]['A'])
            self._I1_y.append(self._geometry_prop[section_i]['I1'])
            self._I2_y.append(self._geometry_prop[section_i]['I2'])
            self._J12_y.append(self._geometry_prop[section_i]['J12'])

        return None

    def stress_profile(self, call_plotter = True):
        '''Calculates tensile and shear stress distribution at given 
        cross section.

        Parameters
        ----------
        call_plotter: Boolean
            If call_plotter == True, plots stress distribution at 
            the critical point for each section.

        Returns
        -------
        stress_profile: dict 
            dict containing arrays for z position from neutral axis, 
            sigma_x, sigma_y, tau_xy, sigma_p1, sigma_p2 and tau_max.

        '''
        for section in self._geometry_prop:
            pass

        if plot == True:
            raise NotImplementedError
        pass

    def __repr__(self):
        return 'To be implemented'

if __name__ == '__main__':
    pass