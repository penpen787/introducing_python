# 다른 언어들과 비슷하게 연산자 지원

9 / 5   # 1.8 다른언어와 다르게 정수 나누기 정수여도 부동 소수점으로 결과출력
9 // 5  # 1  // 는 소수점 이하를 버리고 정수로 출력

5 / 0   # divide by zero error

a = 10
a += 5
a -= 7
a *= 2
a /= 3
a //= 5

9 % 5 # mod 연산

divmod(9, 5) # (1,4) 몫과 나머지를 동시에 얻는 함수

# 사칙연산은 기본 수학의 연산우선순위 순
a = 2 + 3 * 4 / 2  # a?

# 진법
base2_1 = 0b0101  # ?
base2_2 = 0B0101

base8_1 = 0o11  # ?
base8_2 = 0O13

base16_1 = 0XAB
base16_2 = 0xabc

# False = 0 or 0.0, True = 1 or 1.1 로 계산
b = True + 2
c = False + 5.0


'''
    python 2 에서는 int, long 이 나뉘어 있었지만
    python 3 에서는 int로 통합 ( 크기 제한 X )
https://docs.python.org/2/library/stdtypes.html#numeric-types-int-float-long-complex
https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

float 는 해당 시스템 C 의 double 과 크기가 같음
'''





