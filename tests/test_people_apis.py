
from starlette.testclient import TestClient
import pytest,os
# from server.app import app
import json

import requests
from faker import Faker
fake = Faker()

# The root url of the flask app
url = 'http://127.0.0.1:5000/people'


def test_common_friends_api_empty():
    peopleA = "1"
    peopleB = "2"
    surl = url+"/%s/%s"%(peopleA,peopleB)
    r = requests.get(surl) 
    assert r.status_code == 200 
    result = r.json()
    assert len(result['data']) > 0 


def test_common_friends_api_work():
    peopleA = "13"
    peopleB = "14"
    surl = url+"/%s/%s"%(peopleA,peopleB)
    r = requests.get(surl) 
    assert r.status_code == 200 
    result = r.json()
    assert len(result['data']) > 0 

    shouldExists = False
    if len( result['data']['common_friend'] ) > 0:
        shouldExists = True

    assert shouldExists == True


def test_common_friends_api_should_not_exists():
    peopleA = "2"
    peopleB = "44"
    surl = url+"/%s/%s"%(peopleA,peopleB)
    r = requests.get(surl) 
    assert r.status_code == 200 
    result = r.json()
    assert len(result['data']) > 0 

    shouldNotExists = False
    if len( result['data']['common_friend'] ) == 0:
            shouldNotExists = True

    assert shouldNotExists == True


def test_common_friends_api_should_return_error():
    peopleA = "-2"
    peopleB = "44"
    surl = url+"/%s/%s"%(peopleA,peopleB)
    r = requests.get(surl) 
    assert r.status_code == 400 
    

def test_common_friends_api_should_return_error2():
    peopleA = "9387395734523424394"
    peopleB = "44"
    surl = url+"/%s/%s"%(peopleA,peopleB)
    r = requests.get(surl) 
    assert r.status_code == 400  

def test_common_friends_api_should_not_found():
    peopleA = "99999"
    peopleB = "44"
    surl = url+"/%s/%s"%(peopleA,peopleB)
    r = requests.get(surl) 
    assert r.status_code == 204 

def test_get_user_favourite_fruits_and_vegetables():
    
    peopleA = "4"
    surl = url+"/favourite/%s"%(peopleA)
    r = requests.get(surl) 
    assert r.status_code == 200 
    result = r.json()
    assert len(result['username']) > 0 



def test_get_all_user_favourite_fruits_and_vegetables():
    
    for i in range(1,30):
        surl = url+"/favourite/%s"%(i)
        r = requests.get(surl) 
        assert r.status_code == 200 
        result = r.json()
        assert len(result['username']) > 0 


def test_people_detail_api_normal():
    peopleA = "1"
    surl = url+"/%s"%(peopleA)
    r = requests.get(surl) 
    assert r.status_code == 200 
    result = r.json()
    assert result['index'] == 1
