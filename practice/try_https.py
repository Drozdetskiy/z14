import requests
import json
url = 'https://postman-echo.com'

response = requests.get(
    url=url + '/get',
    params={
        'key_1': 'Value_1',
        'key_2': 'Value_2'
    }
)

print(response.status_code)

response = requests.post(
    url = url + '/post',
    params={
      'q1': 'value1'
    },
    json={
        'key': 'value'
    }
)

print(json.dumps(response.json(), indent=4))
