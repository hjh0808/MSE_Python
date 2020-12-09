date = ['09/05', '09/06', '09/07', '09/08', '09/09']     # key의 형태이다.
close_price = [10500, 10300, 10100, 10800, 11000]        # value의 형태이다.
close_table = dict(zip(date, close_price))               # 딕셔너리의 형태로 만들어라.
print(close_table)                                       # close_table을 출력하여라.