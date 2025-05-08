import math

# Parametreler
lambda_ = 4  # Ortalama çağrı sayısı
k = 6        # Belirli bir çağrı sayısı

# PMF formülü
pmf = (math.exp(-lambda_) * (lambda_ ** k)) / math.factorial(k)
print(f"Teorik Olasılık: P(X={k}) = {pmf:.4f}")