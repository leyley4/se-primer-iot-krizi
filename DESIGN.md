# SE Primer - Ekran Tasarımları ve Mantığı

Bu belge, "Yoğun Bakım IoT Siber Saldırısı" senaryosunun Google Stitch üzerinde tasarlanan 3 temel mobil ekranını tanımlar.

## 1. Giriş Ekranı (Onboarding)
**Amacı:** Kullanıcının oyun parametrelerini belirlemesi.
**Görsel Öğeler:**
*   **Başlık:** Yoğun Bakım IoT Kriz Simülasyonu
*   **Seçim Alanı 1 (Seviye):** "Yeni Başladım" (İpuçları açık) / "Deneyimli" (60 saniye süre baskısı)
*   **Seçim Alanı 2 (Rol):** Ağ Güvenlik Uzmanı / Nöbetçi Yazılım Mühendisi
*   **Seçim Alanı 3 (Hedef):** Sistemleri Ayakta Tutmak / Hasta Verilerini Korumak
*   **Buton:** "Simülasyonu Başlat"
*   <img width="369" height="766" alt="image" src="https://github.com/user-attachments/assets/2634df26-3729-4c09-b263-5edc85e7b6ca" />


## 2. Sahne Ekranı (Oynanış / Kriz Anı)
**Amacı:** Kullanıcıya krizi sunmak, karar verdirtmek ve AI Tutor ile etkileşime sokmak.
**Görsel Öğeler:**
*   **Durum Panosu (Üstte):** "Saat 03:00 - Yaşam destek ağında fidye yazılımı tespit edildi!" (Eğer kullanıcı "Deneyimli" seçtiyse sağ üstte geriye sayan 60 saniyelik bir sayaç).
*   **Karar Kartları (Ortada):**
    *   A Butonu: "Ağı fiziksel olarak kes."
    *   B Butonu: "Yedeğe geç."
*   **AI Tutor Sohbet Balonu (Altta):** Doğrudan cevabı söylemeyen, düşündürücü soru alanı. Örnek metin: *"Ağı fiziksel kesmeden önce cihazların kendi iç senkronizasyonunun bozulup bozulmayacağını nasıl anlarsın?"*
*   <img width="369" height="761" alt="image" src="https://github.com/user-attachments/assets/2eddc585-dfcc-44f6-be32-eaf7200ad082" />


## 3. Son Ekranı (Kabul Kriterleri ve Bitiş)
**Amacı:** Yapılan seçimlerin teknik sonucunu (İyi veya Kötü Son) göstermek.
**Görsel Öğeler:**
*   **Sonuç Başlığı:** "SON A - İYİ" veya "SON B - KÖTÜ"
*   **Durum Özeti:** 
    *   *İyi Son Örneği:* "03:15: Sistem ayakta, cihazlar manuel izolasyonda çalışıyor, hasta verileri güvende ve KVKK ihlali yok."
    *   *Kötü Son Örneği:* "03:15: Sistem kilitlendi. Verileri buluta çıkarken KVKK ihlali yaşandı ve cihazların senkronizasyonu koptu."
*   **Geri Bildirim Alanı:** "Ne oldu, neden oldu?" mantığıyla kullanıcının kararlarının özet teknik açıklaması.
*   **Buton:** "Tekrar Oyna"
*   <img width="368" height="787" alt="image" src="https://github.com/user-attachments/assets/566626f4-e08e-4a9c-8270-0d9a60260206" />

