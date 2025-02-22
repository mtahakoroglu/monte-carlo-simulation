<h2>İki Arkadaşın Buluşma Olasılığı 🫂</h2>

<p align="justify">Monte Carlo simülasyonunu daha iyi anlamak için iki arkadaşın buluşma olasılığını hesapladığımız bir başka örneğe bakalım:</p>

<b>Instructor</b>

<p align="justify">Selam ChatGPT! İki arkadaş bir yerde 1 saatlik bir zaman penceresi içinde buluşacaklar. Yâni mesela 14:00-15:00 arasında şehir merkezinde buluşacaklar. Telefonları olmadığından haberleşemiyorlar. Daha önceden "buluşma yerine giden 15dk beklesin, öbürü gelmezse o zaman geri dönsün" diye sözleşmişler. Bu problemi matematiksel olarak çözebilir miyiz?</p>

<b>ChatGPT</b>

<p align="justify">Evet, bu problemi matematiksel olarak çözebiliriz!</p>

<h3>Matematiksel Çözüm 🤔💭📊🧮📝</h3>

<p align="justify">Arkadaşların geliş zamanlarını $X$ ve $Y$ olarak tanımlayalım.</p>

$$X,Y∼U(0,60)$$

<p align="justify">yâni her biri 0 ile 60 dakika arasında eşit olasılıkla herhangi bir zamanda gelebilir. İki arkadaşın buluşabilmesi için geliş zamanları arasındaki fark en fazla 15 dakika olmalıdır:</p>

$$ |X−Y|  \leq 15$$

<p align="justify">Bu, birim karede bir bölgenin alanını hesaplama problemine dönüşüyor.</p>

<h4>Geometrik Yorum<h4>

<p align="justify">İki arkadaşın geliş zamanlarını $(X,Y)$ olarak düşünelim. Bunlar birim karede</p>

$$[0,60]×[0,60]$$

<p align="justify">alanında rastgele dağılım gösterir. Bu kare içinde, 

$$ |X−Y∣ \leq 15$$

<p>koşulunu sağlayan noktaların oluşturduğu bölgeyi inceleyelim:</p>

<b>Intructor</b>

<p align="justify">Peki bu iki arkadaşın buluşma olasılığını Python'da <b>numpy</b> ile rasgele sayı üreteci kullanarak yâni Monte Carlo simülasyonu ile nasıl çözebilirim?</p>

<b>ChatGPT</b>

<p align="justify">Selam! Bu problemi Monte Carlo simülasyonu ile çözebilirsin. Ana fikri şöyle özetleyelim:</p>

<ul>
    <li>İki arkadaşın geliş zamanlarını (0 ile 60 dakika arasında) rastgele seç.</li>
    <li>Buluşma yeri için gelen kişi 15 dakika bekliyor.</li>
    <li>Eğer diğer kişi bu süre içinde gelirse buluşma gerçekleşiyor.</li>
    <li>Bunu binlerce kez simüle ederek buluşma olasılığını hesapla.</li>
</ul>

<p align="justify">Bunu <b>numpy</b> kullanarak şu şekilde kodlayabilirsin:</p>

```
import numpy as np

def bulusma_olasiligi(n_sim=100000):
    # Arkadaşların geliş zamanlarını (0-60 dk) rastgele seç
    arrival_A = np.random.uniform(0, 60, n_sim)
    arrival_B = np.random.uniform(0, 60, n_sim)

    # Mutlak farkları al ve 15 dakikadan küçük olanları say
    bulusanlar = np.abs(arrival_A - arrival_B) <= 15

    # Buluşma olasılığı
    return np.mean(bulusanlar)

# Simülasyonu çalıştır
bulusma_olasiligi()
```


<h3>💻 Python Koduyla Örnek</h3>

<p align="justify">Aşağıdaki kodun koşturulmasını ve yorumunu izlemek için <a href="https://www.youtube.com/watch?v=uY9mXSJkxpw">tıklayınız</a>.</p>

```
import numpy as np
import matplotlib.pyplot as plt

# Simülasyon için nokta sayısı
n = 10000

# [-1, 1] aralığında rastgele x ve y koordinatları üret
x = np.random.uniform(-1, 1, n)
y = np.random.uniform(-1, 1, n)

# Noktaların orijine olan mesafesi (r^2 = x^2 + y^2)
distances = x**2 + y**2

# Çeyrek daire içindeki noktaları belirle (r^2 <= 1)
inside_circle = distances <= 1

# Pi tahmini: 4 * (çeyrek daire içindeki noktalar / toplam noktalar)
pi_estimate = 4 * np.sum(inside_circle) / n

print(f"Tahmini Pi: {pi_estimate:.4f}")

# Noktaları görselleştir
plt.figure(figsize=(6,6))
plt.scatter(x[inside_circle], y[inside_circle], color='green', s=1, label='Dairenin İçindeki Noktalar')
plt.scatter(x[~inside_circle], y[~inside_circle], color='red', s=1, label='Dairenin Dışındaki Noktalar')
circle = plt.Circle((0, 0), 1, edgecolor='blue', fill=False, linewidth=2, label='Çeyrek Daire')
plt.gca().add_patch(circle)
plt.title(f"MCS ile Pi sayısı tahmini: {pi_estimate:.4f} | n = {n}")
plt.xlabel("x")
plt.ylabel("y")
plt.axis('equal')
plt.legend()
plt.axis('tight')
plt.tight_layout()
plt.savefig("pi-estimation.png", dpi=300)
plt.show()
```

<h3>🧪 Kodun Çalışma Mantığı:</h3>
<ul>
    <li><b>n</b> kadar rastgele nokta üretilir.</li>
    <li>Her noktanın orijine uzaklığı hesaplanır.</li>
    <li>Uzaklığı 1 veya daha az olan noktalar dairenin içindedir.</li>
    <li>İçerideki nokta oranı ile 𝞹 tahmini yapılır.</li>
    <li>Görselde içteki noktalar yeşil, dıştaki noktalar kırmızı olarak gösterilir.</li>
</ul>

<img src="pi-estimation.png" alt="monte carlo simülasyonu ile pi sayısı tahmini" width="500" height=auto>

<h3>Referanslar</h3>
<p align="justify">[1] https://www.mehmetalikucuk.com/genel/kare-daire-olasilik-ve-pi-sayisi/</p>