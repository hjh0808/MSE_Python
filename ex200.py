ohlc = [["open", "high", "low", "close"],
		[100, 110, 70, 100],
		[200, 210, 180, 190],
		[300, 310, 300, 310],]
		
total_profit = 0

for day_price in ohlc[1:]:   
	profit = day_price[0] - day_price[3]  # 0의 자리와 3의 자리의 값을 ?다.
	# 수익 = 시가 - 종가 이다.
	total_profit += profit   # 총수익에 수익을 누적 시킨다.}

print(total_profit)   # 총수익을 출력시킨다.