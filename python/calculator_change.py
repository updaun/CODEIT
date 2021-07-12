def calculate_change(payment, cost):
    change = payment - cost
    five_milion = 0
    one_milion = 0
    five_thousand = 0
    one_thousand = 0
    while True:
        if change >= 50000:
            change -= 50000
            five_milion += 1
        elif change < 50000 and change > 10000:
            change -= 10000
            one_milion += 1
        elif change < 10000 and change >= 5000:
            change -= 5000
            five_thousand += 1
        elif change < 5000 and change >= 1000:
            change -= 1000
            one_thousand += 1
        elif change == 0:
            break
    print(f'50000원 지폐: {five_milion}장')
    print(f'10000원 지폐: {one_milion}장')
    print(f'5000원 지폐: {five_thousand}장')
    print(f'1000원 지폐: {one_thousand}장')         

# 테스트
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)