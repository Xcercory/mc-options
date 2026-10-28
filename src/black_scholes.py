import numpy as np
from scipy.stats import norm
def bs_call(S0: float, K: float, T: float, r: float, sigma: float) -> float:
    #Цена европейского call по Блэку-Шоулзу.#
    d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
def bs_put(S0: float, K: float, T: float, r: float, sigma: float) -> float:
    #Цена европейского put по Блэку-Шоулзу.#
    d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return K * np.exp(-r * T) * norm.cdf(-d2) - S0 * norm.cdf(-d1)