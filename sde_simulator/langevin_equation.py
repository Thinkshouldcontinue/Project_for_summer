import numpy as np
import matplotlib.pyplot as plt

def langevin_eq(sigma, mu, tau, dt, total_time, num_sample_path):
    num_time_step = int(total_time / dt)
    sigma_bis = sigma * np.sqrt(2.0/ tau)
    sqrtdt = np.sqrt(dt)
    X = np.zeros((num_sample_path, num_time_step))
    for i in range(1, num_time_step):
        X[:, i] =  X[:, i-1] + dt*(-(X[:,i-1] - mu) / tau) + sigma_bis * sqrtdt * np.random.randn(num_sample_path)
    return X



