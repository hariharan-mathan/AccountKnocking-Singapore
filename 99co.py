import requests

site_url = '99.co'

def account_knock(email):
    url = "https://www.99.co/api/v1/web/accounts/login"
    headers = {
        # "Cookie": "__cf_bm=bIkTLj4QBc9oeOI3u7FkAfGjOQsJ3YsSvhT0xl5qLmU-1720603028-1.0.1.1-XPw9yuLXDNlU.sRsodYi9TmaiqO_fbphuTZK_qMZ9r_PwT.reeBfSKrCIXVEjZUciHZjdIbszLUNXDXI6Nw.RQ; _cfuvid=a4ycZo2Vx8oSN4BXvFTNyFgrC0T.fP9sGXa2FsidXuM-1720603028629-0.0.1.1-604800000; cf_clearance=yXyiGmaJK148pggdab4kO5vPcLDQy8WpTfFPwZeO_Bw-1720603028-1.0.1.1-qUdy7XGeAxF_CQ6fwEKoKF9mCisnppLm4p1XHonn0abxmvHtcQPiGxMmCfJ0hIcM95V7XG3Fcx2xzA7iUnwB_Q; nid=747a2d59-be4f-4352-b76a-f1e83026e77c; ajs_anonymous_id=747a2d59-be4f-4352-b76a-f1e83026e77c; _gcl_au=1.1.1077215682.1720603055; _fbp=fb.1.1720603054896.982805983149252238; WZRK_G=590587d73ce84652b6d9b624ca1ca17a; _gid=GA1.2.575294638.1720603055; _ga_GG21BH9GS5=GS1.1.1720603055.1.0.1720603055.60.0.0; _ga=GA1.1.1837153242.1720603055; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22zadW1DLYFC59izQV0we0%22%7D; _ga_XW0YWPFYJ7=GS1.2.1720603055.1.0.1720603055.0.0.0; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%22unknown%22%7D; _tt_enable_cookie=1; _ttp=VO8aI7xng90UIZOxqiB-D4PvZVi; _hjSessionUser_288049=eyJpZCI6Ijc1MDNjNjkwLTA2YjUtNTg4OC1iZDM0LTcxYmE5Mzc4MWY4MiIsImNyZWF0ZWQiOjE3MjA2MDMwNTU2NzksImV4aXN0aW5nIjpmYWxzZX0=; _hjSession_288049=eyJpZCI6IjRiMmJhNjJlLWQ1YjYtNDM1MC04ZWZiLWJjMDk4MWEwMzhjMCIsImMiOjE3MjA2MDMwNTU2ODIsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; _hjDonePolls=949993; dicbo_id=%7B%22dicbo_fetch%22%3A1720603056372%7D; WZRK_S_6Z6-5Z4-R56Z=%7B%22p%22%3A1%2C%22s%22%3A1720603054%2C%22t%22%3A1720603131%7D; G_ENABLED_IDPS=google; _ga_9FDXXVZSH0=GS1.1.1720603055.1.1.1720603148.0.0.0; _ga_6C5VMQ1JNP=GS1.1.1720603055.1.1.1720603159.29.0.0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.127 Safari/537.36",
    }
    data = {"password": "password123", "email": email}
    
    try:
        response = requests.post(url, headers=headers, json=data)
        
        response_json = response.json()
        
        if response_json.get("error", {}).get("message") == "invalid user":
            print(f"{email} does not exist on {site_url}")
        elif response_json.get("error", {}).get("message") == "The password you entered is incorrect. Please try again.":
            print(f"{email} user found on {site_url}")
        
    except:
        print("Unexpected response:", response.text)

email = str(input('Enter the Email: '))
account_knock(email)
