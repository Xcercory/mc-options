import numpy as np
def mc_european_call(
    S0: float, K: float, T: float, r: float, sigma: float, 
    n_paths: int = 100_000, seed: int = 42
) -> tuple[float, float]:
    """
    Оценка цены европейского call опциона методом Монте-Карло (модель GBM).
    Возвращает кортеж: (цена опциона, стандартная ошибка).
    """
    rng = np.random.default_rng(seed)
    # 1. Генерируем стандартные нормальные случайные числа Z
    Z = rng.standard_normal(n_paths)
    # 2. Симулируем конечную цену актива S_T по формуле GBM
    ST = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)
    # 3. Считаем payoff (выплату) для call опциона
    payoff = np.maximum(ST - K, 0.0)
    # 4. Дисконтируем к сегодняшнему дню
    discounted_payoff = np.exp(-r * T) * payoff
    # 5. Считаем среднее (цену) и стандартную ошибку (SE)
    price = float(np.mean(discounted_payoff))
    se = float(np.std(discounted_payoff, ddof=1) / np.sqrt(n_paths))
    return price, se