import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.integrate import quad

# Üstel dağılım fonksiyonları
def exponential_pdf(x, lambd):
    return lambd * np.exp(-lambd * x)

def exponential_cdf(x, lambd):
    return 1 - np.exp(-lambd * x)

# Parametreler
lambd = 0.5  # Lambda (oran parametresi)
n = 100000  # Örnek büyüklüğü
x_vals = np.linspace(0, 15, 1000)  # PDF için x ekseni
x_fill = np.linspace(0, 3, 1000)  # Gölgelenecek alan

# Monte Carlo Simülasyonu
samples = np.random.exponential(scale=1/lambd, size=n)

# Teorik ve Empirik Olasılık Hesaplama
P_X_less_3_theoretical = exponential_cdf(3, lambd)
P_X_less_3_empirical = np.mean(samples < 3)

# Histogram ve PDF çizimi
plt.figure(figsize=(8, 6))
sns.histplot(samples, bins=50, kde=True, stat='density', color='b', alpha=0.6, label='Monte Carlo Histogram')
plt.plot(x_vals, exponential_pdf(x_vals, lambd), 'r', lw=2, label='Teorik PDF')
plt.fill_between(x_fill, exponential_pdf(x_fill, lambd), alpha=0.3, color='g', label='P(X < 3)')
plt.xlabel('Bekleme Süresi (dakika)', fontsize=16)
plt.ylabel('Olasılık Yoğunluk Fonksiyonu (PDF)', fontsize=16)
plt.title(f'Üstel Dağılım: P(X < 3)\nTeorik: {P_X_less_3_theoretical:.3f}, Empirik (n={n}): {P_X_less_3_empirical:.3f}', fontsize=16)
plt.grid(True, linestyle='--')
plt.tight_layout()
# plt.subplots_adjust(left=0.11)  # Increase left margin specifically
plt.xticks(fontsize=16)  # Makes x-axis numbers bigger
plt.yticks(fontsize=16)  # Makes y-axis numbers bigger
plt.legend(fontsize=14)
plt.savefig(f"../figure/phone_call_wait_time_{n}.png", dpi=500)
plt.show()

# Matematiksel Olasılık Hesabı (Integral ile Doğrulama)
def exponential_integral(x, lambd):
    return quad(lambda t: lambd * np.exp(-lambd * t), 0, x)[0]

theoretical_integral = exponential_integral(3, lambd)
print(f"Teorik P(X < 3) (integral ile hesaplanan): {theoretical_integral:.3f}")
