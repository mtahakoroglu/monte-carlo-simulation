import numpy as np
import matplotlib.pyplot as plt

# Simülasyon için nokta sayısı
num_points = 10000

# [-1, 1] aralığında rastgele x ve y koordinatları üret
x = np.random.uniform(-1, 1, num_points)
y = np.random.uniform(-1, 1, num_points)

# Noktaların orijine olan mesafesi (r^2 = x^2 + y^2)
distances = x**2 + y**2

# Çeyrek daire içindeki noktaları belirle (r^2 <= 1)
inside_circle = distances <= 1

# Pi tahmini: 4 * (çeyrek daire içindeki noktalar / toplam noktalar)
pi_estimate = 4 * np.sum(inside_circle) / num_points

print(f"Tahmini Pi: {pi_estimate:.4f}")

# Noktaları görselleştir
plt.figure(figsize=(6,6))
plt.scatter(x[inside_circle], y[inside_circle], color='green', s=1, label='Dairenin İçindeki Noktalar')
plt.scatter(x[~inside_circle], y[~inside_circle], color='red', s=1, label='Dairenin Dışındaki Noktalar')
circle = plt.Circle((0, 0), 1, edgecolor='blue', fill=False, linewidth=2, label='Çeyrek Daire')
plt.gca().add_patch(circle)
plt.title(f"Monte Carlo ile Pi Tahmini: {pi_estimate:.4f}")
plt.xlabel("x")
plt.ylabel("y")
plt.axis('equal')
plt.legend()
plt.axis('tight')
plt.tight_layout()
plt.savefig("pi_estimation.png", dpi=600)
plt.show()
