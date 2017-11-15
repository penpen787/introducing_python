#-*-coding:utf-8-*-i

# author : Grace

'''
3.1 리스트와 튜플
#리스트 변경가능, 튜플은 불변, (리스트는 항목을 할당, 자유롭게 수정하거나 삭제 등 변경가능)
#리스트
'''

#리스트 생성
empty_list = [ ]
print(empty_list)
another_empty_list = list()
print(another_empty_list)

#리스트 특징
weekdays = ['Monday','Tuesday','Wednesday', 'Thursday', 'Friday' ] #순서가 있는 데이터에 유용
print(weekdays)

big_birds = ['emu', 'ostrich', 'cassowary']

print(big_birds)

first_names = ['Graham', 'John', 'Terry', 'Terry', 'Michael' ] #값이 유일할 필요 없음
print(first_names)



#다른 데이터 타입을 리스트로 변환
##list() 함수를 이용해 리스트로 변환
print(list('cat'))
a_tuple = ( 'ready', 'fire', 'aim')
print(a_tuple)
print(list(a_tuple))

#split() 함수를 이용해 문자열을 리스트로 변환
birthday = '1/6/1952'
print(birthday.split('/'))

splitme = 'a/b//c/d//e'
print(splitme.split('/')) #왜?
print(splitme.split('//'))

#offset으로 항목 얻기
marxes = [ 'Groucho', 'Chico', 'Harpo']
print(marxes[0])
print(marxes[1])
print(marxes[2])
#print(marxes[3])
print(marxes[-1])
print(marxes[-2])
print(marxes[-3])
#print(marxes[-4])

#리스트의 리스트
small_birds = ['hummingbird','finch']
extinct_birds = ['dodo','passenger pigeon', 'Norwegian Blue']
carol_birds = [3, 'French hens', 2, 'turtledoves']
all_birds = [small_birds,extinct_birds,carol_birds]
print(all_birds)
print(all_birds[0])
print(all_birds[1])
print(all_birds[1][0])

#offset으로 항목 바꾸기
marxs = ['Groucho', 'Chico', 'Harpo']
marxs[2] = 'Wanda'
print(marxs)
#marxs[3] = 'suzy'  #리스트의 오프셋은 리스트에서 유효한 위치여야 함
#pritn(marxs)

#슬라이스로 항목 추출하기
#오프셋으로 서브시퀀스 추출 가능
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[0:2])
print(marxes[::2])
print(marxes[::-2])
print(marxes[::-1]) #오프셋으로 역순 정렬 가능
print(marxes[::3])
print(marxes[::4])
print(marxes[::5])
print(marxes[::-3])
print(marxes[::-4])

#.append()  : 리스트 끝에 항목 추가
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.append('Zeppo')
print(marxes)

# extend() or += : 리스트 병합하기
# extend() : 항목 추가하기
# del 변수명[오프셋] : 오프셋으로 항목 삭제
# remove() : 값으로 항목 삭제
# pop() : 오프셋으로 항목을 얻은 후 삭제
# index() : 값으로 항목 오프셋 찾기
# 문자열 in 리스트 : 리스트에서 어떤 겂의 존재를 확인
# count() : 리스트에 특정 값이 얼마나 있는지 세기
# '구분자',join() : 문자열로 변환하기
# sort() : 정렬하기
# len() : 항목 개수 얻기
# 할당: = , 복사 : copy()

#복사방법1 - 할당 : 객체를 참조
a = [1,2,3]
print(a)
b = a
print(b)
a[0]= 'surprise'
print(a)
print(b) #b는 단지 같은 리스트 객체의 a를 참조 따라서 a 혹은 b 리스트의 내용을 변경하면 두 변수 모두에 반영

#복사 방법2 - 동일한 값을 가진 새로운 객체를 생성
#copy()
#list()
#슬라이스[:]


a = [1,2,3]
'''
b = a.copy()
print(b)
c = list(a)
print(c)
d = a[:]
print(d)

a[0] = 'integer lists are boring'
print(a)
print(b)
print(c)
print(d)
'''

