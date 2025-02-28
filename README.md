<h2>Monte Carlo Simülasyonu</h2>

<p align="justify">ChatGPT'ye aşağıdaki soruyu soralım.</p>

<b>Instructor</b>

<p align="justify">Selam ChatGPT, Monte Carlo simülasyonu nedir? 
    Bana bu konu hakkında bilgi verebilir misin? Python kodu ile 
    örnek bir Monte Carlo simülasyonu gösterebilir misin?</p>

<b>ChatGPT</b>

<p align="justify">Selam! 😊 Monte Carlo simülasyonu, belirsizliğin 
veya karmaşıklığın olduğu problemlerin çözümünde rastgele örnekleme 
kullanarak sonuçların olasılık dağılımını tahmin etmeye yarayan bir 
yöntemdir. Bu yöntem özellikle matematik, finans, mühendislik ve 
fizik gibi alanlarda kullanılır.</p>

<h3>📊 Monte Carlo Simülasyonu Ne Yapar?</h3>
<ul>
    <li>Karmaşık sistemleri modellemek için rastgele sayı üretir.</li>
    <li>Çok sayıda rastgele örnekleme ile beklenen sonuçları tahmin eder.</li>
    <li>Belirli bir sonucun olasılığını veya ortalama değerini belirlemek için kullanılır.</li>
</ul>

<h3>💻 Nasıl Monte Carlo Simülasyonu Yapacağız?</h3>
<p align="justify">Bilgisayarların işlemcilerinde (cpu veya gpu) sayıcılar (counter) veya zamanlayıcılar (timer) denilen birimler vardır. Burada rasgele sayı üreteci (random number generator) yardımıyla bu simülasyonlar yapılabilir. Bütün programlama dilleriyle rasgele sayı üretilebilir ancak biz burada <b>Python</b>'da <b>numpy</b> paketinin <b>random</b> sınıfında tanımlı <b>uniform()</b>, <b>randint()</b>, <b>shuffle()</b>, <i>vb.</i> gibi fonksiyonları kullanarak rasgele sayı üretecek ve böylece Monte Carlo simülasyonları yapacağız. Ayrıca uygun olan bazı problemlerde sonuçları <b>matplotlib</b> paketi ile görselleştireceğiz.</p>

<p align="justify"><a href="https://github.com/mtahakoroglu/monte-carlo-simulation/tree/main/week-01">Hafta 1: 📝 Pi Sayısını Tahmin Etme</a></p>
<p align="justify"><a href="https://github.com/mtahakoroglu/monte-carlo-simulation/tree/main/week-02">Hafta 2: 🫂 İki arkadaşın buluşma olasılığı</a></p>
<p align="justify"><a href="https://github.com/mtahakoroglu/monte-carlo-simulation/tree/main/week-03">Hafta 3: 🧑‍🤝‍🧑 İki kardeşin yanyana gelme olasılığı</a></p>
<p align="justify"><a href="https://github.com/mtahakoroglu/monte-carlo-simulation/tree/main/week-03">Hafta 4: 💻 Uygulama (LAB)</a></p>