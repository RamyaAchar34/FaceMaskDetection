````markdown
# 😷 AI Face Mask Detection

An AI-powered web application that detects whether a person is wearing a face mask or not from an uploaded image.

The application is built using **Python, Flask, TensorFlow, OpenCV, HTML, CSS, and JavaScript**.

## 🚀 Features

- 📷 Upload an image for analysis
- 🤖 AI-based face mask detection
- 😷 Detects **Mask** and **No Mask**
- 📊 Displays prediction confidence
- 🔄 Animated upload progress
- 🔍 AI scanning animation
- ⏳ Processing status updates
- 💻 Responsive and user-friendly interface

## 🛠️ Technologies Used

- Python
- Flask
- TensorFlow
- OpenCV
- NumPy
- HTML5
- CSS3
- JavaScript
- CNN (Convolutional Neural Network)

## 📂 Project Structure

```text
FaceMaskDetection/
│
├── static/
│   ├── bg.jpg
│   ├── logo.png
│   ├── script.js
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── check_model.py
├── requirements.txt
├── Dockerfile
└── mask_no_mask.h5
````

## 🧠 How It Works

1. The user uploads an image through the web interface.
2. The image is processed using OpenCV.
3. The image is resized to **200 × 200 pixels**.
4. Pixel values are normalized before prediction.
5. The trained TensorFlow model analyzes the image.
6. The application predicts:

   * **Mask**
   * **No Mask**
7. The prediction confidence is displayed on the screen.

## 📊 Model

The trained deep learning model is used to classify images into two categories:

| Class | Prediction |
| ----- | ---------- |
| 0     | Mask       |
| 1     | No Mask    |

## 🌐 Web Application

The application uses **Flask** as the backend framework and provides a simple web interface for uploading images and viewing predictions.

## ▶️ Run Locally

Clone the repository:

```bash
git clone https://github.com/RamyaAchar34/FaceMaskDetection.git
```

Navigate to the project folder:

```bash
cd FaceMaskDetection
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the Flask application:

```bash
python app.py
```

Open the application in your browser:

```text
http://127.0.0.1:5000
```

## 👩‍💻 Developed By

**Ramya Achar**

Data Science & Analytics | Python | SQL | Power BI | Machine Learning | Deep Learning

## ⭐ Project

If you find this project useful, feel free to ⭐ the repository.
