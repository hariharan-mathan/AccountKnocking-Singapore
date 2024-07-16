import requests

site_url = 'qoo10.sg'

def account_knock(email):
    login_api_url = "https://www.qoo10.sg/gmkt.inc/swe_MemberAjaxService.asmx/CheckExistsMemberEMail"
    payload = {
        "email": f"{email}"
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.127 Safari/537.36",
        "Referer": "https://www.qoo10.sg/gmkt.inc/Login/Login.aspx?ReturnUrl=https%3a%2f%2fwww.qoo10.sg%2fgmkt.inc%2fMy%2fDefault.aspx"
    }

    try:
        response = requests.post(url=login_api_url, headers=headers, json=payload)
        response_json = response.json()
        response_data = response_json.get("d", 1)
        
        if(response_data != 1):
            msg = response_data.get('ResultMsg',1)
            if(msg != 1):
                if(msg == 'Success'):
                    print(f'{email} does not exist on {site_url}')
                else:
                    print(f'{email} user found on {site_url}')
            else:
                print(f'There is no message found in json response {response_data}')
        else:
            print(f"There is no proper json response {response.text}")
    except:
        print(f"Unexpected Response: {response.text}")

email = str(input('Enter the Email: '))
account_knock(email)