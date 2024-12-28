import requests
# from semantic_similarity import model

URL = 'http://localhost:11434/api/generate'
MODEL = 'tinyllama'

expected_response = 'The sky is blue because of light scattering.'

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
    # asserting response time
    assert response.elapsed.total_seconds()>5
    # printing the response
    print(response.json()['response'])
    # asserting the number of tokens
    # assert response.json()['prompt_eval_count']==40
    # asserting model similarity

# test_api_generate_positive1(URL,body)