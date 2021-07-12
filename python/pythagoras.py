# a<b<c 라고 가정할 때,  a + b + c = 1000a+b+c=1000 을 만족하는 피타고라스 삼조 (a, b, c)는 단 하나인데요.
# 이 경우, a * b * c는 얼마인가요?
for a in range(1, 334):
    for b in range(1, 501):
        if a > b:
            continue
        c = 1000 - a -b
        if (c**2 == a**2 + b**2):
            print(a,b,c)
            print(a*b*c)