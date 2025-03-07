import requests

url = "http://127.0.0.1:5000/predict"
input_data = {
    "fuel_type": "Petrol",
    "transmission": "Manual",
    "year": 2000,
    "mileage": 5.0
}

response = requests.post(url, json=input_data)
print(response.json())
