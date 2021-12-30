import requests
from decouple import config

API_KEY = config('API_KEY')

query_params = {"api_key": API_KEY, "attach_breed": 0, "page": 1, "limit": 2}
end_point = config('END_POINT')

response = requests.get(end_point, params=query_params).text
print(response)

