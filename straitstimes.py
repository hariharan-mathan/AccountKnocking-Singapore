import requests

site_url = "straitstimes.com"

def account_knock(email):
    login_api_url = "https://account-api.my.sph.com.sg/user/exist"
    headers = {
        "Host": "account-api.my.sph.com.sg",
        "Content-Length": "34",
        "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126"',
        "Sec-Ch-Ua-Platform": '"Linux"',
        "Accept-Language": "en-GB",
        "Sec-Ch-Ua-Mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.127 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
        "Origin": "https://www.straitstimes.com",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.straitstimes.com/global",
        "Accept-Encoding": "gzip, deflate, br",
        "Priority": "u=1, i"
    }
    payload = {
        "username": f"{email}"
    }
    response = requests.post(url=login_api_url, headers=headers, data=payload)
    # print(response.text)
    try:
        response = requests.post(url=login_api_url, headers=headers, data=payload)
        response_data = response.json()
        if(response_data['payload'] == True):
            print(f"{email} user found on {site_url}")
        elif(response_data['payload'] == False):
            print(f"{email} does not exist on {site_url}")
        else:
            print(f"Unexpected error: {response_data}")
    except:
        print(f"Unexpected Response: {response.text}")

email = str(input("Enter the Email: "))
account_knock(email)