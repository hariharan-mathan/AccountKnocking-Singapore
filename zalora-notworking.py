from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import requests

site_url = 'zalora.sg'

def account_knock(email):
    # Set up Selenium and open the browser
    options = webdriver.FirefoxOptions()
    # options.add_argument('--headless')  # Run in headless mode if you don't need a UI
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
    driver.get("https://www.zalora.sg/customer/account/create/?from=header")
    cookies = driver.get_cookies()
    user_agent = driver.execute_script("return navigator.userAgent;")
    print(cookies)
    cookie_string = "; ".join([f"{cookie['name']}={cookie['value']}" for cookie in cookies])
    driver.quit()

    login_api_url = "https://www.zalora.sg/customer/account/create/?from=header"

    headers = {
        "Host": "www.zalora.sg",
        # "Cookie": "_pxvid=93910510-3a93-11ef-bc9f-a5bc2e5d0c69; __pxvid=93e756dc-3a93-11ef-82c0-0242ac120002; userLanguage=en; browserDetection=eyJ0eXBlIjoiYnJvd3NlciIsIm5hbWUiOiJDaHJvbWUiLCJjc3NDbGFzcyI6ImNocm9tZSIsInZlcnNpb24iOiIxMjYifQ%3D%3D; zid=349984017.1720159901; rrCookie=x0rQFE6JsFpizDMmYoD31sQG1VktfO00; DEVICE_ID=48fac241-84ab-4f4e-9c70-1e93b4f400d2; _ga=GA1.2.1720657362.1720159902; _gcl_au=1.1.1387077625.1720159904; __rtbh.sid=%7B%22eventType%22%3A%22sid%22%2C%22id%22%3A%22349984017.1720159901%22%7D; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22tGTpsBnSpu7M2ezQpGVF%22%7D; 905125419dc9d3c8f422452a786673ba=10217201601382221-0; wallet_balance=0.00; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%2210217201601382221%22%7D; ANONYMOUS_TRACKING_ID=d3811df6-ade7-41f3-b5a4-b3d5faa4e6fc; ajs_anonymous_id=d3811df6-ade7-41f3-b5a4-b3d5faa4e6fc; pxcts=2c095f27-3e8d-11ef-bb1f-6602302655ca; PHPSESSID_17fa9b1613f8ae6225f507737ba25894=d9b70ed9efb7c03227eead0467bf9e2e; _gid=GA1.2.2141005708.1720596168; sessionCount=1; _gat=1; web_momo_revamp=1; _ga_T9WNSTZ90E=GS1.2.1720596168.2.1.1720596184.44.1.735069297; pageCount=4; cto_bundle=F0QJnF95dFI0TTJTQW14dUl0JTJCNldMYWx6WXNMM3dZbDlPJTJGdlRHdWdGZENrMmg1SVJyb0wwbXFaZW5JSWw0TXYxJTJGZXU4WHNCcVVoVnhPTkoxc2xza3JmMUdpWXoyQXBwYTNvbVN3WUI2TnQ0JTJGdTNuZVVBUkhzV0psV3U3WkxRRUxDZlR5; _px3=3e3f8b48ea0e838b69228c31fbeef80e1126bbd0891bf89f5f8ebce31a02692f:wQvlHiaiXosx1lCP3dwNWU9Ho0KaUsYl8yPD+gCxD28S99BG4MVEYytHIs5tjAe2pgBWhshrkOsa6j1XaIpmUQ==:1000:uXAmtkKQbzPoXaWqLDAQovdCS6G26PNNvcvskWemU67SO88bPrnE6PwQG6Ft0MQx7kw0F1bgL0Mx5RYs18SVrhBPA3gC0unzId6wD1952VbgsNeBFpFLkKubpwMT4NWcEpIREBSZLj9By+5pCnP82r6/OJvUboYDSWSEFcR1ed8YjdtSgYdYlzCQVNgVTDi9E/0t0zbsdJYs+zAofFYezQUSobEjvo+DpNYhyBGj+1Q=; _gali=send",
        "Cookie": f'{cookie_string}',
        "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\"",
        "Content-Type": "application/x-www-form-urlencoded",
        "Giosis_srv_name": "SGWWW-A-06",
        "Accept-Language": "en-GB",
        "Sec-Ch-Ua-Mobile": "?0",
        # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.127 Safari/537.36",
        "User-Agent": f"{user_agent}",
        "Sec-Ch-Ua-Platform": "Linux",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Origin": "https://www.zalora.sg",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.zalora.sg/customer/account/create/",
        "Priority": "u=0, i",
    }
    payload = {
        "YII_CSRF_TOKEN": "6c3ecfafc871a163eac538ce25df27f32b76f6c5",
        "RegistrationForm[email]": f"{email}",
        "RegistrationForm[password]": "password123",
        "RegistrationForm[password2]": "password123",
        "RegistrationForm[gender]": "male",
        "RegistrationForm[first_name]": "hasdfsjl",
        "RegistrationForm[day]": "16",
        "RegistrationForm[month]": "11",
        "RegistrationForm[year]": "2005",
        "stayLogged": "1",
        "RegistrationForm[is_newsletter_subscribed]": "1"
    }

    try:
        response = requests.post(url=login_api_url, headers=headers, data=payload, allow_redirects=False)

        # print(f"Response status code: {response.status_code}")
        # print(f'Response Headers: {response.headers}')
        # print(f"Response content: {response.text}")
        status_code = response.status_code
        location_header = response.headers.get('Location', '')

        if status_code == 200:
            print(f"{email} user found on {site_url}")
        elif status_code == 302:
            if location_header.startswith("/customer/account/verify/"):
                print(f"{email} does not exist on {site_url}")
            elif location_header == "https://www.zalora.sg/customer/account/create/?from=header":
                print(f"Cookie error. Please change the cookie. {response.text}")
            else:
                print("Unexpected redirect. Change the cookie", location_header)
        elif status_code == 403:
            print("Cookie error. Please change the cookie.")
        else:
            print(f"Unexpected status code: {status_code}.")
    except:
        print(f"Unexpected Error: {response.text}")

email = str(input('Enter the Email: '))
account_knock(email)