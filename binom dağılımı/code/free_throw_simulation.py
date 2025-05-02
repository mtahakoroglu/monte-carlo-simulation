import numpy as np
import math

N = 10_000  # Simülasyon sayısı
p, k, n = 0.7, 3, 5

# üç serbest atışı sayı yapma olasılığı
# Binom dağılımı ile hesapla
prob = math.comb(n, k) * p**k * (1 - p)**(n - k)
print(f"P(X = {3}) = {prob:.5f}")
# 5 atışlık denemeler
shots = np.random.rand(N, n) < p  # True = başarılı
success_counts = np.sum(shots, axis=1)
# Kaçında tam 3 başarı var?
prob_sim = np.mean(success_counts == 3)
print(f"Monte Carlo P(3 başarılı) ≈ {prob_sim:.5f}")
# dört serbest atışı sayı yapma olasılığı
k = 4
prob = math.comb(n, k) * p**k * (1 - p)**(n - k)
print(f"P(X = {k}) = {prob:.5f}")
# 5 atışlık denemeler
shots = np.random.rand(N, n) < p  # True = başarılı
success_counts = np.sum(shots, axis=1)
# Kaçında tam 4 başarı var?
prob_sim = np.mean(success_counts == k)
print(f"Monte Carlo P(4 başarılı) ≈ {prob_sim:.5f}")
# beş serbest atışı sayı yapma olasılığı
k = 5
prob = math.comb(n, k) * p**k * (1 - p)**(n - k)
print(f"P(X = {k}) = {prob:.5f}")
# 5 atışlık denemeler
shots = np.random.rand(N, n) < p  # True = başarılı
success_counts = np.sum(shots, axis=1)
# Kaçında tam 5 başarı var?
prob_sim = np.mean(success_counts == k)
print(f"Monte Carlo P(5 başarılı) ≈ {prob_sim:.5f}")
# en az üç serbest atışı sayı yapma olasılığı
k = 3
prob = math.comb(n,3)*p**3*(1-p)**2 + math.comb(n,4)*p**4*(1-p)**1 + math.comb(n,5)*p**5*(1-p)**0
# prob = 1 - stats.binom.cdf(k - 1, n, p)
print(f"P(X ≥ {k}) = {prob:.5f}")
# 5 atışlık denemeler
shots = np.random.rand(N, n) < p  # True = başarılı
success_counts = np.sum(shots, axis=1)
# Kaçında en az 3 başarı var?
prob_sim = np.mean(success_counts >= k)
print(f"Monte Carlo P(≥ {k} başarılı) ≈ {prob_sim:.5f}")