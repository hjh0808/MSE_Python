def message1():    # message1�϶� "A"�� ����Ͽ���.
	print("A")
	
def message2():    # message2�϶� "B"�� ����Ͽ���.
	print("B")
	
def message3():     
	for i in range(3):   # for���� ���� �ݺ��Ͽ���.
		message2()       # message2()�� �����Ͽ��� -> "B"�� ����ض�
		print("C")       # "C"�� ����ض�.    message2 �� "C"�� ���� �ݺ��Ͽ���.
	message1()           # �������� message1()�� ����ض� -> "A"
	
message3()      