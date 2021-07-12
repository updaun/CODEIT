# 가변 타입 객체 vs 불변 타입 객체
# 리스트 클래스 객체 vs 튜플 클래스 객체

# mutable_object = [1,2,3]
# immutable_object = (1,2,3)

# mutable_object[0] = 4
# print(mutable_object) # [4, 2, 3]

# immutable_object[0] = 4
# print(immutable_object) # TypeError: 'tuple' object does not support item assignment

# 기존 튜플의 속성 변경 - 불가능
# tuple_x = (6,4)
# tuple_x[0] = 4
# tuple_x[1] = 1
# print(tuple_x)

# 새로운 인스턴스 지정 - 가능
# tuple_x = (6,4)
# tuple_x = (4,1)
# tuple_x = (4,1,7)
# print(tuple_x) # (4,1,7)

# 기존 리스트의 속성 변경 - 가능
list_x = []

list_x.append(4)
list_x.append(1)
list_x.append(7)

print(list_x) # [4, 1, 7]


# 가변 타입 : list, dict, 직접 만드는 class
# 불변 타입 : bool, int, float, str, tuple