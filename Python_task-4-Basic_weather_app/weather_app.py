import os
import tkinter as tk
from tkinter import messagebox
import requests
from dotenv import load_dotenv


# ================= API ================= #

load_dotenv()

API_KEY = os.getenv("API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"



def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32



def get_weather():
    
    city = city_entry.get().strip()

    if city == "":
        messagebox.showerror(
            "Input Error",
            "Please enter a city name."
        )
        return

    status.config(text="Fetching weather...")

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:

        response = requests.get(
            BASE_URL,
            params=params,
            timeout=10
        )

        if response.status_code == 401:
            messagebox.showerror(
                "API Error",
                "Invalid API Key."
            )
            status.config(text="Invalid API Key")
            return

        if response.status_code == 404:
            messagebox.showerror(
                "City Not Found",
                "Please enter a valid city."
            )
            status.config(text="City not found")
            return

        response.raise_for_status()

        data = response.json()

        temp_c = data["main"]["temp"]
        temp_f = celsius_to_fahrenheit(temp_c)

        humidity = data["main"]["humidity"]

        wind = data["wind"]["speed"]

        weather = data["weather"][0]["description"].title()

        temp_c_label.config(text=f"{temp_c:.1f} °C")

        temp_f_label.config(text=f"{temp_f:.1f} °F")

        humidity_label.config(text=f"{humidity}%")

        wind_label.config(text=f"{wind} m/s")

        condition_label.config(text=weather)

        status.config(
            text=f"Weather updated for {data['name']}"
        )

    except requests.exceptions.Timeout:

        messagebox.showerror(
            "Timeout",
            "Request timed out."
        )

        status.config(text="Network Timeout")

    except requests.exceptions.ConnectionError:

        messagebox.showerror(
            "Connection Error",
            "No Internet Connection."
        )

        status.config(text="No Internet")

    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e)
        )

        status.config(text="Something went wrong")

# ================= WINDOW ================= #

root = tk.Tk()
root.title("Basic Weather App")
root.geometry("700x550")
root.minsize(650, 500)
root.configure(bg="#EAF4FC")

# ================= TITLE ================= #

title = tk.Label(
    root,
    text="🌤 Basic Weather App",
    font=("Segoe UI", 24, "bold"),
    bg="#EAF4FC",
    fg="#0F4C81"
)
title.pack(pady=20)

# ================= SEARCH FRAME ================= #

search_frame = tk.Frame(root, bg="#EAF4FC")
search_frame.pack(pady=10)

city_label = tk.Label(
    search_frame,
    text="Enter City Name",
    font=("Segoe UI", 12),
    bg="#EAF4FC"
)
city_label.pack()

city_entry = tk.Entry(
    search_frame,
    width=30,
    font=("Segoe UI", 14),
    justify="center",
    relief="solid",
    bd=2
)
city_entry.pack(pady=10, ipady=5)

search_btn = tk.Button(
    search_frame,
    text="Get Weather",
    font=("Segoe UI", 12, "bold"),
    bg="#0078D7",
    fg="white",
    activebackground="#005A9E",
    activeforeground="white",
    cursor="hand2",
    padx=20,
    pady=6,
    command=get_weather
)
search_btn.pack()

# ================= RESULT AREA ================= #

cards_frame = tk.Frame(root, bg="#EAF4FC")
cards_frame.pack(pady=25)

# ---------- Card Function ---------- #

def create_card(parent, title_text, value_text, row, column):
    frame = tk.LabelFrame(
        parent,
        text=title_text,
        font=("Segoe UI", 11, "bold"),
        bg="white",
        padx=20,
        pady=15
    )

    frame.grid(
        row=row,
        column=column,
        padx=15,
        pady=15,
        sticky="nsew"
    )

    value = tk.Label(
        frame,
        text=value_text,
        font=("Segoe UI", 18, "bold"),
        bg="white",
        fg="#0F4C81",
        width=12
    )

    value.pack()

    return value


temp_c_label = create_card(
    cards_frame,
    "🌡 Temperature (°C)",
    "-- °C",
    0,
    0
)

temp_f_label = create_card(
    cards_frame,
    "🌡 Temperature (°F)",
    "-- °F",
    0,
    1
)

humidity_label = create_card(
    cards_frame,
    "💧 Humidity",
    "-- %",
    1,
    0
)

wind_label = create_card(
    cards_frame,
    "🌬 Wind Speed",
    "-- m/s",
    1,
    1
)

# ================= CONDITION ================= #

condition_frame = tk.LabelFrame(
    root,
    text="☁ Weather Condition",
    font=("Segoe UI", 11, "bold"),
    bg="white",
    padx=20,
    pady=20
)

condition_frame.pack(
    padx=40,
    fill="x"
)

condition_label = tk.Label(
    condition_frame,
    text="No Data",
    font=("Segoe UI", 18, "bold"),
    bg="white",
    fg="#0F4C81"
)

condition_label.pack()

# ================= STATUS BAR ================= #

status = tk.Label(
    root,
    text="Ready",
    anchor="w",
    bg="#D6EAF8",
    padx=10,
    font=("Segoe UI", 10)
)

status.pack(
    side="bottom",
    fill="x"
)

# ================= RUN ================= #

root.mainloop()