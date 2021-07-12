# 화씨 온도에서 섭씨 온도로 바꿔 주는 함수
def fahrenheit_to_celsius(fahrenheit):
    result = []
    for i in fahrenheit:
        calculate_temp = round((((i - 32) * 5 ) / 9), 1)
        result.append(calculate_temp)
    return result


temperature_list = [40, 15, 32, 64, -4, 11]
print("화씨 온도 리스트: " + str(temperature_list))  # 화씨 온도 출력

temperature_list = fahrenheit_to_celsius(temperature_list)
print("섭씨 온도 리스트: " + str(temperature_list))  # 섭씨 온도 출력