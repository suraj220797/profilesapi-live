import requests

def client():
    credentials = {'username':'admin', 'password':'django1234'}

    response = requests.post("http://127.0.0.1:8000/api/rest_auth/login/",
                                data=credentials)

    print('status code: ', response.status_code)
    response_data =response.json()
    print(response_data)


if __name__ == "__main__":
    client()
