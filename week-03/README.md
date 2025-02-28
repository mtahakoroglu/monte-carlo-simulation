<h2>Kardeşlerin Yan Yana Gelme Olasılığı 🫂</h2>

<p align="justify">Şu ana kadar baktığımız Monte Carlo simülasyonlarında belli alanlarda rasgele oluşturulan nokta sayılarını oranlayarak çözüme gittik. Burada bu sefer böyle bir oranlama hesabı yapmadan bir Monte Carlo Simülasyonu (MCS) yapalım.</p>

<p align="justify"><b>👨‍🏫 Soru:</b> On arkadaş resim çektirecekler. Arkadaşlardan ikisi kardeş. Resim çekilmeden önce rasgele sıralanıyorlar. Kardeşlerin resimde yan yana gelme olasılığı nedir?</p>

<h3>Matematiksel Çözüm 1 🤔💭📊🧮📝</h3>

<p align="justify">Evet, bu problemi matematiksel olarak çözebiliriz! Daha önce mutlaka bir yerlerde "kaç farklı şekilde sıralanabilirler" gibi soruları görmüşüzdür. Burada on arkadaşın yan yana kaç farklı şekilde poz verebileceğini $10!$ ile hesaplayabiliriz. Bu örneklem uzayda bütün durumları oluşturuyor. Bunlar arasında kardeşlerin yan yana olduğu durumları bulmak için kardeşleri tek kişi gibi düşünelim: O zaman karşımıza $9!$ çıkar. Burada kardeşlerin kendi aralarında değişiklik yapabileceğini de düşünürsek oradan da $2!$ gelecektir. Ayrı ayrı bulduğumuz bu sayıları doğru biçimde oranlarsak matematiksel olarak çözümü elde ederiz.</p>

$$P(Y) = \frac{9!2!}{10!} = 0.2$$

<h3>Matematiksel Çözüm 2 🤔💭📊🧮📝</h3>

<p align="justify">Yine bugüne kadar mutlaka Bayes formülünü duymuşuzdur. Bayes formülünü oluşturan koşullu ve toplam olasılık prensipleriyle bu soruya yaklaşıp çözümü bu yolla da bulabiliriz. Burada kardeşlerden birinin kenara gelmesinin $K$ ile (ve dolayısıyla kenara gelmemesi durumunun $K'$ ile) temsil edildiğini kabul edelim. Ayrıca yan yana gelmelerine de $Y$ diyelim. Yanyana gelme olasılığı $P(Y)$ koşullu olasılıklar ve toplam olasılık yaklaşımıyla aşağıdaki gibi bulunur.</p>

$$P(Y) = P(Y|K)P(K)+P(Y|K')P(K')$$

$$P(Y) = \frac{1}{9}\frac{2}{10}+\frac{2}{9}\frac{8}{10}$$

$$P(Y) = \frac{2}{90}+\frac{16}{90} = \frac{18}{90} = 0.2$$

<p align="justify">Bu ifadelerde geçen $|$ işareti koşullu olasılığı temsil etmektedir. Mesela, $Y|K$ demek ilk kardeş kenara geldiğinde öbür kardeşin onun yanına gelmesini belirtmektedir.</p>

<b>Nümerik Çözüm 💻</b>

<p align="justify">ChatGPT'ye bu problemi verip bize Monte Carlo çözümünü üretmesini istediğimizde, aşağıdaki kodu bize verecektir. Kodda, <b>numpy</b> paketinde yer alan <b>random</b> isimli sınıf ait <b>shuffle</b> fonksiyonunun mânâsı "karıştır" veya daha doğru bir tabirle "(kartları) <b>kar</b>(ıştır)" demektir.</p>

<b>kardesler_yanyana.py</b>

```
import numpy as np

def monte_carlo_simulation(num_trials=100000):
    people = ["K1", "K2"] + list(range(1, 9))  # Kardeşler + 8 kişi
    success_count = 0

    for _ in range(num_trials):
        np.random.shuffle(people)  # Rastgele sırala
        # Kardeşler yan yana mı?
        for i in range(len(people) - 1):
            if (people[i] == "K1" and people[i + 1] == "K2") or (people[i] == "K2" and people[i + 1] == "K1"):
                success_count += 1
                break

    probability = success_count / num_trials
    return probability

# Simülasyonu çalıştır
simulated_probability = monte_carlo_simulation()
print(f"Monte Carlo Simülasyonu Sonucu: {simulated_probability:.4f}")
```