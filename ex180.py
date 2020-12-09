low_prices = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

volatility = [ ]   # volatility를 리스트로 만들어라.
for i in range(5): # 0, 1, 2, 3, 4  # 5번 반복.
	diff = high_prices[i] - low_prices[i]   # 최고가와 최저가의 각자리에 있는 값을 빼라
	volatility.append(diff)   # diff값을 volatility안에 넣어라
	
print(volatility)    # volatility를 출력하여라