import numpy as np

# Monte Carlo simülasyonu
num_samples = 100000  # Örnek sayısı
vidalar = np.random.normal(loc=5, scale=0.1, size=num_samples)

# Kabul edilen vidaların oranını hesapla
kabul_edilen = np.sum((vidalar >= 4.9) & (vidalar <= 5.1)) / num_samples

print(f"Kabul edilen vida oranı: {kabul_edilen:.4f}")
