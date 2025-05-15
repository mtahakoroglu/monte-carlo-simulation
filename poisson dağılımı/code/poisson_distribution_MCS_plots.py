import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import poisson

# Parametreler
lambda_ = 4
num_trials = 100_000
max_k = 15  # Görselleştirme için k aralığı

# PMF değerleri (Teorik)
k_vals = np.arange(0, max_k + 1)
pmf_vals = poisson.pmf(k_vals, mu=lambda_)

# Monte Carlo simülasyonu
samples = np.random.poisson(lambda_, size=num_trials)
counts, bins = np.histogram(samples, bins=np.arange(0, max_k+2), density=True)

# Grafik
plt.figure(figsize=(10, 6))
plt.bar(k_vals-0.2, pmf_vals, width=0.4, label='Teorik PMF', color='skyblue')
plt.bar(k_vals+0.2, counts, width=0.4, label='Monte Carlo Histogram', color='salmon', alpha=0.7)

plt.xlabel("Çağrı Sayısı (k)")
plt.ylabel("Olasılık")
plt.title(f"Örnek sayısı n={num_trials} için Poisson Dağılımı: λ = {lambda_}")
plt.legend()
plt.grid(True)
plt.savefig("poisson_distribution_MCS_plots.png", dpi=300, bbox_inches='tight')
plt.show()