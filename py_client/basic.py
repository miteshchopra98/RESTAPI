import requests

endpoint1 = 'https://httpbin.org/'
endpoint2 = 'https://httpbin.org/anything'
endpoint3 = 'http://127.0.0.1:8000/'
endpoint4 = 'http://localhost:8000/api/'

get_response = requests.get(endpoint4, params={'product_id':1}, json={"query":"Hello World"})

print(get_response.text)
print(get_response.json())
print(get_response.status_code)