from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import numpy as np
import joblib
import os

app = Flask(__name__, static_folder="../frontend", static_url_path="/")
CORS(app)

MODEL_PATH = os.path.join("backend", "model", "model.pkl")
SCALER_PATH = os.path.join("backend", "model", "scaler.pkl")

try:
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    print("✅ Model dan scaler berhasil dimuat.")
except Exception as e:
    print("❌ Gagal memuat model:", e)
    model, scaler = None, None

@app.route("/")
def serve_index():
    return send_from_directory("../frontend", "index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        features = np.array([
            data["luas_tanah"],
            data["luas_bangunan"],
            data["kamar_tidur"],
            data["kamar_mandi"],
            data["lokasi_score"]
        ]).reshape(1, -1)

        scaled_features = scaler.transform(features)
        prediction = model.predict(scaled_features)[0]

        # 🔹 ubah ke satuan rupiah (kalikan sejuta biar realistis)
        predicted_price = prediction * 1000

        return jsonify({
            "predicted_price": round(predicted_price, 2),
            "pesan": f"Prediksi harga rumah sekitar Rp {predicted_price:,.0f}"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/api/test")
def test():
    return jsonify({"message": "API berjalan dengan baik!"})

if __name__ == "__main__":
    app.run(debug=True)
