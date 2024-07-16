import requests
import re

site_url = "singaporematrimony.org"

def account_knock(email):
    url = "https://singaporematrimony.org/"
    session=requests.Session()
    response=session.get(url=url)
    # print(response)
    cookie_string = "; ".join([f"{cookie.name}={cookie.value}" for cookie in response.cookies])
    # print(cookie_string)
    match = re.search(r'XSRF-TOKEN=([^;]+)', cookie_string)
    xsrf_token = match.group(1) if match else None
    url = "https://singaporematrimony.org/password/email"
    headers = {
        # "Host": "singaporematrimony.org",
        # "Cookie": "_ga=GA1.1.2098379899.1720094962; XSRF-TOKEN=brL9eYVbnkxF63Y5v5YZgY2N5YYUBoe1czTbgkrX; singapore_matrimony_session=0dNT0xgjkodEgnJ3CGiqnBptGdbd3IwfrLvadigb; _ga_TCPMCQT923=GS1.1.1720697225.3.1.1720697336.0.0.0",
        "Cookie": f"{cookie_string}"
        # "Cache-Control": "max-age=0",
        # "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\"",
        # "Sec-Ch-Ua-Mobile": "?0",
        # "Sec-Ch-Ua-Platform": "\"Linux\"",
        # "Accept-Language": "en-GB",
        # "Upgrade-Insecure-Requests": "1",
        # "Origin": "https://singaporematrimony.org",
        # "Content-Type": "application/x-www-form-urlencoded",
        # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.127 Safari/537.36",
        # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        # "Sec-Fetch-Site": "same-origin",
        # "Sec-Fetch-Mode": "navigate",
        # "Sec-Fetch-User": "?1",
        # "Sec-Fetch-Dest": "document",
        # "Referer": "https://singaporematrimony.org/password/reset",
        # "Accept-Encoding": "gzip, deflate, br",
        # "Priority": "u=0, i",
        # "Connection": "keep-alive"
    }
    data = {
        "_token": f"{xsrf_token}",
        "email": f"{email}"
    }

    try:
        response = requests.post(url, headers=headers, data=data, allow_redirects=False)
        if(response.status_code == 200):
            print(f"{email} user found on {site_url}")
        elif(response.status_code == 302):
            print(f"{email} does not exist on {site_url}")
        else:
            print(f"Unexpected Error: {response.status_code}\n{response.text}\n Change the Cookies")
    except:
        print(f"Unexpected Error: {response.text}")

email = str(input("Enter the Email: "))
account_knock(email)