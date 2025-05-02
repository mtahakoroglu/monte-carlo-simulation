import numpy as np
import math

N = 10_000  # Simülasyon sayısı
p, k, n = 0.7, 3, 5 # Serbest atış başarı oranı, başarı sayısı, deneme sayısı

# üç serbest atışı sayı yapma olasılığını Binom dağılımı ile hesapla
prob = math.comb(n, k) * p**k * (1 - p)**(n - k)
print(f"P(X = {3}) = {prob:.5f}")
# n=5 atışlık denemeler
shots = np.random.rand(N, n) < p  # True = başarılı
success_counts = np.sum(shots, axis=1)
# Kaçında tam k=3 başarı var?
prob_sim = np.mean(success_counts == k)
print(f"Monte Carlo P({k} başarılı) ≈ {prob_sim:.5f}")

# 5 atıştan 4'ünü yapma olasılığını Binom dağılımı ile hesapla
k = 4
prob = math.comb(n, k) * p**k * (1 - p)**(n - k)
print(f"P(X = {4}) = {prob:.5f}")
# n=5 atışlık denemeler
shots = np.random.rand(N, n) < p  # True = başarılı
success_counts = np.sum(shots, axis=1)
# Kaçında tam k=4 başarı var?
prob_sim = np.mean(success_counts == k)
print(f"Monte Carlo P({k} başarılı) ≈ {prob_sim:.5f}")

# 5 atıştan en az üçünü yapma olasılığını Binom dağılımı ile hesapla
k = 3
prob = sum(math.comb(n, i) * p**i * (1 - p)**(n - i) for i in range(k, n + 1))
print(f"P(X ≥ {k}) = {prob:.5f}")
# n=5 atışlık denemeler
shots = np.random.rand(N, n) < p  # True = başarılı
success_counts = np.sum(shots, axis=1)
# Kaçında en az k=3 başarı var?
prob_sim = np.mean(success_counts >= k)
print(f"Monte Carlo P({k} veya daha fazla başarılı) ≈ {prob_sim:.5f}")