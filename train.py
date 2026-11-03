import pandas as pd
import json
import os
import sys
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType

# 1. Veriyi Yükle
df = pd.read_csv('data/oturumlar.csv')
X = df[['seviye', 'karar_suresi_sn', 'hata_sayisi']].astype(float)
y = df['ipucu_verilmeli_mi']

# 2. Modeli Eğit (Sabit tohum 'random_state' ile tekrarlanabilirlik)
model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X, y)

# 3. Ölç ve Değerlendir (Eval Kapısı)
y_pred = model.predict(X)
accuracy = accuracy_score(y, y_pred)
print(f"Model Doğruluğu: {accuracy:.2f}")

# Spec'te belirlediğimiz %80 kabul eşiği
if accuracy < 0.80:
    print("HATA: Model doğruluk eşiğini (%80) geçemedi. Artefakt üretilmedi.")
    sys.exit(1)

# 4. Paketle (ONNX ve Config - Sözleşme)
os.makedirs('model', exist_ok=True)

initial_type = [('float_input', FloatTensorType([None, 3]))]
onx = convert_sklearn(model, initial_types=initial_type)
with open("model/model.onnx", "wb") as f:
    f.write(onx.SerializeToString())

config = {
    "features": ["seviye", "karar_suresi_sn", "hata_sayisi"],
    "classes": [0, 1],
    "metrics": {"accuracy": accuracy},
    "version": "1.0"
}
with open("model/config.json", "w") as f:
    json.dump(config, f, indent=4)

print("BAŞARILI: Model eşiği geçti. 'model' klasörü içine model.onnx ve config.json oluşturuldu.")
