import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

open = float(btc['opening_price'])
high = float(btc['max_price')
low = float(btc['min_price'])
diff = high - low    # 변동폭 = 최고가-최저가

# 연산을 하기 위해 float를 사용한다. 실수는 float을 사용한다.
if (시가+변동폭) > 최고가:
	print("상승장")      # 참이면 "상승장"을 출력시킨다.
else:
	print("하락장")      # 거짓이면 "하락장"을 출력시킨다.

