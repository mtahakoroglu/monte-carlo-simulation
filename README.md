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
<p align="justify">Bilgisayarların işlemcilerinde (cpu veya gpu) sayıcılar (counter) veya zamanlayıcılar (timer) denilen birimler vardır. Burada rasgele sayı üreteci (random number generator) yardımıyla bu simülasyonlar yapılabilir. Bütün programlama dilleriyle rasgele sayı üretilebilir ancak biz burada <b>Python</b>'da <b>numpy</b> paketinin <b>random</b> sınıfında tanımlı <b>uniform()</b>, <b>randint()</b>, <b>shuffle()</b>, <b>normal()</b>, <b>exponential()</b>, <b>poisson()</b>, <i>vb.</i> gibi fonksiyonları kullanarak rasgele sayı üretecek ve Monte Carlo simülasyonları yapacağız. Ayrıca uygun olan bazı problemlerde sonuçları <b>matplotlib</b> paketi ile de görselleştireceğiz. Her zaman olmasa bile bazen <b>scipy</b> (Normal ve Poisson dağılımı MCS örneklerinde rasgele sayı üretiminde karşımıza çıktı), <b>seaborn</b> (üstel dağılım MCS örneğinde grafik çizdirmede karşımıza çıktı) gibi paketlere de ihtiyaç duyabilmekteyiz. Bu yüzden onları da yüklemeliyiz.</p>

<p align="justify"><a href="https://github.com/mtahakoroglu/monte-carlo-simulation/tree/main/week-01">📝 Pi Sayısını Tahmin Etme</a> | <a href="https://www.youtube.com/watch?v=uY9mXSJkxpw&list=PLMoe16OQDeeBlOr_C8cCvN_UV7irHupO0&index=2">video</a></p>
<p align="justify"><a href="https://github.com/mtahakoroglu/monte-carlo-simulation/tree/main/week-02">🫂 İki arkadaşın buluşma olasılığı | <a href="https://www.youtube.com/watch?v=8aBywUP7tTM&list=PLMoe16OQDeeBlOr_C8cCvN_UV7irHupO0&index=2">video</a></p>
<p align="justify"><a href="https://github.com/mtahakoroglu/monte-carlo-simulation/tree/main/week-03">🧑‍🤝‍🧑 İki kardeşin yanyana gelme olasılığı</a> | <a href="https://www.youtube.com/watch?v=UgJL_WuztS4">video</a></p>
<p align="justify"><a href="https://github.com/mtahakoroglu/monte-carlo-simulation/tree/main/week-04">💻 Uygulama (LAB)</a></p>
<p align="justify"><a href="https://github.com/mtahakoroglu/monte-carlo-simulation/tree/main/week-05">🔩 Vidaların Kabul Edilebilirlik Aralığı (Normal Dağılım)</a> | <a href="https://www.youtube.com/watch?v=qygabAtODsY">video</a></p>
<p align="justify"><a href="https://github.com/mtahakoroglu/monte-carlo-simulation/tree/main/week-06">☎️ Çağrı Bekleme Süreleri (Üstel Dağılım)</a> | <a href="https://www.youtube.com/watch?v=-0Tr9FeRFF8">video</a></p>
<!--
<p align="justify"><a href="https://github.com/mtahakoroglu/monte-carlo-simulation/tree/main/week-07">📝 Ara Sınav Örneği</a> | <a href="https://www.youtube.com/watch?v=-0Tr9FeRFF8">video</a></p>
-->
<p align="justify"><a href="https://github.com/mtahakoroglu/monte-carlo-simulation/tree/main/binom dağılımı">📐 Alperen Şengün Serbest Atış (Binom Dağılımı)</a> | <a href="https://www.youtube.com/watch?v=iAxJOqpEqNA">video</a></p>
<p align="justify"><a href="https://github.com/mtahakoroglu/monte-carlo-simulation/tree/main/poisson dağılımı">☎️ Çağrı Merkezine Belirli Sayıda Çağrı Gelme İhtimali (Poisson Dağılımı)</a> | <a href="https://www.youtube.com/watch?v=q8mVobkl5ZA">video</a></p>