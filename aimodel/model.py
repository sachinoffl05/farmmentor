import random

def predict_disease(image_path):
    diseases = [
        "Leaf Blight",
        "Powdery Mildew",
        "Healthy Leaf",
        "Rust Disease"
    ]
    return random.choice(diseases)