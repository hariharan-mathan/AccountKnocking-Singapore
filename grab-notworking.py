import requests

site_url = "grab.com"

def account_knock(phone):
    url = "https://partner-api.grab.com/grabid/v1/mfa/v2/PUSH"
    headers = {
        "Host": "partner-api.grab.com",
        "Cookie": "OptanonAlertBoxClosed=2024-07-04T07:10:30.020Z; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Jul+04+2024+12%3A40%3A30+GMT%2B0530+(India+Standard+Time)&version=202304.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1; _gid=GA1.2.62406908.1720077030; _gcl_au=1.1.368985611.1720077031; _fbp=fb.1.1720077031269.256625132808740692; _ga=GA1.2.427047428.1720077030; _hjSessionUser_1532049=eyJpZCI6Ijg3Y2RlMjZhLTc4ZWUtNWRjMC05M2FkLTkzOTU1NjVkMmUwNSIsImNyZWF0ZWQiOjE3MjAwNzcwMzE0OTgsImV4aXN0aW5nIjp0cnVlfQ==; _ga_65FYNH52KQ=GS1.1.1720077031.1.1.1720077111.55.0.1740941655",
        "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\"",
        "X-Recaptcha": "03AFcWeA5549dsyuCz_LS2VP5CrSmk1WZ_oNSrz2SvD4NmUI3plDXyd7j8en173ft0QL09BzIf3lfNckCfnziyMx9vBZa24DOPdHUf8UgDfv_jBuOkDRsmf4_hmroX00glbGj43RysLrwExjqUB_MYao5uMOcSqd8rjHE25hbv0UNmoOOX9ym2s6YEK1odzpgRgbDouVvnnKq9WMArF4MNBGg9-oXNvzff-bHb9d2xNfIuityKCKoHpWtSgceOlij-ySFcR6bVyB1sTi75BdYg67KjLoAGFUMwpjoVzDIWNemwG0sJRybA2hW-t_twpZ_lgC09kY8FVKg2zCVNsqD1MoT4sed4omZJx713-V3AJsZW_f6h-EgpgwaCGABk8Vn9Jld-u-wdzmA-AVbGZdlvES0FD-RQey9TO8dJPKtWFhG5EL_YFy5-PiHQpuGJS9XB87Fff98b2M7JdKHRVqHSiNdL6niUkwBMWmAPlwc7ekHnlTOhn0nc0oGJs1wK7XgotkUPaEnHH178pPZnZw7qc8UiFSEgTE4DYuAqR_XMSuLWklNZF_NU8jpEnuK_qZ7RGy_tkDi2DYce3lgEq2xoJLE0hq_KJ7DDhgeFBoXTA-5jCp-75PVNz-Ai3OE12ft_w7ksSpggDoqWykl58qKBR2b15i8ojtuj9TlguOgsOYdUU7blFqMbhHoodFN9S-YANkOTipwlAOm7EqeoxNVoKP8JWSxm8DmW6X3UxxELM4PNPNnV6JDcFlMaC46-ckdSQm1hCT88xOojsigK3Sm9cHzFAf89T9FYt7J8F1ufhSzkuUhv3FxUb1YYi3dhANAwAkMoj1rpMbnEUAcT90995sfh89tRFe8x_Co5w9K2_iakYYiuCZBWA7rUsnXLM0CyvjKY68qWIB62RXP1gPHUYrp6LsXfHJ9Du61-wmt2vVASLRrXbHheGmsGcqfrXB_auG9eucdjcV4bSPH96nRT4g8Eh1a8l-nPETjvVP-7dKD4IQxwiWKOzQ347jVsCh55USXT6beCC0DONsCJCKs29OSJ_k0GULUJALg_5mfsD3vaRPqKqWnlzqSxiXgnWV7SK6chxryn4S7EPJp5qnHyrKuFv5FM_lSOXbnA3d1SkjWd0Qjc2yA1W1HGbDK1BT8DircCOQBCQGiTaCzhhtOHg-XZ1ME5F8wensqSSZrZEiPuvUV1xL_ZFeadTMp835wiB53T-XCb-XlU4OZWJaTOaVYIdqeuJ6ab5i8HSzPLx2QqFfrjSKMZQGUj5c-UwEeIKvoP6qQeeZPGBOg0IiuxIxz-DOwiqeZmbIsGCpIJI2r2mv34SVBnnrfxxagnWsswJhblKTiLzmDElVj8jmr_pJ8xF3eoW4yIGIAkY8ppPShf2FXZ2haxRiLZRVcxIE2VCqoJGxhZltGCzSFjbHpgNvpnSAb6DxKzO9pXtgDdEltiGuPm4_N9bQyZ1FYjQ_tPpKewnmwTHVau3B7IA3ZJonJXyoYrIJLu5WHz2wv9v23HSh4t04NKS6avXmadnW8YU8A1a3SmngIcx6IRAx20knPkTwMvwybrESmTs9eIRDj0WSkq1wRkvlj41Ro7GNqCOM3Q09Sn9JM8-UT2GNHCAJa-nbVqSTxT5OtkjcTSYBwiLlwEGMThK8DnAw5TZrqGPwbr6Zo1SSPBVQGVw3NdAPmTDRhiDtojUkC7ISUBlnNFDfW4r3EOMJASUkQsOke4iwAA02c9AOVX3lDuhcDrADVI-YKHBD8ZCaIS-9yiCvQBnf4M3WvZQGShB2c3KcKGX02dtoFwbfQP7ALPbt6BkZkFOq0u1fkeVzL7nY61ArXTmGTntk3KfukAaSj2_6KTJTUv8il1zEq7QF7lUKDVuHWXmLJcv_gIY2PIK5xRkWJWKsSiKf6YGmAvPiAa_OS5Lh0237586zCVoxYghL9n388GWxJ5xbPwUe7r0IfbNB6m9FYM1XRLw2g86bSo_fM0muNwpjAoqMCwFtYrGMKVsvBfuI2x-aA9SvRdRsDlu5liDrUcGy8RAxADzaL9I5nglR1fy4lOfS7EmtlUAEqEtnQN1yT0sHmpvxeY8dbMjtTlyzu5VREvqEc",
        "Accept-Language": "en-GB",
        "Sec-Ch-Ua-Mobile": "?0",
        "X-Hydraweb-Jwt": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnYWEiLCJhdWQiOiJ3bGciLCJuYW1lIjoiZ3JhYnRheGkiLCJpYXQiOjE3MjA2MDUyODcsImV4cCI6MTcyMDYwNTg4NywibmJmIjoxNzIwNjA1Mjg3LCJ2ZXIiOiIxLjE5LjAuMjQiLCJicklEIjoiODIzN2ExZDY5MmY3NGIwYjZhYjNkZjU1MTQ1YmM0NjQ5YWFVRHAiLCJzdXMiOmZhbHNlLCJicklEdjIiOiJlODkzOGVjYjk4NDVkNTE0MDc4ZjE0YmJmYWI1NzlmM2ZkN1VEcCIsImJyVUlEIjoiOGMzMTU5OTQtZGI2OS00YmJiLTkxNjktNDE3ZWQxMGY1NjU2In0.RTQelMEhiVDof0mO-KYjURPsaCZAXOE-vjKjQC8kJHS6HbTQiMpeV4VP1QAFUeBVGNFshbMzQlKbxi7ZiNDhQ3s79xHcT9VUR6EQ32D7N-5UpP4LwOL6dDvBT8ZjwVzj6xrEPrAqQ6RZNdHiUoqM_MzWnzAAdZppgOFHXiZAI_ZvSudBIRFao6HPBWj6RXTq4Dj0fMkGNxiwqy138DaxJObV_JOL4_wFClcHua7PieK7jn_UimVSdxdum5GbigAJh3gh2uj_S1Ec5UVI6wnKRXCeSfI_l9iVzl9Tb0ozc9jxWw0iTsvltWTi876GMZSwMhoPdAJjUwFjkN_f0emTrg",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.127 Safari/537.36",
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "X-Request-Id": "f97f597e-f9fc-46a3-bee7-7d42b4a0bbab",
        "Sec-Ch-Ua-Platform": "\"Linux\"",
        "Origin": "https://weblogin.grab.com",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://weblogin.grab.com/",
        "Priority": "u=1, i",
        "Connection": "keep-alive"
    }
    payload = {
        "ctx_id": "a5e9169345ee47949299623849f43639",
        "phone_number": f"{phone}",
        "client_id": "4ddf78ade8324462988fec5bfc5874c2"
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response_json = response.json()
        
        if "errors" in response_json:
            error_message = response_json["errors"][0]["message"]
            if error_message == "partner is not allowed to register user":
                print(f"{phone} does not exist on {site_url}")
            elif error_message == "suspected toll fraud":
                print(f"{phone} user found on {site_url}")
            elif "mech_type" in response_json:
                print(f"{phone} user found on {site_url}")
            else:
                print("Unexpected error message:", response.text, "\nChange the Cookie")
        else:    
            print(f"Unexpected json response {response.text}")
                
    except ValueError:
        print(f"Unexpected response {response.text}")

# Example usage
phone = str(input("Enter the phone number: "))
account_knock(phone)
