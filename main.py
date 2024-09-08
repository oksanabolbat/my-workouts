import time

import requests
import datetime as dt

APP_ID = "2b46501c"
APY_KEY = "b1e90ebd3c32d37aa9343ff0deab3cb2"

WEIGHT = "40"
AGE = "11"
HEIHGT = "160"

URL_NUTRITIONIX = "https://trackapi.nutritionix.com/v2/natural/exercise"
URL_SHEETY = "https://api.sheety.co/1f35fcee30d9ea1d5cf0c396068544a3/myWorkouts/sheet1"

headers_params = {
    "x-app-id": APP_ID,
    "x-app-key": APY_KEY,
}
exercise_text = input("Tell me which exersice you did: ")
query_params = {
    "query": exercise_text,
    "weight_kg": WEIGHT,
    "age": AGE,
    "height_cm": HEIHGT

}

exercise_response = requests.post(URL_NUTRITIONIX, json=query_params, headers=headers_params)
print(exercise_response.json())
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
    response = requests.post(URL_SHEETY, json=sheety_body)
    print(response.text)
