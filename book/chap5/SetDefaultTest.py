from collections import defaultdict
from collections import Counter

dict1 = defaultdict(int)

dict1['A'] = 0
dict1['B']
print(dict1)


# intvalue = int('A')
# print(intvalue)


#dict1 = {'H':1, "B":2}



print(len(dict1))




def a(var1):
    def b():
        print(var1);
        pass
    return b

a1 = a(1)
a2 = a(2)

print(a1)
print(a2)

def c(var1):
    def d():
        pass
    return c

c1 = c(1)
c2 = c(2)

print(c1)
print(c2)
