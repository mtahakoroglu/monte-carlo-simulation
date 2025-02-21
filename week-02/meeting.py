import numpy as np

def bulusma_olasiligi(n_sim=10000):
    # Arkadaşların geliş zamanlarını (0-60 dk) rastgele seç
    arrival_A = np.random.uniform(0, 60, n_sim)
    arrival_B = np.random.uniform(0, 60, n_sim)

    # Mutlak farkları al ve 15 dakikadan küçük olanları say
    bulusanlar = np.abs(arrival_A - arrival_B) <= 15

    # Buluşma olasılığı
    return sum(bulusanlar)/n_sim

# Simülasyonu çalıştır
print(bulusma_olasiligi())
