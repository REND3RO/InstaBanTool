import requests
import time
import json
import os
import colorama
from colorama import Fore

colorama.init(autoreset=True)

clear = lambda: os.system('cls')
abood = requests.session()
jk_id = []

sleep: (2)
print(Fore. GREEN + """
RansomCyberArmy⚠️""")

print(Fore. RED +  """Programmed By @ransomxrend3ro🎩""")
print('===========================================================================')
usr = input(Fore.WHITE + '[!] Username :')
pas = input(Fore.WHITE + '[!] Password :')
target = input(Fore.WHITE + '[!] Target :')
slp = int(input(Fore.WHITE + '[!] Sleep :'))
hd_rep_st = {
    'Host': 'www.instagram.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
    'Accept': '*/*',
    'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
    'X-CSRFToken': 'bSj6yMFvzPzkEhKPuMw8yNXDW4SExRbF',
    'X-Instagram-AJAX': 'c795b4273c42',
    'X-IG-App-ID': '936619743392459',
    'X-IG-WWW-Claim': 'hmac.AR1nKNnzb0dp3ayTWPVIl8DWytEkfyt2ABq5q2ExK1AlaYtV',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://www.instagram.com',
    'Connection': 'keep-alive',
    'Referer': 'https://www.instagram.com/stories/0j4j/2573662312570101481/',
    'Cookie': 'ig_did=DE81B66B-7537-432D-A88C-E2FB4039FE7A; ig_nrcb=1; csrftoken=bSj6yMFvzPzkEhKPuMw8yNXDW4SExRbF; mid=YJ89AQALAAFL5TgDkM7tDBJ6FceC; ds_user_id=46730828610; sessionid=46730828610%3AbPXPffro0LHdge%3A3; shbid=9769; shbts=1621048758.1743295; rur=ATN',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Length': '3064'

}
url_log = 'https://www.instagram.com/accounts/login/ajax/'
hd_log = {
    'Host': 'www.instagram.com',
    'Connection': 'keep-alive',
    'X-IG-WWW-Claim': 'hmac.AR1b28zx1nUVtbXtODp2VBJaFeTHpFPOEQf1qAs1jWc4xRbn',
    'X-Instagram-AJAX': 'c795b4273c42',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'X-CSRFToken': 'FYwXgU48GhlD4f687jer4oy2YPdQ0WNv',
    'X-IG-App-ID': '936619743392459',
    'Sec-GPC': '1',
    'Origin': 'https://www.instagram.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.instagram.com/',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cookie': 'ig_did=DBCFBE81-32C0-4170-9B78-9C8B00EC4DC5; ig_nrcb=1; mid=YJ5WuQALAAFBcpLvXNtJaAicvjvJ; rur=FTW; csrftoken=FYwXgU48GhlD4f687jer4oy2YPdQ0WNv',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Length': '299'
}
data_log = {
    'username': usr,
    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{pas}'
}
req_log = abood.post(url_log, headers=hd_log, data=data_log)

