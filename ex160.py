리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in 리스트:    
	if i.endswith(('.h', '.c')):   # .h 또는 .c로 끝난다면 
		print(i)                   # 그것을 출력하여라.
		