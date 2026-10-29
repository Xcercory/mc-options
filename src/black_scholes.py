import numpy as np
from scipy.stats import norm
#S0(Spot) - Текущая цена акции (к примеру 100)
#K(Strike) - Цена по которой мы договорились купить бумагу в будущем 
#T(Time) - время до конца контракта в годах (к примеру 1 год)
#r(Rate) - Безрисоквая процентная ставка (к примеру 5%)
#Sigma(Volatility) - Волатильность (наскольо сильно меняется цена акции) чем выше Sigma тем дороже опцион
#d1 - На сколько стандартных отклонений цена акции отличается от точки безубыточности.
#d2 - Это вероятность того что опцион вообще принесет прибыль (то есть цена акции S_T окажется выше страйка K к моменту исполнения )

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