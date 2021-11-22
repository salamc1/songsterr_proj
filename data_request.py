import requests
import json

MOP_url = 'https://dqsljvtekg760.cloudfront.net/455118/460590/e6rrY2SCKDXLKgE3nfXxB/1.json'

data = requests.get(MOP_url)
raw_json_data = data.content

json_str = str(raw_json_data)

with open('data.txt', 'w') as f:
      f.write(json_str)
