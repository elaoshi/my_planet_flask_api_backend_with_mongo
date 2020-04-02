
from starlette.testclient import TestClient
import pytest,os
# from server.app import app
import json

import requests
from faker import Faker
fake = Faker()

# The root url of the flask app
url = 'http://127.0.0.1:5000/employee'


@pytest.mark.skip(reason="long time running")
def test_company_api_by_name_not_exists():
    for i in range(1,40):
        fake = Faker()
        campany_name = fake.name()
        surl = url+"/company_name/" + campany_name
        r = requests.get(surl) 
        assert r.status_code == 400 

def test_company_api_by_name_lowercase():
    campany_name = "ZENTRY"
    surl = url+"/company_name/" + campany_name
    r = requests.get(surl) 
    assert r.status_code == 200 
    assert len(r.json()['data']) > 0



def test_company_api_by_name_normal():
    campany_name = "zentry"
    surl = url+"/company_name/" + campany_name
    r = requests.get(surl) 
    assert r.status_code == 200 
    assert len(r.json()['data']) > 0


def test_company_by_id_successful():
    
    campany_id = "18"
    surl = url+"/company_id/" + campany_id
    r = requests.get(surl) 
    assert r.status_code == 200 
    assert len(r.json()['data']) > 0



def test_company_api_by_name_not_exists2():
    campany_name = "-1"
    surl = url+"/company_name/" + campany_name
    r = requests.get(surl) 
    assert r.status_code == 400 



def test_company_by_id_not_exists1():
    
    # for i in range(1,10):
        fake = Faker()
        campany_id = "%s"%(fake.random_int(2999,9999))
        # campany_id = "18"
        surl = url+"/company_id/" + campany_id
        r = requests.get(surl) 
        assert r.status_code == 204 
        # assert len(r.json()['data']) > 0



