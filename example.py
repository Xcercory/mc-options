from src.black_scholes import bs_call
from src.mc_pricer import mc_european_call
from src.variance_reduction import mc_call_control_variate

# Параметры для акции Apple 
S0 = 180.0   # Текущая цена
K = 185.0    # Страйк (цена исполнения)
T = 0.5      # Полгода до экспирации (0.5 лет)
r = 0.05     # Безрисковая ставка 5%
sigma = 0.25 # Волатильность 25%

print("--- Аналитический расчет (Black-Scholes) ---")
bs_price = bs_call(S0, K, T, r, sigma)
print(f"Цена по формуле: ${bs_price:.2f}")

print("\n--- Обычный Монте-Карло (100,000 путей) ---")
mc_price, mc_se = mc_european_call(S0, K, T, r, sigma, n_paths=100_000)
print(f"Цена MC: ${mc_price:.2f} (плюс/минус ${mc_se:.2f})")

print("\n--- Продвинутый Монте-Карло (Control Variate) ---")
cv_price, cv_se = mc_call_control_variate(S0, K, T, r, sigma, n_paths=100_000)
print(f"Цена MC + CV: ${cv_price:.2f} (плюс/минус ${cv_se:.2f})")
print(f"Мы сэкономили вычислений, уменьшив погрешность в {mc_se/cv_se:.1f} раз!")