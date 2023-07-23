f=open("새파일.txt",'w')
f.close()

f=open("D:\점프 투 파이썬\새파일.txt",'w')
f.close()

f=open("D:\점프 투 파이썬\새파일.txt",'w')
for i in range(1,11):
    data= "%d번째 줄입니다.\n" %i
    f.write(data)
f.close()

f=open("D:\점프 투 파이썬\새파일.txt",'r')
while True:
    line=f.readline()
    if not line:
        break
    print(line)
f.close()

f=open("D:\점프 투 파이썬\새파일.txt",'r')
lines=f.readlines()
for line in lines:
    print(line)
f.close()

f=open("D:\점프 투 파이썬\새파일.txt",'r')
data=f.read()
print(data)
f.close()

f=open("D:\점프 투 파이썬\새파일.txt",'a')
for i in range(11,20):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close()

with open("foo.txt","w") as f:
    f.write("life is too short, you need python")
    

import sys
args=sys.argv[1:]
for i in args:
    print(i)
