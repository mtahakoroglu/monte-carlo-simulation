import numpy as np
import matplotlib.pyplot as plt

# Simülasyon için nokta sayısı
n_sim = 500

# Rastgele geliş zamanları (0-60 dk)
arrival_A = np.random.uniform(0, 60, n_sim)
arrival_B = np.random.uniform(0, 60, n_sim)

# Buluşma sağlanan noktalar (mavi) ve sağlanamayanlar (kırmızı)
meet_condition = np.abs(arrival_A - arrival_B) <= 15

# Grafiği çiz
plt.figure(figsize=(6,6))
plt.scatter(arrival_A[meet_condition], arrival_B[meet_condition], color='blue', s=5, label="Buluştu (|X-Y| ≤ 15)")
plt.scatter(arrival_A[~meet_condition], arrival_B[~meet_condition], color='red', s=5, label="Buluşamadı (|X-Y| > 15)")

# Paralel doğrular
x = np.linspace(0, 60, 100)
plt.plot(x, x + 15, 'k--')  # Üst sınır: Y = X + 15
plt.plot(x, x - 15, 'k--')  # Alt sınır: Y = X - 15

# Eksenler ve ayarlar
plt.xlim(0, 60)
plt.ylim(0, 60)
plt.xlabel("Arkadaş A'nın Geliş Zamanı (dakika)")
plt.ylabel("Arkadaş B'nin Geliş Zamanı (dakika)")
plt.title(f"Arkadaşların Buluşma Olasılığı {sum(meet_condition)}/{n_sim}={np.mean(meet_condition)}") # sum(meet_condition)/n_sim
plt.legend()
plt.grid(True, linestyle='--')
plt.tight_layout()
plt.savefig(f"meeting_plot_n_{n_sim}.png", dpi=600)
plt.show()