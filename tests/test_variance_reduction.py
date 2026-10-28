from src.black_scholes import bs_call
from src.mc_pricer import mc_european_call
from src.variance_reduction import mc_call_antithetic, mc_call_control_variate

def test_variance_reduction_is_better():
    S0, K, T, r, sigma = 100, 100, 1.0, 0.05, 0.2
    N = 10_000
    
    # 1. Обычный MC
    _, se_plain = mc_european_call(S0, K, T, r, sigma, n_paths=N)
    
    # 2. Антитетика
    price_anti, se_anti = mc_call_antithetic(S0, K, T, r, sigma, n_paths=N)
    
    # 3. Контрольные вариаты
    price_cv, se_cv = mc_call_control_variate(S0, K, T, r, sigma, n_paths=N)
    
    # Проверяем, что цены не смещены (близки к BS)
    bs_price = bs_call(S0, K, T, r, sigma)
    assert abs(price_anti - bs_price) < 4 * se_anti
    assert abs(price_cv - bs_price) < 4 * se_cv
    
    # Проверяем, что стандартная ошибка уменьшилась
    assert se_anti < se_plain
    assert se_cv < se_plain