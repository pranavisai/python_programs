import requests
import datetime as dt

pixela_end_point = "https://pixe.la/v1/users"
TOKEN = "hello12345"
USERNAME = "pranavisai"
graphID = "graph1"
headers = {
    "X-USER-TOKEN": TOKEN
}

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

#response = requests.post(url= pixela_end_point, json=user_params)
#profile creation success!

graph_endpoint = f"{pixela_end_point}/{USERNAME}/graphs"

graph_params = {
    "id": "graph1",
    "name": "Everyday Exercise Calories",
    "unit": "Cal",
    "type": "int",
    "color": "ajisai",
}

#response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# graph creation is success!

pixel_creation_end_point = f"{pixela_end_point}/{USERNAME}/graphs/{graphID}"

today = dt.datetime.now()
date = today.strftime("%Y%m%d")

pixel_params = {
    "date": date,
    "quantity": "359",
}
#response = requests.post(url=pixel_creation_end_point, json=pixel_params, headers=headers)
#pixel updated successfully

update_or_delete_end_point = f"{pixela_end_point}/{USERNAME}/graphs/{graphID}/{date}"

update_pixel = {
    "quantity": "450",
}

#response = requests.put(url=update_end_point, json=update_pixel, headers=headers)

response_data = requests.delete(url=update_or_delete_end_point, headers=headers)
print(response_data.text)




