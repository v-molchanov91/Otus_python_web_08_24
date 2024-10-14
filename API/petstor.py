import json

import pytest
import requests


def test_add_pet():
    body = {
     "id": 0,
     "category": {
       "id": 0,
       "name": "dog"},
     "name": "Foks",
     "photoUrls": [],
     "tags": [
        {
         "id": 0,
         "name": "home"}
     ],
     "status": "available"}

    headers = {'access-control-allow-headers': "Content-Type", 'content-type': "application/json"}
    response = requests.post('https://petstore.swagger.io/v2/pet', json=body, headers=headers)
    response_data = response.json()
    assert response.status_code == 200
    assert response_data['id'] > 0, f"Expected id to be greater than 0, but got {response_data['id']}"


@pytest.mark.parametrize("username, firstName, lastName", [("Swag_swag", "Maria", "Ivanov")])
def test_add_user(username, firstName, lastName):
    body = {
        "id": 0,
        "username": username,
        "firstName": firstName,
        "lastName": lastName,
        "email": "v@mail.ru",
        "password": "1234567",
        "phone": "89675432134",
        "userStatus": 0
    }

    headers = {'accept': "application/json", 'content-type': "application/json"}
    response = requests.post('https://petstore.swagger.io/v2/user', json=body, headers=headers)
    response_data = response.json()
    assert response.status_code == 200
    assert response_data['message'].isdigit()


def test_upload_files():
    file_path = 'C:/Users/v.molchanov/Pictures/Screenshots/Снимок экрана 2024-08-27 095252.png'
    files = {'file': open(file_path, 'rb')}
    r = requests.post('https://petstore.swagger.io/v2/pet/34/uploadImage', files=files)

    files['file'].close()

    assert r.status_code == 200
    response_data = r.json()
    assert 'message' in response_data, "Expected 'message' in response, but it was not found."


def test_not_find_name_user():
    user_name = "Василий"
    url = f'https://petstore.swagger.io/v2/user/{user_name}'
    r = requests.get(url)
    assert r.status_code == 404


def test_find_name_user():
    user_name = "Swag_swag"
    url = f'https://petstore.swagger.io/v2/user/{user_name}'
    r = requests.get(url)
    assert r.status_code == 200
