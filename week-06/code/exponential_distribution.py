import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def exponential_pdf(x, lambd):
    return lambd * np.exp(-lambd * x)

# Parametreler
lambd = 1  # lambda (oran parametresi)
n_values = [100, 1000, 10000, 100000]  # Farklı örnek büyüklükleri
x_vals = np.linspace(0, 8, 1000)  # pdf için x değerleri

fig, axes = plt.subplots(2, 2, figsize=(12, 10))  # 2x2 subplot
axes = axes.flatten()

for i, n in enumerate(n_values):
    samples = np.random.exponential(scale=1/lambd, size=n)  # Monte Carlo örnekleri
    
    # Histogram
    sns.histplot(samples, bins=50, kde=False, stat='density', color='b', alpha=0.6, ax=axes[i])
    
    # Teorik PDF çizimi
    axes[i].plot(x_vals, exponential_pdf(x_vals, lambd), 'r', lw=2, label='Teorik PDF')
    
    # Grafik başlığı ve etiketler
    axes[i].set_title(f'n = {n}')
    axes[i].set_xlabel('x')
    axes[i].set_ylabel('Olasılık Yoğunluğu')
    axes[i].legend()

plt.suptitle('Monte Carlo Simülasyonu vs Teorik Üstel Dağılım', fontsize=14)
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
