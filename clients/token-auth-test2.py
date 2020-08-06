import requests

def client():
    data = {
        "username" : 'resttest',
        'email' : 'test@rest.com',
        'password1' : 'django1234',
        'password2' : 'django1234'
    }


    response = requests.post("http://127.0.0.1:8000/api/rest_auth/registration/",
                                data=data)

    print("status_code :", response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()
