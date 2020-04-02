
from starlette.testclient import TestClient
import pytest,os
# from server.app import app
import json

import requests

url = 'http://127.0.0.1:5000' # The root url of the flask app

def test_index():
    r = requests.get(url+'/') # Assumses that it has a path of "/"
    assert r.status_code == 200
