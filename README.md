````markdown
# 😷 AI Face Mask Detection

An AI-powered web application that detects whether a person is wearing a face mask or not from an uploaded image.

Built using **Python, Flask, TensorFlow, OpenCV, HTML, CSS, and JavaScript**.

## 🌐 Live Demo

👉 **[Launch AI Face Mask Detection App](https://facemaskdetection-ym86.onrender.com)**

Upload a face image and get an AI-powered prediction of **Mask** or **No Mask** along with the prediction confidence.

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
- TensorFlow / Keras
- OpenCV
- NumPy
- HTML5
- CSS3
- JavaScript
- CNN (Convolutional Neural Network)
- Docker
- GitHub
- Render

## 🧠 Model

The application uses a trained **CNN (Convolutional Neural Network)** model for image classification.

**Input:** 200 × 200 pixel image

**Classes:**

| Class | Prediction |
|---|---|
| 0 | Mask |
| 1 | No Mask |

The model processes the uploaded image and returns the predicted class along with its confidence score.

## 🔄 How It Works

```text
User Uploads Image
        ↓
Flask Receives Image
        ↓
OpenCV Processes Image
        ↓
Image Resized to 200 × 200
        ↓
Pixel Normalization
        ↓
CNN Model Prediction
        ↓
Prediction + Confidence
        ↓
Result Displayed on Web Page
````

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
├── mask_no_mask.h5
├── .gitignore
├── .gitattributes
└── README.md
```

## 📄 File Description

| File / Folder          | Description                            |
| ---------------------- | -------------------------------------- |
| `app.py`               | Flask application and prediction logic |
| `mask_no_mask.h5`      | Trained CNN model                      |
| `check_model.py`       | Model checking utility                 |
| `requirements.txt`     | Python dependencies                    |
| `Dockerfile`           | Docker configuration                   |
| `templates/index.html` | Web page structure                     |
| `static/style.css`     | Styling and animations                 |
| `static/script.js`     | Frontend interactions                  |
| `static/bg.jpg`        | Background image                       |
| `static/logo.png`      | Application logo                       |

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/RamyaAchar34/FaceMaskDetection.git
```

### 2. Navigate to the project

```bash
cd FaceMaskDetection
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
.venv\Scripts\activate
```

**macOS / Linux:**

```bash
source .venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

## 🐳 Docker

Build the Docker image:

```bash
docker build -t face-mask-detection .
```

Run the application:

```bash
docker run -p 5000:5000 face-mask-detection
```

Open:

```text
http://localhost:5000
```

## ☁️ Deployment

The application is deployed using **Docker and Render**.

🌐 **Live Application:**
[https://facemaskdetection-ym86.onrender.com](https://facemaskdetection-ym86.onrender.com)

## 👩‍💻 Developer

**Ramya Achar**

Data Science & Analytics | Python | SQL | Power BI | Tableau | Machine Learning | Deep Learning

### 🔗 Links

* 🌐 [Live Demo](https://facemaskdetection-ym86.onrender.com)
* 💻 [GitHub Repository](https://github.com/RamyaAchar34/FaceMaskDetection)

---

⭐ If you find this project useful, consider giving it a star on GitHub.

```
```
