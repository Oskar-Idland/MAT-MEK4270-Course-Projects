import numpy as np


def mesh_function(f, t):
    N_t = len(t)
    y = np.zeros(N_t)
    for i in range(N_t):
        y[i] = f(t[i])
    
    return y

def func(t):
    if 0 <= t and t <= 3:
        return np.exp(-t)
    elif 3 < t and t <= 4:
        return np.exp(-3*t) 

def test_mesh_function():
    t = np.array([1, 2, 3, 4])
    f = np.array([np.exp(-1), np.exp(-2), np.exp(-3), np.exp(-12)])
    fun = mesh_function(func, t)
    assert np.allclose(fun, f)
