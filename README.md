# 🚀 Network Intrusion Detection System (NIDS)

## 📌 Overview

This project is a **Network Intrusion Detection System (NIDS)** that monitors network traffic and detects suspicious or malicious activities using **Machine Learning**.

It provides a **web-based dashboard** where users can view real-time network activity and intrusion alerts.

---

## 🎯 Features

* 🔍 Real-time packet monitoring
* 🤖 Machine Learning-based attack detection
* 📊 User-friendly web dashboard
* 🔐 Login & registration system
* 📁 Data storage using SQLite

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML, CSS
* **Machine Learning:** Scikit-learn (model.pkl)
* **Database:** SQLite

---

## 📂 Project Structure

```
NIDS_project/
│── app.py
│── sniffer.py
│── train_model.py
│── nids_model.pkl
│── database.db
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│
├── static/
│   ├── style.css
│   ├── logo.png
│   ├── favicon.png
```

---

## ⚙️ How to Run the Project

### 1️⃣ Clone the repository

```
git clone https://github.com/24BCS12641/NIDS-Project.git
cd NIDS-Project
```

### 2️⃣ Install dependencies

```
pip install flask scikit-learn
```

### 3️⃣ Run the application

```
python app.py
```

### 4️⃣ Open in browser

```
http://127.0.0.1:5000
```

---

## 🧠 How It Works

1. Captures network packets using a sniffer
2. Extracts important features
3. Uses a trained ML model to classify traffic
4. Displays results on the dashboard

---

## 📸 Screenshots

<img width="1901" height="848" alt="Screenshot 2026-03-22 121446" src="https://github.com/user-attachments/assets/c73656cf-6744-467d-974f-48ff97b92659" />


---

## 🔮 Future Improvements

* Add deep learning model
* Improve UI design
* Deploy on cloud (AWS/Render)
* Real-time alert notifications

---

## 👨‍💻 Author

**Sunny Kumar**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
