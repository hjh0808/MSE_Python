low_prices = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

volatility = [ ]   # volatility�� ����Ʈ�� ������.
for i in range(5): # 0, 1, 2, 3, 4  # 5�� �ݺ�.
	diff = high_prices[i] - low_prices[i]   # �ְ��� �������� ���ڸ��� �ִ� ���� ����
	volatility.append(diff)   # diff���� volatility�ȿ� �־��
	
print(volatility)    # volatility�� ����Ͽ���