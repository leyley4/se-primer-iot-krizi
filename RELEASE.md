# SE Primer: IoT Kriz Simülasyonu - AI Tutor
**Geliştirici:** Leyla Aydın

## 🔗 Önemli Bağlantılar
* **Uygulama Demo Videosu:** [İzlemek için tıklayın](https://drive.google.com/file/d/15Lda8_2uMlYVRcIXxdDmL4vsCyHtRWUJ/view?usp=drive_link)
* **Hugging Face Model URL (Commit-Pinned):** [model.onnx](https://huggingface.co/leyleyw/iot-kriz-modeli/resolve/fb96b02d75e21d1b0ebd0441fc68ba7bb8f436ca/model/model.onnx)

## 🚀 Proje Özeti
Bu projede, Hastane IoT Kriz Simülasyonu oynayan oyuncuların davranışlarını (Seviye, Karar Süresi, Hata Sayısı) analiz edip anlık ipucu müdahalesinde bulunan bir **Karar Ağacı (Decision Tree)** modeli geliştirilmiştir. Model Python'da eğitilmiş (%100 Doğruluk), ONNX formatına dönüştürülerek Hugging Face'e yüklenmiş ve `onnxruntime-web` ile doğrudan tarayıcı içinde (Edge AI) çalıştırılmıştır.

## 🧪 Diferansiyel Test (Oracle) ve Hata Toleransı
Sistemin güvenilirliği, `tests/parite.py` içindeki Python Test Kahini (Oracle) ile doğrulanmıştır. Belirlenen 5 kritik referans senaryosunda beklenen olasılıklar ile ONNX çalışma zamanı çıktıları karşılaştırılmış, aradaki farkın hocanın belirlediği `< 1e-4` tolerans sınırının altında kaldığı kanıtlanmıştır.

## 📝 Sınav Tasarımı (Öğrenim Çıktıları)
Bu proje, bir yazılım mühendisliği öğrencisinin şu yetkinliklerini kanıtlamak üzere tasarlanmıştır:
1. **Model Eğitimi ve Paketleme:** Scikit-learn ile model eğitip donanımdan bağımsız ONNX formatına dönüştürebilme.
2. **Dağıtım (Deployment) ve Sürüm Kontrolü:** AI modelini dış bir sunucuda (Hugging Face) Rollback destekli, commit'e sabitlenmiş (immutable) linklerle barındırabilme.
3. **Web Entegrasyonu (In-Browser Inference):** Backend sunucusuna ihtiyaç duymadan, AI modelini salt JavaScript ve HTML ile ön yüzde çalıştırabilme.
4. **Kalite Güvencesi:** Deterministik olmayan bir makine öğrenmesi sistemini matematiksel tolerans sınırları kurarak test edebilme.