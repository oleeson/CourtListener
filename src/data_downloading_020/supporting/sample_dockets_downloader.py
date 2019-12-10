import requests
from requests.auth import HTTPBasicAuth
import json
import pandas as pd

# Note that additional pages can be accessed like:
# https://www.courtlistener.com/api/rest/v3/dockets/?page=2

# Checking the webpage in a browser can help to make sense of things

response = requests.get('https://www.courtlistener.com/api/rest/v3/dockets')

### Here's a couple methods/attributes to take note of; play with them in a notebook to see what they do:
# response.json()
# response.content
# json.loads(response.content)
# response.elapsed
### Don't forget that you can always look into these by typing "response." and then hit "tab",
###  most editors have autocomplete that will show you some of the methods/attributes that could be useful.

df = pd.DataFrame(json.loads(response.content))

# Incorporate some tests into your data
assert len(df) > 5

print(f'Successfully downloaded, but not yet stored, {len(df)} rows')

if __name__ == "__main__":
    # If we're running this script from the command line, we'll store the data
    df.to_csv("/mnt/d/Users/k_bea/PycharmProjects/FLPResearch/data/dockets_sample.csv")
    print(f'Successfully stored {len(df)} rows')