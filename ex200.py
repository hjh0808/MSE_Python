ohlc = [["open", "high", "low", "close"],
		[100, 110, 70, 100],
		[200, 210, 180, 190],
		[300, 310, 300, 310],]
		
total_profit = 0

for day_price in ohlc[1:]:   
	profit = day_price[0] - day_price[3]  # 0�� �ڸ��� 3�� �ڸ��� ���� ?��.
	# ���� = �ð� - ���� �̴�.
	total_profit += profit   # �Ѽ��Ϳ� ������ ���� ��Ų��.}

print(total_profit)   # �Ѽ����� ��½�Ų��.