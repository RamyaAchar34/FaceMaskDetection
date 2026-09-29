from flask import Flask, render_template, request, jsonify
import base64
from tensorflow.keras.models import load_model
import numpy as np
import cv2

app = Flask(__name__)

# Load model
model = load_model("mask_no_mask.h5", compile=False)

# Classes (0 = with_mask, 1 = without_mask)
classes = ["Mask", "No Mask"]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    if "file" not in request.files:
        return render_template(
            "index.html",
            prediction="No file selected",
            confidence=""
        )

    file = request.files["file"]

    if file.filename == "":
        return render_template(
            "index.html",
            prediction="No file selected",
            confidence=""
        )

    try:
        # Read uploaded image directly into memory
        file_bytes = np.frombuffer(file.read(), np.uint8)

        # Decode image using OpenCV
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        if img is None:
            raise Exception("Unable to read image.")

        # Resize exactly like training
        img = cv2.resize(img, (200, 200))

        # Normalize
        img = img.astype(np.float32) / 255.0

        # Add batch dimension
        img = np.expand_dims(img, axis=0)

        # Predict
        prediction = model.predict(img, verbose=0)

        predicted_class = np.argmax(prediction)
        confidence = float(np.max(prediction) * 100)

        result = classes[predicted_class]

        return render_template(
            "index.html",
            prediction=result,
            confidence=f"{confidence:.2f}%"
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction=f"Error: {str(e)}",
            confidence=""
        )

@app.route("/predict_frame", methods=["POST"])
def predict_frame():

    data = request.json["image"]

    encoded = data.split(",")[1]

    img_bytes = base64.b64decode(encoded)

    np_arr = np.frombuffer(img_bytes, np.uint8)

    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    img = cv2.resize(img, (200, 200))

    img = img.astype("float32") / 255.0

    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img, verbose=0)

    index = np.argmax(prediction)

    confidence = float(np.max(prediction) * 100)

    classes = ["Mask", "No Mask"]

    return jsonify({
        "prediction": classes[index],
        "confidence": round(confidence, 2)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)