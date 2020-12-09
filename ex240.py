def 함수0(num):
	return num * 2    # num * 2를 하여 돌아가라. (돌아갈 곳이 없으니 끝이다.)
	
def 함수1(num):
	return 함수0(num + 2)   # num + 2를 하여 함수0으로 돌아가라	
def 함수2(num):
	num = num + 10    # num은 10을 더하여 갱신한 것이다.
	return 함수1(num)  # 함수1(num)으로 돌아가라
	
c = 함수2(2)     # c는 함수2에 2를 대입한 값이다.
print(c)      # c를 출력하여라