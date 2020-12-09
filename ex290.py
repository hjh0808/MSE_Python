class 부모:
	def __init__(self):    # 객체 생성
		print("부모생성")
		
class 자식(부모):            # 자식 클래스는 부모 클래스를 상속받는다.
	def __init__(self):    # 객체 생성
		print("자식생성")    # "자식생성"을 출력한다.
		super().__init__()   # 부모 클래스에 접근한뒤 생성자를 호출한다.
		
나 = 자식()