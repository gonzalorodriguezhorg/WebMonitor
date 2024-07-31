import requests
import pprint


def get_web_code(host, type="secure"):
    web_connection = {}
    if type == "secure":
        host = "https://" + host
    else:
        host = "http://" + host
    try:
        r = requests.get(host)
    except Exception as e:
        web_connection["response"] = False
        web_connection["reason"] = f"{str(e)}"
    else:
        web_connection["response"] = True
        web_connection["status_code"] = r.status_code
        web_connection["history"] = r.history
        web_connection["headers"] = r.headers
        web_connection["cookies"] = r.cookies
        web_connection["encoding"] = r.encoding
    return web_connection


var = get_web_code("taeconta.com")
pprint.pprint(var)
