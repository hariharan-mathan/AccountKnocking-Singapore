from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import requests

site_url = "foodpanda.sg"

def account_knock(email):
    options = webdriver.FirefoxOptions()
    # options.add_argument('--headless')  # Run in headless mode if you don't need a UI
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
    driver.get("https://www.foodpanda.sg/")
    cookies = driver.get_cookies()
    user_agent = driver.execute_script("return navigator.userAgent;")
    cookie_string = "; ".join([f"{cookie['name']}={cookie['value']}" for cookie in cookies])
    print(cookie_string)
    driver.quit()

    login_api_url = "https://www.foodpanda.sg/login/new/api/email-check"
    headers = {
                "Content-Type": "application/json;charset=UTF-8",
                "Accept": "application/json, text/plain, */*",
                # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.127 Safari/537.36",
                # "Cookie": "_pxvid=384a457b-39d3-11ef-85d8-495691dc02b4; dhhPerseusGuestId=1720076503803.947539916549420624.n7ofhd2j0c; ld_key=1720076503803.947539916549420624.n7ofhd2j0c; _gcl_au=1.1.1927717914.1720076506; __ssid=95f68916f96c8010b93aa78570863c0; _fbp=fb.1.1720076508123.389171964634403468; _pxhd=u31Bi0qySz1Klb1JWBxP0BP1rrj/vTTTkA2xVKdVXEf3v281q0J9nfWFt1yoBRuH8HiPzepzR01eM1y0K8DXGQ==:Rw8grU0-DtlXPda9Fu2USmdZWAVtkY80i-ehAU/hNrRdRZJ02SDWVkeYYfB00wWT0r0-zm5gxXt-0HCGil49t0wKzaUXh8jDdvS/Eagea1U=; __cf_bm=3tfttLmBoNvDO8Ki9_c65c2LqZPtLdnpUhpXTLmHiZg-1720605940-1.0.1.1-B9JnOyz7Y24lrxUvzFvPrvqzoBrDluvU0gHjx3Oxa_DRplZEAZ7yqZP6Tv5aOEgUpRJzep6HaYmMHm1Oga7BL1BtjUkJxqVJDYZB8VUAJu0; dhhPerseusSessionId=1720605951908.112250730329613697.lszzkau29v; hl=en; pxcts=fe298766-3ea3-11ef-931f-696081abac24; _gid=GA1.2.964056655.1720605954; _ga_HCJXSZSZBP=GS1.1.1720605954.2.0.1720605954.60.0.0; _ga=GA1.1.1244672814.1720076506; _hjSessionUser_915617=eyJpZCI6Ijk1MjExYjhhLTllYTEtNWYzYy1hYTY0LWMwNzI0NzhjM2E5ZCIsImNyZWF0ZWQiOjE3MjAwNzY1MDY3MDIsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_915617=eyJpZCI6IjNjODIxNjQxLTNlY2QtNDU0Mi1iODE4LWFiZmQzMmE3ZjVhNSIsImMiOjE3MjA2MDU5NTQ3NDUsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; _tq_id.TV-81365445-1.27fd=abbed5ea15c1a28b.1720076507.0.1720605955..; _px3=aa500b725789523890515eb3d2a90c2c9debc2132e83a90e8d572c99f4b8ee6d:EDFYe8g//VWw0HqaKNZYMCbupKLJRqSuhKxi3h5gAsJzZXtvY/nJS4nhXFxiBanXGaP++wcnKL2GuJLdeUtBqA==:1000:iuECn1+fK0PUpXEtGf1HvQhOuTnxXihETpeUBvBYzTktt1CCt6DydIn5sQ0XyAVUZP/CAbkyydbg06UaFXHPwPVADBV+5eXohgU8RUT9/gS1cCxhC1JSEN6SVC44/FZwSniT7/ZcQ6gRmzi/NBzZ7qZu8xpnabR0NP75JH5/Y7g2xabcAWmi5Uk+/UxmGkawtG3O+FRHeX9SzUJeKDIyGxRgiuvPAMXciDUt0ky/j/w=; _dd_s=logs=1&id=c66ca800-e48d-4089-93ed-640aa08d208d&created=1720605953663&expire=1720607856344; dhhPerseusHitId=1720606956354.565889523417907954.8hcwq8rp1s",
                "Cookie": f"{cookie_string}",
                "User-Agent": f"{user_agent}",
                "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126"',
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": '"Linux"',
                "Origin": "https://www.foodpanda.sg",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Referer": "https://www.foodpanda.sg/",
                "Priority": "u=1, i",
                "Perseus-Session-Id": "1720605951908.112250730329613697.lszzkau29v",
                "Perseus-Client-Id": "1720076503803.947539916549420624.n7ofhd2j0c"
            }
    payload = {"email": email}
    try:
        response = requests.post(url=login_api_url, headers=headers, json=payload)
        response_json = response.json()
        
        if response_json.get("is_known") == 'true':
            print(f"{email} user found on {site_url}")
        elif response_json.get("is_known") == 'false':
            print(f"{email} does not exist on {site_url}")
        else:
            print(f"Unexpected Error {response.text} \nChange the Cookie")

    except requests.exceptions.RequestException as e:
        print("Unexpected response format:", e)

email = str(input("Enter the Email: "))
account_knock(email)
