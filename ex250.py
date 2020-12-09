import numpy   # 실수로 증가시키기 위해 numpy 함수를 사용한다.
for i in numpy.arrange(0, 5, 0.1): # 원래 for문은 정수 단위로만 증가한다. 하지만 0.1씩 증가시키기 위해 numpy를 사용했다.
	print(i)    # i를 출력시켜라