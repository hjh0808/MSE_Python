import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

open = float(btc['opening_price'])
high = float(btc['max_price')
low = float(btc['min_price'])
diff = high - low    # ������ = �ְ�-������

# ������ �ϱ� ���� float�� ����Ѵ�. �Ǽ��� float�� ����Ѵ�.
if (�ð�+������) > �ְ�:
	print("�����")      # ���̸� "�����"�� ��½�Ų��.
else:
	print("�϶���")      # �����̸� "�϶���"�� ��½�Ų��.

