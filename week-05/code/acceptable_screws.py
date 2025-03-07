import numpy as np

# Monte Carlo simülasyonu
n = 100000  # Örnek sayısı
vidalar = np.random.normal(loc=5, scale=0.1, size=n)

# Kabul edilen vidaların oranını hesapla
kabul_edilen = np.sum((vidalar >= 4.9) & (vidalar <= 5.1)) / n

print(f"Kabul edilen vida oranı: {kabul_edilen:.4f}")
