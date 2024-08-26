import numpy as np


def differentiate(u, dt):
    N_t = len(u)
    d_u = np.zeros(N_t)
    
    # Boundaries 
    d_u[0] = (u[1] - u[0]) / dt
    d_u[-1] = (u[-1] - u[-2]) / dt
    
    # Middle
    for t_i in range(1, N_t-1):
        d_u[t_i] = (u[t_i + 1] - u[t_i - 1]) / (2*dt)
        
    return d_u

def differentiate_vector(u, dt):
    d_u = np.zeros(len(u))
    d_u[0] = d_u[0] = (u[1] - u[0]) / dt
    d_u[-1] = (u[-1] - u[-2]) / dt
    d_u[1:-1] = (u[2:] - u[0:-2]) / (2*dt)
    
    return d_u

def test_differentiate():
    t = np.linspace(0, 1, 10)
    dt = t[1] - t[0]
    u = t**2
    du1 = differentiate(u, dt)
    du2 = differentiate_vector(u, dt)
    assert np.allclose(du1, du2)

if __name__ == '__main__':
    test_differentiate()
    