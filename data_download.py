import numpy as np
import pandas as pd
import requests
import re
import json

URL = "https://s3.amazonaws.com/index_2011.json"

response = requests.get(URL)
with open("index_2011.json", 'wb') as f:
    f.write(response.content)

with open('index_2011.json') as f:
    data = json.load(f)
    data = data[list(data.keys())[0]]

df = pd.DataFrame.from_dict(data)
df.head(5)