if '"userId"' in req_log.text:
    clear()
    print(Fore.WHITE + 'login done')
    logs = req_log.cookies
    sessoind = logs['sessionid']
    uIdf = req_log.json()
    userid = uIdf['userId']
    csrftoken = logs['csrftoken']
    hd_rep = {
        'Host': 'www.instagram.com',
        'Connection': 'keep-alive',
        'X-IG-WWW-Claim': 'hmac.AR1b28zx1nUVtbXtODp2VBJaFeTHpFPOEQf1qAs1jWc4xRbn',
        'X-Instagram-AJAX': 'c795b4273c42',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'X-CSRFToken': csrftoken,
        'X-IG-App-ID': '936619743392459',
        'Sec-GPC': '1',
        'Origin': 'https://www.instagram.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': f'https://www.instagram.com/{target}/',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cookie': f'ig_did=DBCFBE81-32C0-4170-9B78-9C8B00EC4DC5; ig_nrcb=1; mid=YJ5WuQALAAFBcpLvXNtJaAicvjvJ; csrftoken={csrftoken}; ds_user_id={userid}; sessionid={sessoind}; rur=FTW',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Length': '3171'
    }
    url_id = 'https://www.instagram.com/{}/?__a=1'.format(target)
    req_id = abood.get(url_id).json()
    user_id = str(req_id['logging_page_id'])
    idd = user_id.split('_')[1]
    url_rep = 'https://www.instagram.com/reports/web/get_frx_prompt/'
    clear()
    rep = int(input(Fore.RED +
                    "[!] chose The  Type of Report:\n[!] 1-Self Injury\n[!] 2-Hate Speech or Symbols\n[!] 3-Violence Or Dangerous Organizations\n[!] 4-False Information\n[!] 5-Impersonation\n[!] 6- Nudity Or Pornography\n[!] 7-Spam\n[!] 8-I just don't like it\n[!] 9-Drugs\n[!] 10-Scam of fraud\n[!] chose (1-2-3-4-5-6-7-8-9-10) :"))
    if rep == 1:
        sl = 1
        data_report_self = f'entry_point=1&location=2&object_type=5&object_id={idd}&container_module=profilePage&context=%7B%22tags%22%3A%5B%22ig_report_account%22%2C%22ig_its_inappropriate%22%2C%22ig_self_injury_v3%22%5D%2C%22ixt_context_from_www%22%3A%22%7B%5C%22schema%5C%22%3A%5C%22ig_frx%5C%22%2C%5C%22session%5C%22%3A%5C%22%7B%5C%5C%5C%22location%5C%5C%5C%22%3A%5C%5C%5C%22ig_profile%5C%5C%5C%22%2C%5C%5C%5C%22entry_point%5C%5C%5C%22%3A%5C%5C%5C%22chevron_button%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%227132979d-2384-4599-aa47-73098d0db90e%5C%5C%5C%22%2C%5C%5C%5C%22tags%5C%5C%5C%22%3A%5B%5C%5C%5C%22ig_report_account%5C%5C%5C%22%2C%5C%5C%5C%22ig_its_inappropriate%5C%5C%5C%22%2C%5C%5C%5C%22ig_self_injury_v3%5C%5C%5C%22%5D%2C%5C%5C%5C%22object%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22user_id%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22{idd}%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22reporter_id%5C%5C%5C%22%3A17841400254313570%2C%5C%5C%5C%22responsible_id%5C%5C%5C%22%3A17841407054502701%2C%5C%5C%5C%22locale%5C%5C%5C%22%3A%5C%5C%5C%22en_US%5C%5C%5C%22%2C%5C%5C%5C%22app_platform%5C%5C%5C%22%3A11%2C%5C%5C%5C%22extra_data%5C%5C%5C%22%3A%7B%5C%5C%5C%22container_module%5C%5C%5C%22%3A%5C%5C%5C%22profilePage%5C%5C%5C%22%2C%5C%5C%5C%22app_version%5C%5C%5C%22%3A%5C%5C%5C%22None%5C%5C%5C%22%2C%5C%5C%5C%22is_dark_mode%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22app_id%5C%5C%5C%22%3A936619743392459%2C%5C%5C%5C%22sentry_feature_map%5C%5C%5C%22%3A%5C%5C%5C%22JrrU89kBGCUyMDAxOjhmODoxMTJkOjU5NmU6Y2RkNjo1MWVmOjVlZjo5MzgyGHNNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvOTEuMC40NDcyLjEyNCBTYWZhcmkvNTM3LjM2GAVlbl9VUxwYIDEzOWEzYjExNTc2ZDNmOTMxNTgzOWE3NWQ3NDUwMGEzGAAYIDk1ODBjNDlmYzM1MmRkOTcyZTA0MjMxMzRmNzFmMTJiGAAVjIwBADwsGBxZTUFnOGdBTEFBR1FqdEc5Ujd0NXAxR3pqZXVkFqDFhei9XgAcFRQrAAAiPDkVABkVADkVAAAYIDYyNDM2N2ZjMDc3OTQ3NTFhYmU5Yzk1YzgxOGMxMjhkFQIREhgPOTM2NjE5NzQzMzkyNDU5HBaEq6fwyv22PxhAODM1NmMzZDdhYmI5YjcxMGQ4ZDNjYTRlOTdjNjNjODMyNDQzYzI5YzdmMTUzNjAwMTQyMWU0MWRjOGI2ODYwZQAcFQQAEiggaHR0cHM6Ly93d3cuaW5zdGFncmFtLmNvbS92dnJtaC8YDlhNTEh0dHBSZXF1ZXN0ABbE0aHHlqqxPygcL3JlcG9ydHMvd2ViL2dldF9mcnhfcHJvbXB0LxYkFobkno4MAA%3D%3D%5C%5C%5C%22%2C%5C%5C%5C%22shopping_session_id%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22logging_extra%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22is_in_holdout%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22preloading_enabled%5C%5C%5C%22%3Anull%7D%2C%5C%5C%5C%22frx_feedback_submitted%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22additional_data%5C%5C%5C%22%3A%7B%7D%7D%5C%22%2C%5C%22screen%5C%22%3A%5C%22frx_policy_education%5C%22%2C%5C%22flow_info%5C%22%3A%5C%22%7B%5C%5C%5C%22nt%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22graphql%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22enrollment_info%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22ig%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22ig_container_module%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22profilePage%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%2210b49433-dfa1-4791-b069-0b7283824a76%5C%5C%5C%22%7D%5C%22%2C%5C%22previous_state%5C%22%3Anull%7D%22%7D&action_type=2&frx_prompt_request_type=4'
        while True:
            report_self_1 = abood.post(url_rep, headers=hd_rep, data=data_report_self)
            sl += 1
            if '"status":"ok"' in report_self_1.text:
                print(Fore.GREEN + f'report done >> {target} / At:{sl}')
            else:
                print(Fore.RED + report_self_1.text)
            time.sleep(slp)
    elif rep == 2:
        ht = 1
        data_report_hate = f'entry_point=1&location=2&object_type=5&object_id={idd}&container_module=profilePage&context=%7B%22tags%22%3A%5B%22ig_report_account%22%2C%22ig_its_inappropriate%22%2C%22ig_hate_speech_v3%22%5D%2C%22ixt_context_from_www%22%3A%22%7B%5C%22schema%5C%22%3A%5C%22ig_frx%5C%22%2C%5C%22session%5C%22%3A%5C%22%7B%5C%5C%5C%22location%5C%5C%5C%22%3A%5C%5C%5C%22ig_profile%5C%5C%5C%22%2C%5C%5C%5C%22entry_point%5C%5C%5C%22%3A%5C%5C%5C%22chevron_button%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%2205321f5c-ccf2-4a01-8a3f-2e46e39eecf6%5C%5C%5C%22%2C%5C%5C%5C%22tags%5C%5C%5C%22%3A%5B%5C%5C%5C%22ig_report_account%5C%5C%5C%22%2C%5C%5C%5C%22ig_its_inappropriate%5C%5C%5C%22%2C%5C%5C%5C%22ig_hate_speech_v3%5C%5C%5C%22%5D%2C%5C%5C%5C%22object%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22user_id%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22{idd}%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22reporter_id%5C%5C%5C%22%3A17841400254313570%2C%5C%5C%5C%22responsible_id%5C%5C%5C%22%3A17841407054502701%2C%5C%5C%5C%22locale%5C%5C%5C%22%3A%5C%5C%5C%22en_US%5C%5C%5C%22%2C%5C%5C%5C%22app_platform%5C%5C%5C%22%3A11%2C%5C%5C%5C%22extra_data%5C%5C%5C%22%3A%7B%5C%5C%5C%22container_module%5C%5C%5C%22%3A%5C%5C%5C%22profilePage%5C%5C%5C%22%2C%5C%5C%5C%22app_version%5C%5C%5C%22%3A%5C%5C%5C%22None%5C%5C%5C%22%2C%5C%5C%5C%22is_dark_mode%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22app_id%5C%5C%5C%22%3A936619743392459%2C%5C%5C%5C%22sentry_feature_map%5C%5C%5C%22%3A%5C%5C%5C%22JrrU89kBGCUyMDAxOjhmODoxMTJkOjU5NmU6Y2RkNjo1MWVmOjVlZjo5MzgyGHNNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvOTEuMC40NDcyLjEyNCBTYWZhcmkvNTM3LjM2GAVlbl9VUxwYIDEzOWEzYjExNTc2ZDNmOTMxNTgzOWE3NWQ3NDUwMGEzGAAYIDk1ODBjNDlmYzM1MmRkOTcyZTA0MjMxMzRmNzFmMTJiGAAVjIwBADwsGBxZTUFnOGdBTEFBR1FqdEc5Ujd0NXAxR3pqZXVkFqDFhei9XgAcFRQrAAAiPDkVABkVADkVAAAYIGUwNmZjM2JlOGNhMzQ4ZGFhY2I0YzYwYzRlN2NlYmZiFQIREhgPOTM2NjE5NzQzMzkyNDU5HBaEq6fwyv22PxhAODM1NmMzZDdhYmI5YjcxMGQ4ZDNjYTRlOTdjNjNjODMyNDQzYzI5YzdmMTUzNjAwMTQyMWU0MWRjOGI2ODYwZQAcFQQAEiggaHR0cHM6Ly93d3cuaW5zdGFncmFtLmNvbS92dnJtaC8YDlhNTEh0dHBSZXF1ZXN0ABbE0aHHlqqxPygcL3JlcG9ydHMvd2ViL2dldF9mcnhfcHJvbXB0LxYkFobkno4MAA%3D%3D%5C%5C%5C%22%2C%5C%5C%5C%22shopping_session_id%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22logging_extra%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22is_in_holdout%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22preloading_enabled%5C%5C%5C%22%3Anull%7D%2C%5C%5C%5C%22frx_feedback_submitted%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22additional_data%5C%5C%5C%22%3A%7B%7D%7D%5C%22%2C%5C%22screen%5C%22%3A%5C%22frx_policy_education%5C%22%2C%5C%22flow_info%5C%22%3A%5C%22%7B%5C%5C%5C%22nt%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22graphql%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22enrollment_info%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22ig%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22ig_container_module%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22profilePage%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%22438c2737-01c3-4f19-b521-3e132455d946%5C%5C%5C%22%7D%5C%22%2C%5C%22previous_state%5C%22%3Anull%7D%22%7D&action_type=2&frx_prompt_request_type=4'
        while True:
            report_hate = abood.post(url_rep, headers=hd_rep, data=data_report_hate)
            ht += 1
            if '"status":"ok"' in report_hate.text:
                print(Fore.GREEN + f'report done >> {target} / At:{ht}')
            else:
                print(Fore.RED + report_hate.text)
            time.sleep(slp)
    elif rep == 3:
        vo = 1
        while True:
            vo += 1
            dat_vo = f'entry_point=1&location=2&object_type=5&object_id={idd}&container_module=profilePage&context=%7B%22tags%22%3A%5B%22ig_report_account%22%2C%22ig_its_inappropriate%22%2C%22ig_violence_parent%22%5D%2C%22ixt_context_from_www%22%3A%22%7B%5C%22schema%5C%22%3A%5C%22ig_frx%5C%22%2C%5C%22session%5C%22%3A%5C%22%7B%5C%5C%5C%22location%5C%5C%5C%22%3A%5C%5C%5C%22ig_profile%5C%5C%5C%22%2C%5C%5C%5C%22entry_point%5C%5C%5C%22%3A%5C%5C%5C%22chevron_button%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%22d711dede-368e-4dd0-895a-4ccadaf880ff%5C%5C%5C%22%2C%5C%5C%5C%22tags%5C%5C%5C%22%3A%5B%5C%5C%5C%22ig_report_account%5C%5C%5C%22%2C%5C%5C%5C%22ig_its_inappropriate%5C%5C%5C%22%2C%5C%5C%5C%22ig_violence_parent%5C%5C%5C%22%5D%2C%5C%5C%5C%22object%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22user_id%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22{idd}%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22reporter_id%5C%5C%5C%22%3A17841400254313570%2C%5C%5C%5C%22responsible_id%5C%5C%5C%22%3A17841407054502701%2C%5C%5C%5C%22locale%5C%5C%5C%22%3A%5C%5C%5C%22en_US%5C%5C%5C%22%2C%5C%5C%5C%22app_platform%5C%5C%5C%22%3A11%2C%5C%5C%5C%22extra_data%5C%5C%5C%22%3A%7B%5C%5C%5C%22container_module%5C%5C%5C%22%3A%5C%5C%5C%22profilePage%5C%5C%5C%22%2C%5C%5C%5C%22app_version%5C%5C%5C%22%3A%5C%5C%5C%22None%5C%5C%5C%22%2C%5C%5C%5C%22is_dark_mode%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22app_id%5C%5C%5C%22%3A936619743392459%2C%5C%5C%5C%22sentry_feature_map%5C%5C%5C%22%3A%5C%5C%5C%22JrrU89kBGCUyMDAxOjhmODoxMTJkOjU5NmU6Y2RkNjo1MWVmOjVlZjo5MzgyGHNNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvOTEuMC40NDcyLjEyNCBTYWZhcmkvNTM3LjM2GAVlbl9VUxwYIDEzOWEzYjExNTc2ZDNmOTMxNTgzOWE3NWQ3NDUwMGEzGAAYIDk1ODBjNDlmYzM1MmRkOTcyZTA0MjMxMzRmNzFmMTJiGAAVjIwBADwsGBxZTUFnOGdBTEFBR1FqdEc5Ujd0NXAxR3pqZXVkFqDFhei9XgAcFRQrAAAiPDkVABkVADkVAAAYIGM0ZjliYTNhY2MxODQxZTY4ZTBmYjNkOWE4OGRjMjk4FQIREhgPOTM2NjE5NzQzMzkyNDU5HBaEq6fwyv22PxhAODM1NmMzZDdhYmI5YjcxMGQ4ZDNjYTRlOTdjNjNjODMyNDQzYzI5YzdmMTUzNjAwMTQyMWU0MWRjOGI2ODYwZQAcFQQAEiggaHR0cHM6Ly93d3cuaW5zdGFncmFtLmNvbS92dnJtaC8YDlhNTEh0dHBSZXF1ZXN0ABbE0aHHlqqxPygcL3JlcG9ydHMvd2ViL2dldF9mcnhfcHJvbXB0LxYkFobkno4MAA%3D%3D%5C%5C%5C%22%2C%5C%5C%5C%22shopping_session_id%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22logging_extra%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22is_in_holdout%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22preloading_enabled%5C%5C%5C%22%3Anull%7D%2C%5C%5C%5C%22frx_feedback_submitted%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22additional_data%5C%5C%5C%22%3A%7B%7D%7D%5C%22%2C%5C%22screen%5C%22%3A%5C%22frx_tag_selection_screen%5C%22%2C%5C%22flow_info%5C%22%3A%5C%22%7B%5C%5C%5C%22nt%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22graphql%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22enrollment_info%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22ig%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22ig_container_module%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22profilePage%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%22c3410aad-94fd-46d8-8e18-3649367dbbd4%5C%5C%5C%22%7D%5C%22%2C%5C%22previous_state%5C%22%3Anull%7D%22%7D&selected_tag_types=%5B%22ig_violence_threat%22%5D&action_type=2&frx_prompt_request_type=2'
            rep_vo = abood.post(url_rep, headers=hd_rep, data=dat_vo)
            if '"status":"ok"' in rep_vo.text:
                print(Fore.GREEN + f'report done >> {target} / At:{vo}')
            else:
                print(Fore.RED + rep_vo.text)
            time.sleep(slp)
    elif rep == 4:
        fl = 1
        data_false = f'entry_point=1&location=2&object_type=5&object_id={idd}&container_module=profilePage&context=%7B%22tags%22%3A%5B%22ig_report_account%22%2C%22ig_its_inappropriate%22%5D%2C%22ixt_context_from_www%22%3A%22%7B%5C%22schema%5C%22%3A%5C%22ig_frx%5C%22%2C%5C%22session%5C%22%3A%5C%22%7B%5C%5C%5C%22location%5C%5C%5C%22%3A%5C%5C%5C%22ig_profile%5C%5C%5C%22%2C%5C%5C%5C%22entry_point%5C%5C%5C%22%3A%5C%5C%5C%22chevron_button%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%22625e6ccf-8c92-4aad-9abb-77d97c9a8d4c%5C%5C%5C%22%2C%5C%5C%5C%22tags%5C%5C%5C%22%3A%5B%5C%5C%5C%22ig_report_account%5C%5C%5C%22%2C%5C%5C%5C%22ig_its_inappropriate%5C%5C%5C%22%5D%2C%5C%5C%5C%22object%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22user_id%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22{idd}%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22reporter_id%5C%5C%5C%22%3A17841400254313570%2C%5C%5C%5C%22responsible_id%5C%5C%5C%22%3A17841407054502701%2C%5C%5C%5C%22locale%5C%5C%5C%22%3A%5C%5C%5C%22en_US%5C%5C%5C%22%2C%5C%5C%5C%22app_platform%5C%5C%5C%22%3A11%2C%5C%5C%5C%22extra_data%5C%5C%5C%22%3A%7B%5C%5C%5C%22container_module%5C%5C%5C%22%3A%5C%5C%5C%22profilePage%5C%5C%5C%22%2C%5C%5C%5C%22app_version%5C%5C%5C%22%3A%5C%5C%5C%22None%5C%5C%5C%22%2C%5C%5C%5C%22is_dark_mode%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22app_id%5C%5C%5C%22%3A936619743392459%2C%5C%5C%5C%22sentry_feature_map%5C%5C%5C%22%3A%5C%5C%5C%22JrrU89kBGCUyMDAxOjhmODoxMTJkOjU5NmU6Y2RkNjo1MWVmOjVlZjo5MzgyGHNNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvOTEuMC40NDcyLjEyNCBTYWZhcmkvNTM3LjM2GAVlbl9VUxwYIDEzOWEzYjExNTc2ZDNmOTMxNTgzOWE3NWQ3NDUwMGEzGAAYIDk1ODBjNDlmYzM1MmRkOTcyZTA0MjMxMzRmNzFmMTJiGAAVjIwBADwsGBxZTUFnOGdBTEFBR1FqdEc5Ujd0NXAxR3pqZXVkFqDFhei9XgAcFRQrAAAiPDkVABkVADkVAAAYIDEwMjI5NWY3ZjEyZTQzNWFiMzJhNzQwZWJkMGMwM2FkFQIREhgPOTM2NjE5NzQzMzkyNDU5HBaEq6fwyv22PxhAODM1NmMzZDdhYmI5YjcxMGQ4ZDNjYTRlOTdjNjNjODMyNDQzYzI5YzdmMTUzNjAwMTQyMWU0MWRjOGI2ODYwZQAcFQQAEiggaHR0cHM6Ly93d3cuaW5zdGFncmFtLmNvbS92dnJtaC8YDlhNTEh0dHBSZXF1ZXN0ABbE0aHHlqqxPygcL3JlcG9ydHMvd2ViL2dldF9mcnhfcHJvbXB0LxYkFobkno4MAA%3D%3D%5C%5C%5C%22%2C%5C%5C%5C%22shopping_session_id%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22logging_extra%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22is_in_holdout%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22preloading_enabled%5C%5C%5C%22%3Anull%7D%2C%5C%5C%5C%22frx_feedback_submitted%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22additional_data%5C%5C%5C%22%3A%7B%7D%7D%5C%22%2C%5C%22screen%5C%22%3A%5C%22frx_tag_selection_screen%5C%22%2C%5C%22flow_info%5C%22%3A%5C%22%7B%5C%5C%5C%22nt%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22graphql%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22enrollment_info%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22ig%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22ig_container_module%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22profilePage%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%225048bde2-cfb0-4fa7-b063-872143f557bc%5C%5C%5C%22%7D%5C%22%2C%5C%22previous_state%5C%22%3Anull%7D%22%7D&selected_tag_types=%5B%22ig_false_news%22%5D&frx_prompt_request_type=2'
        while True:
            fl += 1
            rep_false = abood.post(url_rep, headers=hd_rep, data=data_false)
            if '"status":"ok"' in rep_false.text:
                print(Fore.GREEN + f'report done >> {target} / At:{fl}')
            else:
                print(Fore.RED + rep_false.text)
            time.sleep(slp)
    elif rep == 5:
        clear()
        cho22 = int(input(Fore.RED + '[!] 1-me\n[!] 2-someone i know\n[!] chose(1-2) :'))
        if cho22 == 1:
            beme = 1
            dat_by_me = f'entry_point=1&location=2&object_type=5&object_id={idd}&container_module=profilePage&context=%7B%22tags%22%3A%5B%22ig_report_account%22%2C%22ig_user_impersonation%22%5D%2C%22ixt_context_from_www%22%3A%22%7B%5C%22schema%5C%22%3A%5C%22ig_frx%5C%22%2C%5C%22session%5C%22%3A%5C%22%7B%5C%5C%5C%22location%5C%5C%5C%22%3A%5C%5C%5C%22ig_profile%5C%5C%5C%22%2C%5C%5C%5C%22entry_point%5C%5C%5C%22%3A%5C%5C%5C%22chevron_button%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%22a543b74d-be47-468e-ac95-9189dd4b9d4f%5C%5C%5C%22%2C%5C%5C%5C%22tags%5C%5C%5C%22%3A%5B%5C%5C%5C%22ig_report_account%5C%5C%5C%22%2C%5C%5C%5C%22ig_user_impersonation%5C%5C%5C%22%5D%2C%5C%5C%5C%22object%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22user_id%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22{idd}%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22reporter_id%5C%5C%5C%22%3A17841400254313570%2C%5C%5C%5C%22responsible_id%5C%5C%5C%22%3A17841407054502701%2C%5C%5C%5C%22locale%5C%5C%5C%22%3A%5C%5C%5C%22en_US%5C%5C%5C%22%2C%5C%5C%5C%22app_platform%5C%5C%5C%22%3A11%2C%5C%5C%5C%22extra_data%5C%5C%5C%22%3A%7B%5C%5C%5C%22container_module%5C%5C%5C%22%3A%5C%5C%5C%22profilePage%5C%5C%5C%22%2C%5C%5C%5C%22app_version%5C%5C%5C%22%3A%5C%5C%5C%22None%5C%5C%5C%22%2C%5C%5C%5C%22is_dark_mode%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22app_id%5C%5C%5C%22%3A936619743392459%2C%5C%5C%5C%22sentry_feature_map%5C%5C%5C%22%3A%5C%5C%5C%22JrrU89kBGCUyMDAxOjhmODoxMTJkOjU5NmU6Y2RkNjo1MWVmOjVlZjo5MzgyGHNNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvOTEuMC40NDcyLjEyNCBTYWZhcmkvNTM3LjM2GAVlbl9VUxwYIDEzOWEzYjExNTc2ZDNmOTMxNTgzOWE3NWQ3NDUwMGEzGAAYIDk1ODBjNDlmYzM1MmRkOTcyZTA0MjMxMzRmNzFmMTJiGAAVjIwBADwsGBxZTUFnOGdBTEFBR1FqdEc5Ujd0NXAxR3pqZXVkFqDFhei9XgAcFRQrAAAiPDkVABkVADkVAAAYIDk0MzQ2NzQ0ODdiNjQ1NmU5ODAzMmVlMDQ0ZTU2NjdjFQIREhgPOTM2NjE5NzQzMzkyNDU5HBaEq6fwyv22PxhAODM1NmMzZDdhYmI5YjcxMGQ4ZDNjYTRlOTdjNjNjODMyNDQzYzI5YzdmMTUzNjAwMTQyMWU0MWRjOGI2ODYwZQAcFQQAEiggaHR0cHM6Ly93d3cuaW5zdGFncmFtLmNvbS92dnJtaC8YDlhNTEh0dHBSZXF1ZXN0ABbE0aHHlqqxPygcL3JlcG9ydHMvd2ViL2dldF9mcnhfcHJvbXB0LxYkFobkno4MAA%3D%3D%5C%5C%5C%22%2C%5C%5C%5C%22shopping_session_id%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22logging_extra%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22is_in_holdout%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22preloading_enabled%5C%5C%5C%22%3Anull%7D%2C%5C%5C%5C%22frx_feedback_submitted%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22additional_data%5C%5C%5C%22%3A%7B%7D%7D%5C%22%2C%5C%22screen%5C%22%3A%5C%22frx_tag_selection_screen%5C%22%2C%5C%22flow_info%5C%22%3A%5C%22%7B%5C%5C%5C%22nt%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22graphql%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22enrollment_info%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22ig%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22ig_container_module%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22profilePage%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%22a255a6bf-1fb2-4acf-af4d-db4a65562aa0%5C%5C%5C%22%7D%5C%22%2C%5C%22previous_state%5C%22%3Anull%7D%22%7D&selected_tag_types=%5B%22ig_user_impersonation_me%22%5D&action_type=2&frx_prompt_request_type=2'
            while True:
                beme += 1
                rep_by_me = abood.post(url_rep, headers=hd_rep, data=dat_by_me)
                if '"status":"ok"' in rep_by_me.text:
                    print(Fore.GREEN + f'report done >> {target} / At:{beme}')
                else:
                    print(Fore.RED + rep_by_me.text)
                time.sleep(slp)
        if cho22 == 2:
            brso = 1
            dat_by_so = f'entry_point=1&location=2&object_type=5&object_id={idd}&container_module=profilePage&context=%7B%22tags%22%3A%5B%22ig_report_account%22%2C%22ig_user_impersonation%22%5D%2C%22ixt_context_from_www%22%3A%22%7B%5C%22schema%5C%22%3A%5C%22ig_frx%5C%22%2C%5C%22session%5C%22%3A%5C%22%7B%5C%5C%5C%22location%5C%5C%5C%22%3A%5C%5C%5C%22ig_profile%5C%5C%5C%22%2C%5C%5C%5C%22entry_point%5C%5C%5C%22%3A%5C%5C%5C%22chevron_button%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%22a489f1ff-819d-44bc-b84d-8d7857694209%5C%5C%5C%22%2C%5C%5C%5C%22tags%5C%5C%5C%22%3A%5B%5C%5C%5C%22ig_report_account%5C%5C%5C%22%2C%5C%5C%5C%22ig_user_impersonation%5C%5C%5C%22%5D%2C%5C%5C%5C%22object%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22user_id%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22{idd}%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22reporter_id%5C%5C%5C%22%3A17841400254313570%2C%5C%5C%5C%22responsible_id%5C%5C%5C%22%3A17841407054502701%2C%5C%5C%5C%22locale%5C%5C%5C%22%3A%5C%5C%5C%22en_US%5C%5C%5C%22%2C%5C%5C%5C%22app_platform%5C%5C%5C%22%3A11%2C%5C%5C%5C%22extra_data%5C%5C%5C%22%3A%7B%5C%5C%5C%22container_module%5C%5C%5C%22%3A%5C%5C%5C%22profilePage%5C%5C%5C%22%2C%5C%5C%5C%22app_version%5C%5C%5C%22%3A%5C%5C%5C%22None%5C%5C%5C%22%2C%5C%5C%5C%22is_dark_mode%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22app_id%5C%5C%5C%22%3A936619743392459%2C%5C%5C%5C%22sentry_feature_map%5C%5C%5C%22%3A%5C%5C%5C%22JrrU89kBGCUyMDAxOjhmODoxMTJkOjU5NmU6Y2RkNjo1MWVmOjVlZjo5MzgyGHNNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvOTEuMC40NDcyLjEyNCBTYWZhcmkvNTM3LjM2GAVlbl9VUxwYIDEzOWEzYjExNTc2ZDNmOTMxNTgzOWE3NWQ3NDUwMGEzGAAYIDk1ODBjNDlmYzM1MmRkOTcyZTA0MjMxMzRmNzFmMTJiGAAVjIwBADwsGBxZTUFnOGdBTEFBR1FqdEc5Ujd0NXAxR3pqZXVkFqDFhei9XgAcFRQrAAAiPDkVABkVADkVAAAYIGUwM2UwNmUxYmMyZjRiNWE5N2RmMDEzODBjYTM3NzA4FQIREhgPOTM2NjE5NzQzMzkyNDU5HBaEq6fwyv22PxhAODM1NmMzZDdhYmI5YjcxMGQ4ZDNjYTRlOTdjNjNjODMyNDQzYzI5YzdmMTUzNjAwMTQyMWU0MWRjOGI2ODYwZQAcFQQAEiggaHR0cHM6Ly93d3cuaW5zdGFncmFtLmNvbS92dnJtaC8YDlhNTEh0dHBSZXF1ZXN0ABbE0aHHlqqxPygcL3JlcG9ydHMvd2ViL2dldF9mcnhfcHJvbXB0LxYkFobkno4MAA%3D%3D%5C%5C%5C%22%2C%5C%5C%5C%22shopping_session_id%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22logging_extra%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22is_in_holdout%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22preloading_enabled%5C%5C%5C%22%3Anull%7D%2C%5C%5C%5C%22frx_feedback_submitted%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22additional_data%5C%5C%5C%22%3A%7B%7D%7D%5C%22%2C%5C%22screen%5C%22%3A%5C%22frx_tag_selection_screen%5C%22%2C%5C%22flow_info%5C%22%3A%5C%22%7B%5C%5C%5C%22nt%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22graphql%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22enrollment_info%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22ig%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22ig_container_module%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22profilePage%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%225a63466a-55f0-4b10-a2e9-ae5df9e2c4b8%5C%5C%5C%22%7D%5C%22%2C%5C%22previous_state%5C%22%3Anull%7D%22%7D&selected_tag_types=%5B%22ig_user_impersonation_someone_i_know%22%5D&action_type=2&frx_prompt_request_type=2'
            while True:
                brso += 1
                rep_by_so = abood.post(url_rep, headers=hd_rep, data=dat_by_so)
                if '"status":"ok"' in rep_by_so.text:
                    print(Fore.GREEN + f'report done >> {target} / At:{brso}')
                else:
                    print(Fore.RED + rep_by_so.text)
                time.sleep(slp)
    elif rep == 6:
        nud = 1
        data_nud = f'entry_point=1&location=2&object_type=5&object_id={idd}&container_module=profilePage&context=%7B%22tags%22%3A%5B%22ig_report_account%22%2C%22ig_its_inappropriate%22%2C%22ig_nudity_v2%22%5D%2C%22ixt_context_from_www%22%3A%22%7B%5C%22schema%5C%22%3A%5C%22ig_frx%5C%22%2C%5C%22session%5C%22%3A%5C%22%7B%5C%5C%5C%22location%5C%5C%5C%22%3A%5C%5C%5C%22ig_profile%5C%5C%5C%22%2C%5C%5C%5C%22entry_point%5C%5C%5C%22%3A%5C%5C%5C%22chevron_button%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%22cd65fc3e-7d22-4027-a980-1d81a706363f%5C%5C%5C%22%2C%5C%5C%5C%22tags%5C%5C%5C%22%3A%5B%5C%5C%5C%22ig_report_account%5C%5C%5C%22%2C%5C%5C%5C%22ig_its_inappropriate%5C%5C%5C%22%2C%5C%5C%5C%22ig_nudity_v2%5C%5C%5C%22%5D%2C%5C%5C%5C%22object%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22user_id%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22{idd}%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22reporter_id%5C%5C%5C%22%3A17841400254313570%2C%5C%5C%5C%22responsible_id%5C%5C%5C%22%3A17841407054502701%2C%5C%5C%5C%22locale%5C%5C%5C%22%3A%5C%5C%5C%22en_US%5C%5C%5C%22%2C%5C%5C%5C%22app_platform%5C%5C%5C%22%3A11%2C%5C%5C%5C%22extra_data%5C%5C%5C%22%3A%7B%5C%5C%5C%22container_module%5C%5C%5C%22%3A%5C%5C%5C%22profilePage%5C%5C%5C%22%2C%5C%5C%5C%22app_version%5C%5C%5C%22%3A%5C%5C%5C%22None%5C%5C%5C%22%2C%5C%5C%5C%22is_dark_mode%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22app_id%5C%5C%5C%22%3A936619743392459%2C%5C%5C%5C%22sentry_feature_map%5C%5C%5C%22%3A%5C%5C%5C%22JrrU89kBGCUyMDAxOjhmODoxMTJkOjU5NmU6Y2RkNjo1MWVmOjVlZjo5MzgyGHNNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvOTEuMC40NDcyLjEyNCBTYWZhcmkvNTM3LjM2GAVlbl9VUxwYIDEzOWEzYjExNTc2ZDNmOTMxNTgzOWE3NWQ3NDUwMGEzGAAYIDk1ODBjNDlmYzM1MmRkOTcyZTA0MjMxMzRmNzFmMTJiGAAVjIwBADwsGBxZTUFnOGdBTEFBR1FqdEc5Ujd0NXAxR3pqZXVkFqDFhei9XgAcFRQrAAAiPDkVABkVADkVAAAYIDEyM2I4ZDZmMGQ1YTQwMDFiYWU0ODE5MDJjMWU3NTM4FQIREhgPOTM2NjE5NzQzMzkyNDU5HBaEq6fwyv22PxhAODM1NmMzZDdhYmI5YjcxMGQ4ZDNjYTRlOTdjNjNjODMyNDQzYzI5YzdmMTUzNjAwMTQyMWU0MWRjOGI2ODYwZQAcFQQAEiggaHR0cHM6Ly93d3cuaW5zdGFncmFtLmNvbS92dnJtaC8YDlhNTEh0dHBSZXF1ZXN0ABbE0aHHlqqxPygcL3JlcG9ydHMvd2ViL2dldF9mcnhfcHJvbXB0LxYkFobkno4MAA%3D%3D%5C%5C%5C%22%2C%5C%5C%5C%22shopping_session_id%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22logging_extra%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22is_in_holdout%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22preloading_enabled%5C%5C%5C%22%3Anull%7D%2C%5C%5C%5C%22frx_feedback_submitted%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22additional_data%5C%5C%5C%22%3A%7B%7D%7D%5C%22%2C%5C%22screen%5C%22%3A%5C%22frx_tag_selection_screen%5C%22%2C%5C%22flow_info%5C%22%3A%5C%22%7B%5C%5C%5C%22nt%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22graphql%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22enrollment_info%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22ig%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22ig_container_module%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22profilePage%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%22e24a7d12-1fa3-4b06-b825-e7f374e2c315%5C%5C%5C%22%7D%5C%22%2C%5C%22previous_state%5C%22%3Anull%7D%22%7D&selected_tag_types=%5B%22ig_nudity_or_pornography_v3%22%5D&action_type=2&frx_prompt_request_type=2'
        while True:
            nud += 1
            rep_nud = abood.post(url_rep, headers=hd_rep, data=data_nud)
            if '"status":"ok"' in rep_nud.text:
                print(Fore.GREEN + f'report done >> {target} / At:{nud}')
            else:
                print(Fore.RED + rep_nud.text)
            time.sleep(slp)
    elif rep == 7:
        sp = 1
        dat_spam = f'entry_point=1&location=2&object_type=5&object_id={idd}&container_module=profilePage&context=%7B%22tags%22%3A%5B%22ig_report_account%22%2C%22ig_its_inappropriate%22%5D%2C%22ixt_context_from_www%22%3A%22%7B%5C%22schema%5C%22%3A%5C%22ig_frx%5C%22%2C%5C%22session%5C%22%3A%5C%22%7B%5C%5C%5C%22location%5C%5C%5C%22%3A%5C%5C%5C%22ig_profile%5C%5C%5C%22%2C%5C%5C%5C%22entry_point%5C%5C%5C%22%3A%5C%5C%5C%22chevron_button%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%2200f2bbf6-b711-435f-a84c-2f5614524fec%5C%5C%5C%22%2C%5C%5C%5C%22tags%5C%5C%5C%22%3A%5B%5C%5C%5C%22ig_report_account%5C%5C%5C%22%2C%5C%5C%5C%22ig_its_inappropriate%5C%5C%5C%22%5D%2C%5C%5C%5C%22object%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22user_id%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22{idd}%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22reporter_id%5C%5C%5C%22%3A17841400254313570%2C%5C%5C%5C%22responsible_id%5C%5C%5C%22%3A17841407054502701%2C%5C%5C%5C%22locale%5C%5C%5C%22%3A%5C%5C%5C%22en_US%5C%5C%5C%22%2C%5C%5C%5C%22app_platform%5C%5C%5C%22%3A11%2C%5C%5C%5C%22extra_data%5C%5C%5C%22%3A%7B%5C%5C%5C%22container_module%5C%5C%5C%22%3A%5C%5C%5C%22profilePage%5C%5C%5C%22%2C%5C%5C%5C%22app_version%5C%5C%5C%22%3A%5C%5C%5C%22None%5C%5C%5C%22%2C%5C%5C%5C%22is_dark_mode%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22app_id%5C%5C%5C%22%3A936619743392459%2C%5C%5C%5C%22sentry_feature_map%5C%5C%5C%22%3A%5C%5C%5C%22JrrU89kBGCUyMDAxOjhmODoxMTJkOjU5NmU6Y2RkNjo1MWVmOjVlZjo5MzgyGHNNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvOTEuMC40NDcyLjEyNCBTYWZhcmkvNTM3LjM2GAVlbl9VUxwYIDEzOWEzYjExNTc2ZDNmOTMxNTgzOWE3NWQ3NDUwMGEzGAAYIDk1ODBjNDlmYzM1MmRkOTcyZTA0MjMxMzRmNzFmMTJiGAAVjIwBADwsGBxZTUFnOGdBTEFBR1FqdEc5Ujd0NXAxR3pqZXVkFqDFhei9XgAcFRQrAAAiPDkVABkVADkVAAAYIDNlZTViOWRjYThmNjQzODFiNGUxZGU2NmJiNzA4YTMyFQIREhgPOTM2NjE5NzQzMzkyNDU5HBaEq6fwyv22PxhAODM1NmMzZDdhYmI5YjcxMGQ4ZDNjYTRlOTdjNjNjODMyNDQzYzI5YzdmMTUzNjAwMTQyMWU0MWRjOGI2ODYwZQAcFQQAEiggaHR0cHM6Ly93d3cuaW5zdGFncmFtLmNvbS92dnJtaC8YDlhNTEh0dHBSZXF1ZXN0ABbE0aHHlqqxPygcL3JlcG9ydHMvd2ViL2dldF9mcnhfcHJvbXB0LxYkFobkno4MAA%3D%3D%5C%5C%5C%22%2C%5C%5C%5C%22shopping_session_id%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22logging_extra%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22is_in_holdout%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22preloading_enabled%5C%5C%5C%22%3Anull%7D%2C%5C%5C%5C%22frx_feedback_submitted%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22additional_data%5C%5C%5C%22%3A%7B%7D%7D%5C%22%2C%5C%22screen%5C%22%3A%5C%22frx_tag_selection_screen%5C%22%2C%5C%22flow_info%5C%22%3A%5C%22%7B%5C%5C%5C%22nt%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22graphql%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22enrollment_info%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22ig%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22ig_container_module%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22profilePage%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%224cb56706-81b0-4740-8566-3d6e708d018a%5C%5C%5C%22%7D%5C%22%2C%5C%22previous_state%5C%22%3Anull%7D%22%7D&selected_tag_types=%5B%22ig_spam_v3%22%5D&frx_prompt_request_type=2'
        while True:
            sp += 1
            rep_spam = abood.post(url_rep, headers=hd_rep, data=dat_spam)
            if '"status":"ok"' in rep_spam.text:
                print(Fore.GREEN + f'report done >> {target} / At:{sp}')
            else:
                print(Fore.RED + rep_spam.text)
            time.sleep(slp)
    elif rep == 8:
        ijd = 1
        data_report_ijd = f'entry_point=1&location=2&object_type=5&object_id={idd}&container_module=profilePage&context=%7B%22tags%22%3A%5B%22ig_report_account%22%2C%22ig_its_inappropriate%22%5D%2C%22ixt_context_from_www%22%3A%22%7B%5C%22schema%5C%22%3A%5C%22ig_frx%5C%22%2C%5C%22session%5C%22%3A%5C%22%7B%5C%5C%5C%22location%5C%5C%5C%22%3A%5C%5C%5C%22ig_profile%5C%5C%5C%22%2C%5C%5C%5C%22entry_point%5C%5C%5C%22%3A%5C%5C%5C%22chevron_button%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%2242beb9a2-bea8-409c-8d6d-21c3bac4eb04%5C%5C%5C%22%2C%5C%5C%5C%22tags%5C%5C%5C%22%3A%5B%5C%5C%5C%22ig_report_account%5C%5C%5C%22%2C%5C%5C%5C%22ig_its_inappropriate%5C%5C%5C%22%5D%2C%5C%5C%5C%22object%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22user_id%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22{idd}%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22reporter_id%5C%5C%5C%22%3A17841400254313570%2C%5C%5C%5C%22responsible_id%5C%5C%5C%22%3A17841407054502701%2C%5C%5C%5C%22locale%5C%5C%5C%22%3A%5C%5C%5C%22en_US%5C%5C%5C%22%2C%5C%5C%5C%22app_platform%5C%5C%5C%22%3A11%2C%5C%5C%5C%22extra_data%5C%5C%5C%22%3A%7B%5C%5C%5C%22container_module%5C%5C%5C%22%3A%5C%5C%5C%22profilePage%5C%5C%5C%22%2C%5C%5C%5C%22app_version%5C%5C%5C%22%3A%5C%5C%5C%22None%5C%5C%5C%22%2C%5C%5C%5C%22is_dark_mode%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22app_id%5C%5C%5C%22%3A936619743392459%2C%5C%5C%5C%22sentry_feature_map%5C%5C%5C%22%3A%5C%5C%5C%22JrrU89kBGCUyMDAxOjhmODoxMTJkOjU5NmU6Y2RkNjo1MWVmOjVlZjo5MzgyGHNNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvOTEuMC40NDcyLjEyNCBTYWZhcmkvNTM3LjM2GAVlbl9VUxwYIDEzOWEzYjExNTc2ZDNmOTMxNTgzOWE3NWQ3NDUwMGEzGAAYIDk1ODBjNDlmYzM1MmRkOTcyZTA0MjMxMzRmNzFmMTJiGAAVjIwBADwsGBxZTUFnOGdBTEFBR1FqdEc5Ujd0NXAxR3pqZXVkFqDFhei9XgAcFRQrAAAiPDkVABkVADkVAAAYIDNiYjRkZjNmMTFhZTRjODE4ZGEzNjkzOTllM2NmNTA0FQIREhgPOTM2NjE5NzQzMzkyNDU5HBaEq6fwyv22PxhAODM1NmMzZDdhYmI5YjcxMGQ4ZDNjYTRlOTdjNjNjODMyNDQzYzI5YzdmMTUzNjAwMTQyMWU0MWRjOGI2ODYwZQAcFQQAEiggaHR0cHM6Ly93d3cuaW5zdGFncmFtLmNvbS92dnJtaC8YDlhNTEh0dHBSZXF1ZXN0ABbE0aHHlqqxPygcL3JlcG9ydHMvd2ViL2dldF9mcnhfcHJvbXB0LxYkFobkno4MAA%3D%3D%5C%5C%5C%22%2C%5C%5C%5C%22shopping_session_id%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22logging_extra%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22is_in_holdout%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22preloading_enabled%5C%5C%5C%22%3Anull%7D%2C%5C%5C%5C%22frx_feedback_submitted%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22additional_data%5C%5C%5C%22%3A%7B%7D%7D%5C%22%2C%5C%22screen%5C%22%3A%5C%22frx_tag_selection_screen%5C%22%2C%5C%22flow_info%5C%22%3A%5C%22%7B%5C%5C%5C%22nt%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22graphql%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22enrollment_info%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22ig%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22ig_container_module%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22profilePage%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%22c45f193f-0889-4165-9736-b76f97e5d60c%5C%5C%5C%22%7D%5C%22%2C%5C%22previous_state%5C%22%3Anull%7D%22%7D&selected_tag_types=%5B%22ig_i_dont_like_it_v3%22%5D&frx_prompt_request_type=2'
        while True:
            report_ijd = abood.post(url_rep, headers=hd_rep, data=data_report_ijd)
            ijd += 1
            if '"status":"ok"' in report_ijd.text:
                print(Fore.GREEN + f'report done >> {target} / At:{ijd}')
            else:
                print(Fore.RED + "err report")
    elif rep == 9:
        Drugs = 1
        data_report_Drugs = f'entry_point=1&location=2&object_type=5&object_id={idd}&container_module=profilePage&context=%7B%22tags%22%3A%5B%22ig_report_account%22%2C%22ig_its_inappropriate%22%2C%22ig_sale_of_illegal_or_regulated_goods_v3%22%5D%2C%22ixt_context_from_www%22%3A%22%7B%5C%22schema%5C%22%3A%5C%22ig_frx%5C%22%2C%5C%22session%5C%22%3A%5C%22%7B%5C%5C%5C%22location%5C%5C%5C%22%3A%5C%5C%5C%22ig_profile%5C%5C%5C%22%2C%5C%5C%5C%22entry_point%5C%5C%5C%22%3A%5C%5C%5C%22chevron_button%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%22316d0414-b0cb-419e-9839-f3bac8faac71%5C%5C%5C%22%2C%5C%5C%5C%22tags%5C%5C%5C%22%3A%5B%5C%5C%5C%22ig_report_account%5C%5C%5C%22%2C%5C%5C%5C%22ig_its_inappropriate%5C%5C%5C%22%2C%5C%5C%5C%22ig_sale_of_illegal_or_regulated_goods_v3%5C%5C%5C%22%5D%2C%5C%5C%5C%22object%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22user_id%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22{idd}%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22reporter_id%5C%5C%5C%22%3A17841400254313570%2C%5C%5C%5C%22responsible_id%5C%5C%5C%22%3A17841407054502701%2C%5C%5C%5C%22locale%5C%5C%5C%22%3A%5C%5C%5C%22en_US%5C%5C%5C%22%2C%5C%5C%5C%22app_platform%5C%5C%5C%22%3A11%2C%5C%5C%5C%22extra_data%5C%5C%5C%22%3A%7B%5C%5C%5C%22container_module%5C%5C%5C%22%3A%5C%5C%5C%22profilePage%5C%5C%5C%22%2C%5C%5C%5C%22app_version%5C%5C%5C%22%3A%5C%5C%5C%22None%5C%5C%5C%22%2C%5C%5C%5C%22is_dark_mode%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22app_id%5C%5C%5C%22%3A936619743392459%2C%5C%5C%5C%22sentry_feature_map%5C%5C%5C%22%3A%5C%5C%5C%22JrrU89kBGCUyMDAxOjhmODoxMTJkOjU5NmU6Y2RkNjo1MWVmOjVlZjo5MzgyGHNNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvOTEuMC40NDcyLjEyNCBTYWZhcmkvNTM3LjM2GAVlbl9VUxwYIDEzOWEzYjExNTc2ZDNmOTMxNTgzOWE3NWQ3NDUwMGEzGAAYIDk1ODBjNDlmYzM1MmRkOTcyZTA0MjMxMzRmNzFmMTJiGAAVjIwBADwsGBxZTUFnOGdBTEFBR1FqdEc5Ujd0NXAxR3pqZXVkFqDFhei9XgAcFRQrAAAiPDkVABkVADkVAAAYIDhmYTllZTQyMjFlYjRhMWI5MDUzMGY4ODkyMzk3OGNlFQIREhgPOTM2NjE5NzQzMzkyNDU5HBaEq6fwyv22PxhAODM1NmMzZDdhYmI5YjcxMGQ4ZDNjYTRlOTdjNjNjODMyNDQzYzI5YzdmMTUzNjAwMTQyMWU0MWRjOGI2ODYwZQAcFQQAEiggaHR0cHM6Ly93d3cuaW5zdGFncmFtLmNvbS92dnJtaC8YDlhNTEh0dHBSZXF1ZXN0ABbE0aHHlqqxPygcL3JlcG9ydHMvd2ViL2dldF9mcnhfcHJvbXB0LxYkFobkno4MAA%3D%3D%5C%5C%5C%22%2C%5C%5C%5C%22shopping_session_id%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22logging_extra%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22is_in_holdout%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22preloading_enabled%5C%5C%5C%22%3Anull%7D%2C%5C%5C%5C%22frx_feedback_submitted%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22additional_data%5C%5C%5C%22%3A%7B%7D%7D%5C%22%2C%5C%22screen%5C%22%3A%5C%22frx_tag_selection_screen%5C%22%2C%5C%22flow_info%5C%22%3A%5C%22%7B%5C%5C%5C%22nt%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22graphql%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22enrollment_info%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22ig%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22ig_container_module%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22profilePage%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%22c84a4659-b781-4db1-bacb-c5c94baa341f%5C%5C%5C%22%7D%5C%22%2C%5C%22previous_state%5C%22%3Anull%7D%22%7D&selected_tag_types=%5B%22ig_drugs_v3%22%5D&action_type=2&frx_prompt_request_type=2'
        while True:
            report_Drugs = abood.post(url_rep, headers=hd_rep, data=data_report_Drugs)
            Drugs += 1
            if '"status":"ok"' in report_Drugs.text:
                print(Fore.GREEN + f'report done >> {target} / At:{Drugs}')
            else:
                print(Fore.RED + "err report")
    elif rep == 10:
        sof = 1
        data_report_sof = f'entry_point=1&location=2&object_type=5&object_id={idd}&container_module=profilePage&context=%7B%22tags%22%3A%5B%22ig_report_account%22%2C%22ig_its_inappropriate%22%5D%2C%22ixt_context_from_www%22%3A%22%7B%5C%22schema%5C%22%3A%5C%22ig_frx%5C%22%2C%5C%22session%5C%22%3A%5C%22%7B%5C%5C%5C%22location%5C%5C%5C%22%3A%5C%5C%5C%22ig_profile%5C%5C%5C%22%2C%5C%5C%5C%22entry_point%5C%5C%5C%22%3A%5C%5C%5C%22chevron_button%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%228a0f0019-372a-4231-88d2-cc14532fb8eb%5C%5C%5C%22%2C%5C%5C%5C%22tags%5C%5C%5C%22%3A%5B%5C%5C%5C%22ig_report_account%5C%5C%5C%22%2C%5C%5C%5C%22ig_its_inappropriate%5C%5C%5C%22%5D%2C%5C%5C%5C%22object%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22user_id%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22{idd}%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22reporter_id%5C%5C%5C%22%3A17841400254313570%2C%5C%5C%5C%22responsible_id%5C%5C%5C%22%3A17841407054502701%2C%5C%5C%5C%22locale%5C%5C%5C%22%3A%5C%5C%5C%22en_US%5C%5C%5C%22%2C%5C%5C%5C%22app_platform%5C%5C%5C%22%3A11%2C%5C%5C%5C%22extra_data%5C%5C%5C%22%3A%7B%5C%5C%5C%22container_module%5C%5C%5C%22%3A%5C%5C%5C%22profilePage%5C%5C%5C%22%2C%5C%5C%5C%22app_version%5C%5C%5C%22%3A%5C%5C%5C%22None%5C%5C%5C%22%2C%5C%5C%5C%22is_dark_mode%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22app_id%5C%5C%5C%22%3A936619743392459%2C%5C%5C%5C%22sentry_feature_map%5C%5C%5C%22%3A%5C%5C%5C%22JrrU89kBGCUyMDAxOjhmODoxMTJkOjU5NmU6Y2RkNjo1MWVmOjVlZjo5MzgyGHNNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvOTEuMC40NDcyLjEyNCBTYWZhcmkvNTM3LjM2GAVlbl9VUxwYIDEzOWEzYjExNTc2ZDNmOTMxNTgzOWE3NWQ3NDUwMGEzGAAYIDk1ODBjNDlmYzM1MmRkOTcyZTA0MjMxMzRmNzFmMTJiGAAVjIwBADwsGBxZTUFnOGdBTEFBR1FqdEc5Ujd0NXAxR3pqZXVkFqDFhei9XgAcFRQrAAAiPDkVABkVADkVAAAYIDkxMDE2Y2U2NzNmYjRmN2Q5NzYzYTNhN2MzYzMzYjkzFQIREhgPOTM2NjE5NzQzMzkyNDU5HBaEq6fwyv22PxhAODM1NmMzZDdhYmI5YjcxMGQ4ZDNjYTRlOTdjNjNjODMyNDQzYzI5YzdmMTUzNjAwMTQyMWU0MWRjOGI2ODYwZQAcFQQAEiggaHR0cHM6Ly93d3cuaW5zdGFncmFtLmNvbS92dnJtaC8YDlhNTEh0dHBSZXF1ZXN0ABbE0aHHlqqxPygcL3JlcG9ydHMvd2ViL2dldF9mcnhfcHJvbXB0LxYkFobkno4MAA%3D%3D%5C%5C%5C%22%2C%5C%5C%5C%22shopping_session_id%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22logging_extra%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22is_in_holdout%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22preloading_enabled%5C%5C%5C%22%3Anull%7D%2C%5C%5C%5C%22frx_feedback_submitted%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22additional_data%5C%5C%5C%22%3A%7B%7D%7D%5C%22%2C%5C%22screen%5C%22%3A%5C%22frx_tag_selection_screen%5C%22%2C%5C%22flow_info%5C%22%3A%5C%22%7B%5C%5C%5C%22nt%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22graphql%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22enrollment_info%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22ig%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22ig_container_module%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22profilePage%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%22ce5becbc-ca11-403e-805b-d0792c7045f9%5C%5C%5C%22%7D%5C%22%2C%5C%22previous_state%5C%22%3Anull%7D%22%7D&selected_tag_types=%5B%22ig_product_scam_fraud_v2%22%5D&frx_prompt_request_type=2'
        while True:
            report_sof = abood.post(url_rep, headers=hd_rep, data=data_report_sof)
            sof += 1
            if '"status":"ok"' in report_sof.text:
                print(Fore.GREEN + f'report done >> {target} / At:{sof}')
            else:
                print(Fore.RED + "err report")

else:
    print(Fore.RED + 'Login Error')