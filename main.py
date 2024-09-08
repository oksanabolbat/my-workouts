import time
import os
import requests
import datetime as dt



WEIGHT = "40"
AGE = "11"
HEIHGT = "160"

URL_NUTRITIONIX = os.environ.get("URL_NUTRITIONIX")
URL_SHEETY = os.environ.get("URL_SHEETY")
APP_ID = os.environ.get("APP_ID")
APP_KEY = os.environ.get("APP_KEY")
TOKEN = f"Bearer {os.environ.get("TOKEN")}"
print(APP_ID, APP_KEY)

headers_params = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

headers_token = {
    "Authorization": TOKEN
}

exercise_text = input("Tell me which exersice you did: ")
query_params = {
    "query": exercise_text,
    "weight_kg": WEIGHT,
    "age": AGE,
    "height_cm": HEIHGT

}

exercise_response = requests.post(URL_NUTRITIONIX, json=query_params, headers=headers_params)

data_exercise = exercise_response.json()

now = dt.datetime.now()
today_dt_str = now.strftime("%d%m%Y")
curr_time = now.time()
curr_time_str = time.strftime("%H:%M:%S")
for exercise in data_exercise["exercises"]:
    sheety_body = {
        "sheet1": {
            "date": today_dt_str,
            "time": curr_time_str,
            "exercise": exercise["name"],
            "duration": float(exercise["duration_min"]),
            "calories": int(exercise["nf_calories"])

        }
    }
    print(sheety_body)
    response = requests.post(URL_SHEETY, json=sheety_body, headers=headers_token)
    print(response.text)
