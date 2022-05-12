import requests

headers = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie': '_ga_L9VRTEHZDK=GS1.1.1636507022.1.1.1636508141.0; _ga=GA1.3.939962833.1624436012; WMONID=s_J3kprxE_u; _gid=GA1.3.1142251945.1652158752; JSESSIONID=Fl9a8EaC3wKorsfEceJNT3FOkRVHewJmmk7o4FR9pTcIaZ107hY6cRKXvHIAi11z.a251YXBwX2RvbWFpbi9rbnUtaW50ZnMta3VwdGwta2NvcmUtd2ViMw==',
'Host': 'knuin.knu.ac.kr',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'none',
'Sec-Fetch-User': '?1',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
}

response = requests.get("https://knuin.knu.ac.kr/public/stddm/lectPlnInqr.knu", headers=headers)

print(response.text)