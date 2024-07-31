import requests
URL = "http://127.0.0.1:8000/"

def send_data (jsondata, type):
    try:
        endpoint = URL + type
        r = requests.headers = {
           "Content-Type": "application/json",
           "Accept":"*/*"
        }
        r = requests.post(endpoint, data = jsondata)
        return r.status_code
    except Exception as e:
        return e