<h1>BİNOM DAĞILIMI (BINOMIAL DISTRIBUTION)</h1>
<h2>🏀 NBA Basketbolcusu Alperen Şengün'ün Serbest Atış Performansı</h2>

<p align="justify"><b>👨‍🏫 Instructor</b><br>Selam ChatGPT,<br>
Bugüne kadar tekdüze (uniform), normal ve üstel (exponential) dağılımlar için Monte Carlo simülasyonları yaptık. Şimdi <b>binom dağılımını</b> NBA basketbolcusu Alperen Şengün'ün serbest atış performansı üzerinden örnek bir soruyla ele alabilir misin? Mesela, Alperen'in serbest atış başarı yüzdesi p = 0.7 olsun.</p>

<img src="https://wp.clutchpoints.com/wp-content/uploads/2025/01/Rockets-center-Alperen-Sengun-shoots-free-throws.jpg" alt="Alperen Sensun shooting a free throw" width="500" height=auto>

<p align="justify"><b>💻 ChatGPT</b><br>Alperen Şengün 5 serbest atış yapıyor. Her atışın başarılı olma olasılığı p=0.7. Bu 5 atıştan tam olarak 5 tanesini sayıya çevirme (başarma) olasılığı nedir?</p>

<h3>🤔💭🧠 Analitik Çözüm (Binom Formülü) 📊🧮📝📐</h3>

<p align="justify">Binom dağılımının olasılık formülü:</p>

$$P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$$

<p align="justify">Burada:</p>
<ul>
    <li>n = 5 (serbest atış deneme sayısı)</li>
    <li>k = 3 (başarılı serbest atış sayısı)</li>
    <li>p = 0.7 (serbest atış başarı yüzdesi)</li>
</ul>

$$P(X=7) = \binom{5}{3} 0.7^3 (0.3)^{2}$$

<p align="justify">Hesap makinesi yerine aşağıdaki Python kodunu koşturarak cevabı bulabiliriz.</p>

```
import scipy.stats as stats

n = 5
p = 0.7
k = 3

# Binom dağılımı ile hesapla
prob = stats.binom.pmf(k, n, p)
print(f"P(X = 7) = {prob:.5f}")
```

<h3>Nümerik Çözüm 💻📊🧮</h3>

<p align="justify">Monte Carlo Simülasyonu Python kodu şöyle olabilir:</p>

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

<li>P(X ≥ 8): En az 8 tanesi başarılı olma olasılığı nedir?</li>

<li>P(X ≤ 5): En fazla 5 tanesi başarılı olma olasılığı nedir?</li>

<li>P(6 ≤ X ≤ 9): 6 ile 9 arasında başarılı olma olasılığı nedir?</li>
</ul>