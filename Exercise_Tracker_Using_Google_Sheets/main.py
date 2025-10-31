import requests
import os
from dotenv import load_dotenv

load_dotenv()

APP_ID = "9590d853"
API_KEY = "ab1147f7598bb003e2f9f9ad74297f0d"
GENDER = "female"
WEIGHT_KG = 65
HEIGHT_CM = 152
AGE = 27

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
response.raise_for_status()
result = response.json()
print(result)