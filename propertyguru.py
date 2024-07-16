# Captcha Problem

import requests

site_url = 'propertyguru.com.sg'

def account_knock(email):
    url = "https://www.propertyguru.com.sg/"
    session=requests.Session()
    response=session.get(url=url)
    # print(response.headers)
    cookie_string = "; ".join([f"{cookie.name}={cookie.value}" for cookie in response.cookies])
    # print(cookie_string)
    login_api_url = 'https://www.propertyguru.com.sg/api/core/users/query'
    params = {
        "email": f'{email}'
    }
    headers = {
        "Cookie": cookie_string,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.127 Safari/537.36"
    }   

    try:
        response = requests.get(url=login_api_url, params=params, headers=headers)
        # print(response.text)
        if(response.status_code == 200):
            userid = response.json().get("userId")
            print(f"{email} user found on {site_url}\n User id = {userid}")
        elif(response.status_code == 404):
            print(f"{email} does not exist on {site_url}")
        else:
            print(f"Unexpected Error: {response.status_code}\n{response.text}\n Change the Cookies")
    except:
        print(f'Unexpected Response: {response.text}')

email = str(input('Enter the Email: '))
account_knock(email)