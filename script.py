import requests
import sys


r = requests.get("http://google.com")
print(r.status_code)
print(r.ok)
