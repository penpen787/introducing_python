'''
ascii 코드
1960년대 ascii 코드가 제정되었다.
ascii 코드는 8비트(1바이트)로 앞에 패리티비트를 제외한 7비트를 문자로 표시하여 128개의 고유한 값을 표현한다.
주로 명령어(command), 영문자(대소문자), 숫자를 표현한다.
https://namu.wiki/w/%EC%95%84%EC%8A%A4%ED%82%A4%20%EC%BD%94%EB%93%9C?from=ASCII

euc-kr / cp949
각 국가별로 자신들의 언어를 나타낼수 있는 ascii코드의 확장판이 등장하였다.
이 ascii 확장판은 2byte(16bit)로 2^16=65536 개의 문자를 표시할 수 있어야 하나..
ascii의 확장이기 때문에 ascii 호환성을 위해 (앞 ascii + 뒤 ascii) 로 표현해야하며,
ascii 중 커맨드 문자를 만나면 멈추는 시스템이 남아있어 총 7bit 128문자중 34개의 커맨드를 뺀 94개문자만 표현 가능하였다.
즉 총 표현 가능한 문자수는 94*94 = 8836개 였다.
이중 한글을 표현가능한 확장판은 euc-kr / cp949 이다.

euc-kr : 2바이트로 ascii 1바이트를 제외한 나머지를 표현한다.
'가'~'힝'까지 완성형으로 표현하며 한글 2350자, 일본어, 중국어등을 표현한다.

cp949 : MS에서 만든 euc-kr 확장형 / 똠방각하 표기 가능

유니코드
유니코드는 전세계 모든 문자를 표기하도록 한 문자 전산 처리 방식
UTF-8 : 1~4 byte 가변
(1byte는 ascii 표현)
한글은 3byte대에 속해있음

기본적으로 유니코드는 U+xxxx 로 표기
파이썬에서 유니코드를 문자열로 표기시 \\u + xxxx 로 표기
'''

import unicodedata

def unicode_test(value):
   name = unicodedata.name(value)
   value2 = unicodedata.lookup(name)
   print(value, name, value2, sep=' , ')


unicode_test('A')
unicode_test('전')
unicode_test('\u2603')


# 파이썬에서 인코딩 (문자열 -> 바이트)
snowman = '\u2603'
encoded = snowman.encode('utf-8')
print(len(encoded), encoded) # b'\xe2\x98\x83', b는 바이트 표기snowman = '\u2603'

encoded = 'A'.encode('utf-8')
print(len(encoded), encoded)

encoded = '김'.encode('utf-8')
print(len(encoded), encoded)

# 디코딩 (바이트 -> 문자열)
place = 'caf\u00e9'
print(place)
place_b = place.encode('utf-8')
print(len(encoded), place_b)


# 텍스트 포맷
# 옛 스타일 %
print("val1 = %d, val2 = %s" % (1, 'T'))

# new style {}.format
print('{} {}'.format(7, 'Z'))