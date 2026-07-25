# 🌤 Basic Weather App

A simple Python GUI application that displays real-time weather information for any city using the **OpenWeatherMap API**. The application is built with **Tkinter** and provides an easy-to-use interface for checking current weather conditions.

---

## 📌 Features

- Search weather by city name
- Display current temperature in Celsius (°C)
- Display current temperature in Fahrenheit (°F)
- Show humidity percentage
- Show wind speed
- Show weather condition
- Simple and user-friendly Tkinter GUI
- Input validation for empty city names
- Error handling for:
  - Invalid city name
  - Invalid API key
  - Network timeout
  - Internet connection issues

---

## 🛠️ Technologies Used

- Python 3.x
- Tkinter
- Requests
- Python Dotenv
- OpenWeatherMap API

---

## 📂 Project Structure

```
Basic_Weather_App/
│── .venv/
│── weather_app.py
│── requirements.txt
│── .env
└── README.md
```

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/basic-weather-app.git
```

### 2. Open the Project Folder

```bash
cd basic-weather-app
```

### 3. Create a Virtual Environment (Optional)

```bash
python -m venv .venv
```

Activate the virtual environment:

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### 4. Install Required Libraries

```bash
pip install -r requirements.txt
```

---

## 🔑 OpenWeatherMap API Key

1. Visit **https://openweathermap.org/api**
2. Create a free account.
3. Generate an API key.
4. Create a `.env` file in the project folder.

Example:

```env
API_KEY=YOUR_OPENWEATHERMAP_API_KEY
```

---

## ▶️ Run the Application

```bash
python weather_app.py
```

---

## 🖥️ Application Interface

The application provides:

- City Name Input
- Get Weather Button
- Temperature (°C)
- Temperature (°F)
- Humidity
- Wind Speed
- Weather Condition
- Status Bar

---

## 📸 Output Example

```
City : Delhi

Temperature : 34°C
Temperature : 93.2°F

Humidity : 62%

Wind Speed : 3.8 m/s

Condition : Clear Sky
```

---

## 📋 Requirements

- Python 3.10 or later
- Internet Connection
- OpenWeatherMap API Key

---

## 📚 Key Skills Demonstrated

- Python Programming
- GUI Development with Tkinter
- REST API Integration
- HTTP Requests
- JSON Parsing
- Environment Variables (.env)
- Error Handling
- Input Validation
- Event-Driven Programming

---

## 🚀 Future Improvements

- Weather Icons
- Hourly Forecast
- 5-Day Forecast
- Automatic Location Detection
- Dark Mode
- Unit Toggle (°C / °F)
- Refresh Button

---

## 👨‍💻 Developed By

**Aman Kumar**

B.Tech Artificial Intelligence

Python Developer

---

## 📄 License

This project is created for learning and educational purposes.
