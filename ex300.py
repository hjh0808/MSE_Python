per = ["10.31", "", "8.00"]

for i in per:
	try:       # try�� �����ڵ�
		print(float(i))
	except:    # except�� ���ܰ� �߻����� �� ������ �ڵ�
		print(0)
	else:      # ���ܰ� �߻����� �ʾ��� �� ������ �ڵ�
		print("clean data")
	finally:   # ���� �߻� ���ο� ������� �׻� ������ �ڵ�
		print("��ȯ �Ϸ�")