import numpy as np

# Parametreler
lambda_ = 4
k = 6
num_trials = 1_000

# Poisson örnekleri üret
samples = np.random.poisson(lam=lambda_, size=num_trials)

# K = 6 olanları say
estimated_prob = np.sum(samples == k) / num_trials
print(f"Simülasyonla Yaklaşık Olasılık: P(X=6) = {estimated_prob:.4f}")