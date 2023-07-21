#오류예외처리기법
try:
    4/0
except ZeroDivisionError as e:
    print(e)
    

try:
    f=open('foo.txt','r')
except FileNotFoundError as e:
    print(str(e))
else:
    data = f.read()
    f.close()


f=open('foo.txt','w')
try:
    #무언가를 실행한다.
    print(1)
finally:
    f.close()


#오류 회피하기
try:
    f=open("나없는 파일",'r')
except FileNotFoundError: #파일 없더라도 오류를 발생시키지 않고 통과
    pass


#오류 일부러 발생시키기
class Bird:
    def fly(self):
        #raise NotImplementedError #일부러 오류 발생
        print("very fast")
class Eagle(Bird):
    pass

eagel =Eagle()
eagel.fly()