'''
3.3 튜플
리스트와 다르게 튜플을 불변
튜플을 정의한 후에는 추가, 삭제, 수정할 수 없음
튜플은 상수의 리스트
'''

#튜플 생성하기
empty_tuple = ()
print(empty_tuple)

#하나 이상의 요소가 있는 튜플을 만들기 - 각 요소 뒤에 콤마 붙이기
#튜플을 정의할 때 괄호 () 생략 가능. , 뒤에 콤마가 붙는다는 것으로 튜플 정의

one_marx = 'Groucho',
print(one_marx)

one_marx1 = ('Groucho')
print(one_marx1)

one_marx2 = ('Groucho',)
print(one_marx2)

#두개 이상의 요소가 있을 경우, 마지막 요소에는 콤파 붙이지 x
marx_tuple = 'Groucho', 'Chico'
print(marx_tuple)

#튜플을 한번에 여러 번수를 할당가능 == 튜플 언패킹

marx_tuple = ('Groucho', 'Chico', 'Harpo')
a,b,c = marx_tuple
print(a)
print(b)
print(c)

marx_list = ['Groucho', 'Chico', 'Harpo']
a,b,c = marx_list
print(a)
print(b)
print(c)

marx_string = 'abc'
a,b,c = marx_string
print(a)
print(b)
print(c)

#marx_int = 123
#a,b,c = marx_int
#print(a)
#print(b)
#print(c)

#튜플을 사용해서 값을 교환
password = 'swordfish'
icecream = 'tuttifrutti'

password, icecream = icecream, password
print(password)
print(icecream)

#tuple() 은 다른 객체를 튜플로 만들어줌
marx_list = ['Groucho', 'Chico', 'Harpo']
print(marx_list)
print(tuple(marx_list))

#튜플 vs 리스트
#튜플은 리스트에 적용할 수 있는 append(), insert() 등 과 같은 함수가 없고, 함수의 수가 매우 적음
#이유는 튜플을 생성한 후에는 수정할 수 없기 때문
#그러나 장점...
#1.튜플은 더 적은 공간을 사용, 2.실수로 튜플의 항목이 손상될 염려가 없음, 3.튜플을 딕셔너리 키로 사용할 수 있음, 4. 네임드 튜플은 객체의 단순한 대안이 될 수 있음, 5. 함수의 인자들은 튜플로 전달

'''
#3.4 딕셔너리
'''
#딕셔너리는 키-값 요소를 추가, 삭제 , 수정 가능
#항목의 순서를 따지지 않으며, 오프셋으로 항목을 선택할 수 없음
# 값에 상응하는 고유한 키를 지정가능
#키는 대부분 문자열, 그러나 불변하는 타입(부울, 정수, 부동소수점수, 튜플, 문자열...)도 가능

#딕셔너리 생성하기
empty_dict = {}
print(empty_dict)
print(type(empty_dict))
bierce = { "day" : "A period of twenty-four hours, mostly misspent", "positive" : "Mistaken at the top of one's voice", "misfortune": "The kind of fortune that never misses"}
print(bierce)

#딕셔너리로 변환하기: dict()
#두 값으로 이루어진 시쿼스를 딕셔너리로 변환 가능
lol = [ ['a','b'],['c','d'],['e','f']]
print(dict(lol)) # 딕셔너리의 키 순서는 임의적, 항목을 어떻게 추가하느냐에 따라 그 순서가 달라짐
lot = [ ('a','b'),('c','d'),('e','f')]
print(dict(lot))

tol= ( ['a','b'],['c','d'],['e','f'])
print(dict(tol)) # 딕셔너리의 키 순서는 임의적, 항목을 어떻게 추가하느냐에 따라 그 순서가 달라짐
los = [ 'ab','cd','ef']
print(dict(los))

