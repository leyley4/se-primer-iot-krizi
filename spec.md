**Problem**
Hastane yoğun bakım ünitesindeki IoT yaşam destek cihazlarını izleyen yerel ağa fidye yazılımı (ransomware) sızdı. Sistem verileri şifrelemeye başladı ve nöbetçi mühendis olarak hastaların hayati verilerini korumak için acil kararlar alman gerekiyor.

**Kapsam Dışı**
* Kullanıcı hesabı oluşturma ve giriş işlemleri
* Kriz sonrasını anlatan ikinci bölüm
* Gerçek hasta verisi kullanımı
* Native mobil uygulama geliştirme

**Kabul Örnekleri**
1. Giriş ekranında oyuncu seviyesi seçildiğinde (örneğin "Deneyimli"), anlatı buna uyum sağlamalı ve 60 saniyelik süre baskısı devreye girmelidir.
2. Her karar aşamasından sonra "ne oldu, neden oldu" bilgisi ekranda gösterilmelidir.
3. AI Tutor, kullanıcı bir seçim yaptığında doğrudan teknik cevabı söylemek yerine ipucu veren Sokratik sorular sormalıdır (Örn: "Ağı fiziksel olarak kesersen cihazların kendi arasındaki senkronizasyonu nasıl sağlanacak?").
4. 1 sağlık senaryosu üzerinden tam 3 karar aşaması sunulmalı ve bu kararların kombinasyonuna göre 2 farklı sondan (İyi veya Kötü) birine ulaşılmalıdır.
5. Kullanıcı "Yeni başladım" seçeneğini işaretlerse, her kararda AI Tutor tarafından yönlendirici ekstra ipuçları görünür olmalıdır.

**Akış Şeması**
* **Başlangıç:** 03:00, Yoğun bakım IoT sensör ağına fidye yazılımı sızdı. 40 cihazın verisi risk altında.
* **Karar 1 - İzolasyon:** 
  * A) Ana şalterden IoT ağının dış dünya ile bağlantısını fiziksel olarak kes.
  * B) Sistemi hızlıca MSSQL yedeğine geçir.
* **Karar 2 - Müdahale:** 
  * A) Zararlı yazılımı canlı sistemde izole etmeye çalış.
  * B) Cihazları manuel moda alıp tüm otomatik veri akışını durdur.
* **Karar 3 - Veri Kurtarma (KVKK Riski):** 
  * A) Hasta loglarını hızlı analiz için geçici olarak bulut API'ye aktar. 
  * B) Sadece yerel şifreli logları cihaz üzerinde (edge) analiz et.
* **Son A (İyi):** Sistem güvenli, cihazlar manuel de olsa çalışıyor, KVKK ihlali yok.
* **Son B (Kötü):** Cihazlar kilitlendi, hasta verileri şifrelendi veya buluta aktarılırken dışarı sızdı.
