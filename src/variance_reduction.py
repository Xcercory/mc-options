import numpy as np

def mc_call_antithetic(S0, K, T, r, sigma, n_paths=100_000, seed=42) -> tuple[float, float]:
    """Антитетические переменные: используем Z и -Z."""
    rng = np.random.default_rng(seed)
    n_half = n_paths // 2
    Z = rng.standard_normal(n_half)
    
    # Симулируем две траектории для каждого Z
    ST1 = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)
    ST2 = S0 * np.exp((r - 0.5 * sigma**2) * T - sigma * np.sqrt(T) * Z)
    
    payoff1 = np.maximum(ST1 - K, 0.0)
    payoff2 = np.maximum(ST2 - K, 0.0)
    
    # Усредняем внутри пар и дисконтируем
    avg_payoff = 0.5 * (payoff1 + payoff2)
    discounted = np.exp(-r * T) * avg_payoff
    
    price = float(np.mean(discounted))
    se = float(np.std(discounted, ddof=1) / np.sqrt(n_half))
    return price, se

def mc_call_control_variate(S0, K, T, r, sigma, n_paths=100_000, seed=42) -> tuple[float, float]:
    """Контрольные вариаты: используем S_T как контрольную переменную."""
    rng = np.random.default_rng(seed)
    Z = rng.standard_normal(n_paths)
    
    ST = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)
    payoff = np.maximum(ST - K, 0.0)
    discounted = np.exp(-r * T) * payoff
    
    # Известное мат. ожидание S_T для GBM
    E_ST = S0 * np.exp(r * T)
    
    # Считаем оптимальный коэффициент корректировки
    cov_matrix = np.cov(discounted, ST)
    c_star = cov_matrix[0, 1] / cov_matrix[1, 1]
    
    # Скорректированная выплата
    adjusted_payoff = discounted - c_star * (ST - E_ST)
    
    price = float(np.mean(adjusted_payoff))
    se = float(np.std(adjusted_payoff, ddof=1) / np.sqrt(n_paths))
    return price, se