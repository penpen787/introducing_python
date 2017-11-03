'''
    파이썬에선 모든것 (부울, 정수, 실수, 문자열, 함수, 프로그램 등) 이 객체Object 로 구현되어있다.
    파이썬은 강타입 언어이며 동적타이핑 언어이다.
    강타입 : 한번 생성된 객체의 타입을 바꿀 수 없음
        From WIKIPEDIA
        These terms do not have a precise definition, but in general,
        a strongly typed language is more likely to generate an error or refuse to compile if the argument passed to a function does not closely match the expected type.
        On the other hand, a weakly typed language may produce unpredictable results or may perform implicit type conversion
    동적 타이핑 언어 : Runtime에 타입을 체크함 / 반대 : 정적타이핑 언어 : Compile 타임에 체크
'''

# a 라는 변수에 정수값(리터럴) 7을 할당
# 변수는 단지 이름일 뿐이며 데이터가 담긴 객체에 그냥 a라고 이름을 붙이는것
a = 7
print(a)

b = a
print(b)

a = 10
print(b)  # ?


type(a)  # int
type(99.9)  # float
type('abc')  # str


# 다음과 같은 예약어는 사용 불가
# False class finally is return 등등

