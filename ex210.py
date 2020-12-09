def message1():    # message1일때 "A"를 출력하여라.
	print("A")
	
def message2():    # message2일때 "B"를 출력하여라.
	print("B")
	
def message3():     
	for i in range(3):   # for문을 세번 반복하여라.
		message2()       # message2()를 실행하여라 -> "B"를 출력해라
		print("C")       # "C"를 출력해라.    message2 와 "C"를 세번 반복하여라.
	message1()           # 마지막은 message1()을 출력해라 -> "A"
	
message3()      