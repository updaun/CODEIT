# 참고로 환율은 1달러에 1,000원, 그리고 1,000엔에 8달러라고 가정
# 원화(￦)에서 달러($)로 변환하는 함수
def krw_to_usd(krw):
    usd_list = []
    for i in krw:
        usd = round(i / 1000 , 1)
        usd_list.append(usd)
    return usd_list
# 달러($)에서 엔화(￥)로 변환하는 함수
def usd_to_jpy(usd):
    jpy_list = []
    for i in usd:
        jpy = round(i * 1000 /8, 1)
        jpy_list.append(jpy)
    return jpy_list
# 원화(￦)으로 각각 얼마인가요?
prices = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
print("한국 화폐: " + str(prices))
 
# amounts를 원화(￦)에서 달러($)로 변환하기
prices = krw_to_usd(prices)

# 달러($)로 각각 얼마인가요?
print("미국 화폐: " + str(prices))

# amounts를 달러($)에서 엔화(￥)으로 변환하기
prices = usd_to_jpy(prices)

# 엔화(￥)으로 각각 얼마인가요?
print("일본 화폐: " + str(prices))