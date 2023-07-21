#sys.argv - 명령행에서 인수 전달하기
import sys
print(sys.argv)

#sys.exit - 강제로 스크립트 종료하기
#sys.exit()

#sys.path - 자신이 만든 모듈 불러와 사용하기
print(sys.path.append("C:/Python/Mymodules"))

#pickle - 객체의 형태를 유지하면서 파일 저장 불러오기
import pickle
f=open("test.txt",'wb')
data = {1:'python',2:'you need'}
pickle.dump(data,f)
f.close()

f=open("test.txt",'rb')
data = pickle.load(f)
print(data)
f.close()

#os.environ - 시스템 환경변수값
import os
print(os.environ)
print(os.environ['PATH'])

#os.chdir - 현재 디렉터리의 위치 변경
os.chdir("C:\WINDOWS")

#os.getcwd - 현재 디렉터리 위치 리턴
print(os.getcwd())

#os.system - 시스템 명령어 호출
os.system("dir")

#os.popen - 실행한 시스템 명령어 결과값 리턴
f=os.popen("dir")
print(f.read())

#os.mkdir(디렉터리) - 디렉터리 생성
#os.rmdir(디렉터리) - 디렉터리 삭제(비어 있어야함)
#os.unlink(파일이름) - 파일 삭제
#os.rename(src,dst) - scr파일 이름을 dst이름으로 바꿈

#shutil - 파일복사 모듈
import shutil
#shutil.copy("scr.txt","dst.txt")

#glob - 디렉터리에 있는 파일 이름 리스트로 만들기
import glob
print(glob.glob("C:/Python/q*"))

#tempfile - 임시파일 만들기
import tempfile
filename=tempfile.mktemp()
print(filename)
f=tempfile.TemporaryFile()
f.close() #생성한 임시파일 자동 삭제

#time
import time
print(time.time()) # 1970/1/1 00:00:00 기준으로 지난 시간 초단위 리턴
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
print(time.ctime())
print(time.strftime('%x',time.localtime(time.time())))
print(time.strftime('%c',time.localtime(time.time())))
for i in range(10):
    print(i)
    time.sleep(1)

#calendar - 파이썬에서 달력
import calendar
print(calendar.calendar(2015))
print(calendar.prcal(2015))
print(calendar.weekday(2015,12,31)) #그 날짜에 해당하는 요일 리턴
print(calendar.monthrange(2015,12)) #요일과 그달이 며칠까지 있는지 튜플 형태로 리턴

#random - 난수발생 모듈
import random
print(random.random())
print(random.randint(1,10))
print(random.randint(1,55))
def random_pop(data):
    number = random.randint(0,len(data)-1)
    return data.pop(number)
def random_pop(data):
    number = random.choice(data)
    data.remove(number)
    return number
if __name__ == "__main__":
    data=[1,2,3,4,5]
    while data:
        print(random_pop(data))

data=[1,2,3,4,5]
print(random.shuffle(data))

#webbrowser - 웹브라우저 자동 실행 모듈
import webbrowser
webbrowser.open("http://google.com")
webbrowser.open_new("http://naver.com")

#threading - 스레드 다루기
import threading
import time

def say(msg):
    while True:
        time.sleep(1)
        print(msg)

for msg in ['you','need','python']:
    t=threading.Thread(target=say, args=(msg,))
    t.daemon=True
    t.start()
for i in range(100):
    time.sleep(0.1)
    print(i)

class MyThread(threading.Thread):
    def __init__(self,msg):
        threading.Thread.__init__(self)
        self.msg=msg
        self.daemon = True
    def run(self):
        while True:
            time.sleep(1)
            print(self.msg)
for msg in ['you','need','python']:
    t=MyThread(msg)
    t.start()
for i in range(100):
    time.sleep(0.1)
    print(i)
