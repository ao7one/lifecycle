# List product lifecycle data
#
# Expected response from FLRT API
# {"results": [
#     {
#         "input": "7200-05-03",
#         "inputurl": "http://www.ibm.com/support/fix...",
#         "ga": "2021.09.10",
#         "eosps": "2023.11.30"
#     },
#     {
#         "input": "7200-05-02",
#         "inputurl": "http://www.ibm.com/support/fix....",
#         "ga": "2021.04.16",
#         "eosps": "2023.11.30"
#     }
# ]}
#

import requests

url = "https://www14.software.ibm.com/webapp/set2/flrt/liteTable?prodKey=aix&format=json"
timeout = 5

try:
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()

    # Load JSON response to dict
    payload = response.json()

    # Parse output
    print(f'{"OS Level": <15}', f'{"GA Date": <10}', f'{"EOSPS": <10}')

    for result in payload['results']:
        oslevel=result['input']
        ga=result['ga']
        eosps=result['eosps']
        print(f'{oslevel: <15}', f'{ga: <10}', f'{eosps: <10}')

except requests.RequestException as reqEx:
    print(reqEx)