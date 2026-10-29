# SE Primer: Yazılım Mühendisliği, Oynanan Bir Kitap

Bu proje, hastane yoğun bakım ünitesindeki bir IoT siber güvenlik krizini konu alan, yapay zeka destekli metin tabanlı bir karar simülasyonudur.

## Teslim Linkleri
* **Çalışan Uygulama (AI Studio):** [](https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221U9ZiAouuQ3dfGJakQpNNJ13ub2Z-ADEq%22%5D,%22action%22:%22open%22,%22userId%22:%22112090504294810179083%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing)
* **Demo Videosu (60 saniye):** [](https://drive.google.com/file/d/1-DDqefWIl7uxF9lVadWwcZ9TUIOFpBn7/view?usp=drive_link)

## Proje Dosyaları
* `spec.md` - Problem tanımı, kapsam ve akış şeması.
* `DESIGN.md` - UI tasarım detayları ve ekran geçişleri.
* `eval.md` - AI Tutor'a verilen 20 öğrenci cevabının Sokratik değerlendirme analizi.
* `cypress/e2e/kriz_senaryosu.cy.js` - E2E test senaryoları.

## Ürün Kararı (Product Decisions)
Zaman ve kapsam kısıtları nedeniyle bu projede kasıtlı olarak geliştirilmeyen 3 özellik:
1. **Kullanıcı hesabı ve giriş sistemi eklenmedi:** Simülasyonun odak noktası kriz anındaki karar mekanizmaları olduğu için kimlik doğrulama süreçleri kapsam dışı bırakıldı.
2. **Gerçek veritabanı bağlantısı kurulmadı:** Sağlık verileri içeren kurguda KVKK ihlali risklerini sıfıra indirmek ve izolasyonu sağlamak amacıyla tamamen statik senaryo verileri kullanıldı.
3. **Native mobil uygulama geliştirilmedi:** Hızlı prototipleme ve kolay erişilebilirlik hedeflendiğinden, bunun yerine mobil uyumlu web arayüzü tercih edildi.
