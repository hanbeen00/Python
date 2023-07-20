#mod1.py (모듈만들기, 원래는 개별파일)
def sum(a,b):
    return a+b
def safe_sum(a,b):
    if type(a) != type(b):
        print("더할수 있는 것이 아닙니다.")
        return
    else:
        result = sum(a,b)
    return result
if __name__ == "__main__":      #mod1.py 파일 직접 실행시에시만 작동
    print(safe_sum('a',1))
    print(safe_sum(1,4))
    print(sum(10,10.4))

#mod2.py (모듈만들기, 원래는 개별파일)
PI=3.141592
class Math:
    def solv(self,r):
        return PI * (r**2)
def sum(a,b):
    return a+b
if __name__ == "__main__":       #mod2.py 파일 직접 실행시에시만 작동
    print(PI)
    a = Math()
    print(a.solv(2))
    print(sum(PI, 4.4))


#실행부분
import mod1
print(mod1.sum(3,4))
print(mod1.safe_sum(3,4))
print(mod1.safe_sum(3,'a'))

from mod1 import sum
print(sum(3,4))
from mod1 import sum, safe_sum
from mod1 import *


import mod2
print(mod2.PI)
b= mod2.Math()
print(b.solv(2))
print(mod2.sum(mod2.PI, 4.4))


import sys
print(sys.path)
