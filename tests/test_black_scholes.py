import pytest
from src.black_scholes import bs_call, bs_put
def test_put_call_parity():
    S0, K, T, r, sigma = 100, 100, 1.0, 0.05, 0.2
    c = bs_call(S0, K, T, r, sigma)
    p = bs_put(S0, K, T, r, sigma)
    assert c - p == pytest.approx(S0 - K * 2.718281828 ** (-r * T), abs=1e-8)

def test_expiry_limit():
    assert bs_call(120, 100, 1e-6, 0.05, 0.2) == pytest.approx(20, abs=0.05)
    assert bs_call(80, 100, 1e-6, 0.05, 0.2) == pytest.approx(0, abs=0.05)

def test_atm_price_reference():
    assert bs_call(100, 100, 1.0, 0.05, 0.2) == pytest.approx(10.4506, abs=1e-3)