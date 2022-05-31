import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import UnivariateSpline



def plot_lift(self, x , y):
    plt.plot(x,y)
    return None

def scale_array(array, n_step):  
    old_indices = np.arange(0, len(array))
    new_indices = np.linspace(0, len(array)-1, n_step)
    spl = UnivariateSpline(old_indices, array, k=3, s=0)
    array = spl(new_indices)
    return array