#항목 추가/변경하기
#키를 이용해 값을 할당
#키가 딕셔너리에 존재하는 경우, 그 값은 새 값으로 대체
#키가 존재하지 않는 경우, 값이 키와 사전에 추가됨

pythons = {'Chapman':'Graham','Cleese':'John','Idle':'Eric','Jones':'Terry','Palin':'Michael'}
print(pythons)
pythons['Gilliam'] = 'Gerry' #딕셔너리에 없는 키와 값을 새로 생성
print(pythons)
pythons['Gilliam'] = 'Terry' #딕셔너리에 기존에 존재하는 키라면 값을 변경
print(pythons)

#딕셔너리의 키는 반드시 유일해야함
some_pythons = {'Chapman':'Graham','Cleese':'John','Terry':'Gilliam','Terry':'Jones'}
print(some_pythons)  # 키를 두번 이상 사용하면 마지막 값이 승리

#update() : 딕셔너리 결합하기
#del 딕셔너리['키']
#clear() : 모든 항목 삭제
#문자열/수치.. in 딕셔너리 : 딕셔너리에 특정 키가 있는지 없는지 테스트 가능

#항목얻기 : [key]

pythons = {'Chapman':'Graham','Cleese':'John','Jones':'Terry','Palin':'Michael'}
print(pythons['Cleese'])
#print(pythons['Marx']) #딕셔너리에 없는 키 값은 에러메세지 출력
#get() 함수 -> 키가 존재하지 않으면 옵션값 지정해서 출력 가능
pythons = {'Chapman':'Graham','Cleese':'John','Jones':'Terry','Palin':'Michael'}
print(pythons.get('Cleese'))
print(pythons.get('Marx','Not a Python'))
print(pythons.get('Marx2'))

#모든 키 값 얻기 : keys()
signals = {'green':'go','yellow':'go faster','red':'smile for the camera'}
print(signals.keys())
print(list(signals.keys()))

#모든 값 가져오기 : values()
print(list(signals.keys()))
print(list(signals.values()))

#모든 쌍의 키-값 얻기: items()
print(signals.items())
print(list(signals.items()))

#할당 = , 복사 : copy()

'''
3.5. 셋
'''

#딕셔너리에서 값은 버리고 키만 남은 데이터 타입
#각 키는 유일

#셋 생성하기
empty_set = set()
print(empty_set)
even_numbers = {0,2,4,6,8}
print(even_numbers)
odd_numbers = {1,3,5,7,9}
print(odd_numbers)

#데이터 타입 변환하기 : set()

print(set('letters'))
print(set(['Dasher','Dancer','Prancer','Mason-Dixon']))
print(set({'apple':'red','orange':'orange','cherry':'red'})) #키만 출력

#in 으로 값 멤버쉽 테스트
drinks = { 'martini': {'vodka','vermouth'}, 'black russian':{'vodka','kahlua'},'white russian':{'cream','kahlua','bitters'},'manhattan':{'rye','vermouth','bitters'},'screwdriver':{'orange juice','vodka'}}
for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)

for name, contents in drinks.items():
    if 'vodka' in contents and not ('vermouth' in contents or 'cream' in contents):
        print(name)

#콤비네이션과 연산자
drinks = { 'martini': {'vodka','vermouth'}, 'black russian':{'vodka','kahlua'},'white russian':{'cream','kahlua','bitters'},'manhattan':{'rye','vermouth','bitters'},'screwdriver':{'orange juice','vodka'}}

for name, contents in drinks.items():
    if contents & {'vermouth','orange juice'}:
        print(name)

bruss = drinks['black russian']
print(bruss)
wruss = drinks['white russian']
print(wruss)

##인터섹션 구하기
a = {1,2}
b = {2,3}
print(a & b)
print(a.intersection(b))

##유니온 구하기
print(a|b)
print(a.union(b))

##디퍼런스 구하기
print(a-b)
print(a.difference(b))

##대칭 차집합, 부분집합, 진부분집합, 등등을 구할 수 있음
