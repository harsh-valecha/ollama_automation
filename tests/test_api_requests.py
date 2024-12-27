import requests

URL = 'http://localhost:11434/api/generate'
MODEL = 'tinyllama'

body = {
    'model':MODEL,
    'prompt':'why is sky blue',
    'stream':False
}

def test_api_generate_positive1():
    response = requests.post(URL,json=body)
    # assert response status
    assert response.status_code==200
    # asserting if response body contains model
    assert 'model' in response.json().keys()
    # asserting if the model comes correct
    assert response.json()['model']==MODEL


# test_api_generate_positive1(URL,body)