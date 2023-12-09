import requests


def get_request():
    url = "https://httpbin.org/basic-auth/user/password"
    payload = {}
    headers = {
        'Authorization': 'Basic dXNlcjpwYXNzd29yZA=='
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.status_code)
    return response.status_code


# get_request()

def get_picture():
    url = "https://httpbin.org/image/png"
    payload = {}
    headers = {
        'Authorization': 'Basic dXNlcjpwYXNzd29yZA=='
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    return response

