import requests
from decouple import config

GET_CURRENT_DATA_URL = config("WEATHERSTACK_URL")
GET_PREDICTION_DATA_URL = config("WEATHERSTACK_PREDICTION_URL")
API_KEY = config("WEATHERSTACK_KEY")

POST_URL = "http://localhost:5000"

get_current_data_params = {"access_key": API_KEY, "query": "Dobrich"}

get_forecast_params = {
    "access_key": API_KEY,
    "query": "Dobrich",
    "forecast_days": 1,
    "hourly": 1,
}


def get_current_data():
    r = requests.get(GET_CURRENT_DATA_URL, get_current_data_params)
    resp_json = r.json()
    temperature = resp_json["current"]["temperature"]
    post_body = {"temperature": temperature, "place": "Dobrich", "weather_api_pk": 3}
    p = requests.post(f"{POST_URL}/current", json=post_body)


# Forecast access is paid


def take_predition_data():
    pass


#     r = requests.get(GET_PREDICTION_DATA_URL, get_forecast_params)
#     resp_json = r.json()
#     print(resp_json)
#     # for predict in resp_json:
#     #     temperature = predict["Temperature"]["Value"]
#     #     prediction_for = predict["DateTime"].split("+")[0]
#     #     post_body = {
#     #         "place": "Dobrich",
#     #         "temperature": temperature,
#     #         "prediction_for": prediction_for,
#     #         "weather_api_pk": 2,
#     #     }
#     #     p = requests.post(f"{POST_URL}/prediction", json=post_body)
