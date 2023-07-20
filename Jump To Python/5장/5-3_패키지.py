#game/
#  __init__.py
#  sound/
#    __init__.py
#    echo.py
#  graphic/
#    __init__.py
#    render.py
#  play/
#    __init__.py
#    run.py


#echo.py
def echo_test():
    print("echo")

#__init__.py      해당 디렉터리가 패키지의 일부임을 알려주는 역할, 없을 시 패키지로 인식 안함. __all__변수 설정후 import할 수 있는 모듈 정의.
__all__ = ['echo']

#render.py
#from game.sound.echo import echo_test
from ..sound.echo import echo_test

def render_test():
    print("render")
    echo_test()


# 실행부분
import game.sound.echo
game.sound.echo.echo_test()

from game.sound import echo
echo.echo_test()

from game.sound.echo import echo_test
echo_test()

from game.sound import *
echo.echo_test()

from game.graphic.render import render_test
render_test()
