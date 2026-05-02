from flask import Flask, request, jsonify
import os
from model import predict_disease

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ✅ Test route
@app.route("/")
def home():
    return "AI Disease API is running ✅"

# ✅ Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    result = predict_disease(filepath)

    return jsonify({
        "prediction": result
    })

if __name__ == "__main__":
    app.run(port=5001, debug=True)