import requests

url = "https://www.fast2sms.com/dev/bulkV2"

payload = "variables_values=3456&route=otp&numbers=8921261058"
headers = {
    'authorization': "M2sr1gqbLKERi47BjUpGXnA6dlfODyI9cxwo05vSFku3hmZJWHZjITz7ekbUdM5KDo4v0YgCaWtwBcsQ",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)