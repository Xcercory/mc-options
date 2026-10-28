from src.black_scholes import bs_call
from src.mc_pricer import mc_european_call


def test_mc_converges_to_bs():
    S0, K, T, r, sigma = 100, 100, 1.0, 0.05, 0.2
    
    bs_price = bs_call(S0, K, T, r, sigma)
    mc_price, mc_se = mc_european_call(S0, K, T, r, sigma, n_paths=100_000)
    
    # Цена MC не должна отличаться от BS больше, чем на 3 стандартные ошибки
    assert abs(mc_price - bs_price) < 3 * mc_se