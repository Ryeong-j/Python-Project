def my_add(a, b):
    return a+b


def my_sub(a, b):
    return a-b

print(my_add(1,2))

# main으로 동작하는건지(내 파일 안에서) 
# 모듈로서 동작하는건지 구분할 수 있음
if __name__ == "__main__":
    print('메인입니다.')
else:
    print("모듈입니다.")