import requests
from graph import graph

data = requests.get("https://openexchangerates.org/api/latest.json?app_id=bd95d1c867444a34be353c8cde342b34").json()

currency = new graph(5)