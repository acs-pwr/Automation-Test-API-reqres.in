from marshal import load, loads
from urllib import response
import requests
import json
import pytest
import jsonpath

# untuk ngerun pytest, harus lwat terminal dan ketik 'pytest -v test_post_method.py'
def test_post():
    url='https://reqres.in/api/users'
    s = requests.session()
    s.cookies.clear()
    body = {
        "name": "ardi",
        "job": "leader"
        }

    response = requests.post(url, data=body)
    code_response = response.status_code
    json_response = json.loads(response.text)
    assert code_response == 201
    name = json_response['name']
    assert name == 'ardi'
    job = json_response['job']
    assert job == 'leader'

def test_post_SuccessLogin():
    url = 'https://reqres.in/api/login'
    body = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
    }
    response = requests.post(url,body)
    code_response = response.status_code
    json_response = json.loads(response.text)
    assert code_response == 200
    assert json_response['token'] == 'QpwL5tke4Pnpja7X4'

def test_post_FailedLogin():
    url = 'https://reqres.in/api/login'
    body = {
    "email": "eve.holt@reqres.in",
    "password": ""
    }
    response = requests.post(url,body)
    code_response = response.status_code
    assert code_response == 400



def test_get():
    url='https://reqres.in/api/users?page=2'
    s = requests.session()
    s.cookies.clear()
    response = requests.get(url)
    code_response = response.status_code
    assert code_response == 200
    json_response = json.loads(response.text)
    datas = json_response['data']
    first_datas = (datas[0])
    second_datas = (datas[1])
    third_datas = (datas[2])
    fourth_datas = (datas[3])
    fifth_datas = (datas[4])
    sixth_datas = (datas[5])    
    assert first_datas['id'] == 7
    assert first_datas['email'] == 'michael.lawson@reqres.in'
    assert first_datas['first_name'] == 'Michael'
    assert first_datas['last_name'] == 'Lawson'
    assert first_datas['avatar'] == "https://reqres.in/img/faces/7-image.jpg"
    assert second_datas['id'] == 8
    assert second_datas['email'] == 'lindsay.ferguson@reqres.in'
    assert second_datas['first_name'] == 'Lindsay'
    assert second_datas['last_name'] == 'Ferguson'
    assert second_datas['avatar'] == "https://reqres.in/img/faces/8-image.jpg"
    assert third_datas['id'] == 9
    assert third_datas['email'] == 'tobias.funke@reqres.in'
    assert third_datas['first_name'] == 'Tobias'
    assert third_datas['last_name'] == 'Funke'
    assert third_datas['avatar'] == "https://reqres.in/img/faces/9-image.jpg"

def test_delete():
    url='https://reqres.in/api/users?page=2' 
    response = requests.delete(url)
    code_response = response.status_code
    assert code_response == 204

def test_put():
    url='https://reqres.in/api/users/2'
    response = requests.patch(url)
    code_response = response.status_code
    assert code_response == 200
    


