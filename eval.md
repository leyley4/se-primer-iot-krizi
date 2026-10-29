# Eval (Değerlendirme) Raporu - YBÜ IoT Krizi Simülasyonu

Bu raporda AI Tutor'a verilen 20 farklı öğrenci cevabı ve sistemin Sokratik rehberlik başarı oranı elle etiketlenmiştir.

**Toplam Cevap Sayısı:** 20
**Hata Yapan (Cevabı Ele Veren) Tutor Yanıtı:** 4
**Başarı Oranı:** %80
**Hata Oranı:** %20

## Değerlendirme Tablosu

| No | Karar Aşaması | Öğrenci Cevabı | AI Tutor Yanıtı (Özet) | Etiket | Hata Türü |
|---|---|---|---|---|---|
| 1 | 1. İzolasyon | Ağı keseceğim. | "Fiziksel izolasyon sağlandığında, hemşire deskindeki merkezi alarmlar nasıl çalacak?" | Başarılı | - |
| 2 | 1. İzolasyon | B yaparım, veriler önemli. | "MSSQL yedeğine geçmek, enfekte olan 40 cihazın ağdaki yatay yayılımını durduracak mı?" | Başarılı | - |
| 3 | 1. İzolasyon | Fişlerini çekerim. | "Güç kesintisi hastaların solunumunu nasıl etkiler?" | Başarılı | - |
| 4 | 1. İzolasyon | Kabloları kesersek cihazlar manuel çalışır mı? | "Evet, cihazlar manuel hasta başı moduna geçer ve otonom çalışır." | HATA | Cevabı Ele Verdi |
| 5 | 1. İzolasyon | SQL yedeği temizdir, virüs geçmez. | "Veritabanı temiz olsa bile, cihazların bağlı olduğu ağ anahtarındaki zararlı trafiği nasıl izole edeceksin?" | Başarılı | - |
| 6 | 1. İzolasyon | Ağı kesip Wireshark açarım. | "Trafiği dinlemeden önce hastaların anlık takibi için kime haber vermelisin?" | Başarılı | - |
| 7 | 1. İzolasyon | Hemen MSSQL'e geçerim. | "Yanlış karar. Ağ trafiği kesilmediği için fidye yazılımı yayılmaya devam eder." | HATA | Yanlış Yönlendirdi / Cevabı Verdi |
| 8 | 2. Müdahale | Hepsini kapatıp açarım (Hard reboot). | "Cihazları kapatıp açmak RAM'i temizler, ancak bu süre zarfında hastalara verilen yaşam desteği ne olacak?" | Başarılı | - |
| 9 | 2. Müdahale | MAC filtreleme yaparım. | "Kriz anında 40 cihaz arasından enfekte 6 cihazın MAC adresini nasıl hızlıca tespit edeceksin?" | Başarılı | - |
| 10 | 2. Müdahale | Portları kapatırım. | "Portlar kapandığında, sunucudan gelen anlık ilaç dozaj güncellemeleri durursa cihazlar neye göre ilaç verecek?" | Başarılı | - |
| 11 | 2. Müdahale | Fişi çekersem hastalar ölür mü? | "Bunu cihazların batarya kapasitesi ve yeniden başlama (boot) süresi üzerinden nasıl değerlendirirsin?" | Başarılı | - |
| 12 | 2. Müdahale | Sadece 6 cihazı ağdan düşürürüm. | "Doğru, böylece cihazlar son hafızalarındaki konfigürasyonla ilaç vermeye devam ederler." | HATA | Cevabı Ele Verdi |
| 13 | 2. Müdahale | SPAN port ile dinlerim. | "Aynalanan trafikte (SPAN) özellikle hangi protokollerdeki (örn: SMB, ARP) anomalileri arayacaksın?" | Başarılı | - |
| 14 | 2. Müdahale | Hard reboot virüsü siler bence. | "Fidye yazılımı cihazın flash belleğine kendini (persistence) yazmışsa reboot işe yarar mı?" | Başarılı | - |
| 15 | 3. Kurtarma/KVKK | Fidyeyi öderim, uğraşamam. | "Fidyeyi ödemek siber suçluların verileri Dark Web'de satmamasını teknolojik olarak garanti eder mi?" | Başarılı | - |
| 16 | 3. Kurtarma/KVKK | Yedekten dönerim. | "Temiz yedekten dönsen bile, sızdırılan veriler için yasal olarak (KVKK) 72 saat içinde ne yapmalısın?" | Başarılı | - |
| 17 | 3. Kurtarma/KVKK | Ödersem KVKK ceza kesmez. | "Olayın üzerini örtmek ve resmi kurumlara bildirmemek KVKK mevzuatında ağır ihmal suçu sayılmaz mı?" | Başarılı | - |
| 18 | 3. Kurtarma/KVKK | Hava boşluklu yedek temizdir, direkt yüklerim. | "Yedeği canlıya almadan önce içinde uyuyan (dormant) bir zararlı yazılım olmadığını nasıl doğrulayacaksın?" | Başarılı | - |
| 19 | 3. Kurtarma/KVKK | Fidyeyi ödemek yasal suç mu? | "Evet, fidyeyi ödemek suça teşviktir ve veri ihlalini Kurul'a 72 saat içinde bildirmelisiniz." | HATA | Cevabı Ele Verdi |
| 20 | 3. Kurtarma/KVKK | Kimseye söylemeden kendi içimizde çözeriz. | "Sisteme giren adli bilişim (forensics) uzmanları loglardaki silinme ve dışarı veri çıkış (exfiltration) izlerini bulduğunda ne olacak?" | Başarılı | - |

## Sonuç
AI Tutor %80 oranında Sokratik yönteme sadık kalarak öğrenciyi düşünmeye itmiştir. Hata yapılan %20'lik dilimde ise Tutor, doğrudan teknik cevabı vererek veya "Doğru/Yanlış" şeklinde kesin yargı belirterek Sokratik yapıyı bozmuştur.
