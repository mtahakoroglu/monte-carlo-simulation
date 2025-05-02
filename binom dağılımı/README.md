<h1>BİNOM DAĞILIMI (BINOMIAL DISTRIBUTION)</h1>
<h2>🏀 NBA Basketbolcusu Alperen Şengün'ün Serbest Atış Performansı</h2>

<p align="justify"><b>👨‍🏫 Instructor</b><br>Selam ChatGPT,<br>
Bugüne kadar tekdüze (uniform), normal ve üstel (exponential) dağılımlar için Monte Carlo simülasyonları yaptık. Şimdi <b>binom dağılımını</b> NBA basketbolcusu Alperen Şengün'ün serbest atış performansı üzerinden örnek bir soruyla ele alabilir misin? Mesela, Alperen'in serbest atış başarı yüzdesi p = 0.7 olsun.</p>

<img src="https://wp.clutchpoints.com/wp-content/uploads/2025/01/Rockets-center-Alperen-Sengun-shoots-free-throws.jpg" alt="Alperen Sensun shooting a free throw" width="500" height=auto>

<p align="justify"><b>💻 ChatGPT</b><br>Alperen Şengün 5 serbest atış yapıyor. Her atışın başarılı olma olasılığı p=0.7. Bu 5 atıştan tam olarak 3 tanesini sayıya çevirme (başarma) olasılığı nedir?</p>

<h3>🤔💭🧠 Analitik Çözüm (Binom Formülü) 📊🧮📝📐</h3>

<p align="justify">Binom dağılımının olasılık formülü:</p>

$$P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$$

<p align="justify">Burada:</p>
<ul>
    <li>n = 5 (serbest atış deneme sayısı)</li>
    <li>k = 3 (başarılı serbest atış sayısı)</li>
    <li>p = 0.7 (serbest atış başarı yüzdesi)</li>
</ul>

$$P(X=3) = \binom{5}{3} 0.7^3 (0.3)^{2}$$

<p align="justify">Hesap makinesi yerine aşağıdaki Python kodunu koşturarak cevabı bulabiliriz.</p>

```
import math

p, k, n = 0.7, 3, 5

# Binom dağılımı ile hesapla
prob = math.comb(n,k) * p**k * (1-p)**(n-k)
print(f"P(X = {3}) = {prob:.5f}")
```

<h3>Nümerik Çözüm 💻📊🧮</h3>

<p align="justify">Monte Carlo Simülasyonu için Python kodu şöyle olabilir:</p>

<b>free_throw_simulation.py</b>

```
import numpy as np

N = 10_000  # Simülasyon sayısı
n = 5
p = 0.7

# 10 atışlık denemeler
shots = np.random.rand(N, n) < p  # True = başarılı
success_counts = np.sum(shots, axis=1)

# Kaçında tam 3 başarı var?
prob_sim = np.mean(success_counts == 3)
print(f"Monte Carlo P(3 başarılı) ≈ {prob_sim:.5f}")
```

<p align="justify">Alternatif Sorular</p>

<ul>

<li>P(X = 4): Alperen'in serbest atışlardan tam 4 tanesini atma olasılığı nedir?</li>

<li>P(X = 5): Alperen'in serbest atışların hepsini atma olasılığı nedir?</li>

<li>P(X ≥ 3): Alperen'in serbest atışlardan en az 3 tanesini atma olasılığı nedir?</li>

$$P(X \geq 3) = \sum_{k=3}^n \binom{5}{k} p^k (1-p)^{n-k} = \sum_{k=3}^5 \binom{5}{k} 0.7^k (0.3)^{5-k}$$

$$P(X \geq 3) = \binom{5}{3} 0.7^3 (0.3)^{2} + \binom{5}{4} 0.7^4 (0.3)^{1} + \binom{5}{5} 0.7^5 (0.3)^{0}$$

```
# en az üç serbest atışı sayı yapma olasılığı
k = 3
prob = math.comb(n,3)*p**3*(1-p)**2 + math.comb(n,4)*p**4*(1-p)**1 + math.comb(n,5)*p**5*(1-p)**0
print(f"P(X ≥ {k}) = {prob:.5f}")
# 5 atışlık denemeler
shots = np.random.rand(N, n) < p  # True = başarılı
success_counts = np.sum(shots, axis=1)
# Kaçında en az 3 başarı var?
prob_sim = np.mean(success_counts >= k)
print(f"Monte Carlo P(≥ {k} başarılı) ≈ {prob_sim:.5f}")
```

<li>P(X ≤ 3): Alperen'in serbest atışlardan en fazla 3 tanesini atma olasılığı nedir?</li>

<li>P(2 ≤ X ≤ 4): 2 ile 4 arasında başarılı olma olasılığı nedir?</li>
</ul>