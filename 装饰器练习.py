#定义一个装饰器，可以将函数的日志打印到出来
import time
from functools import wraps

def loglevel(logfile):
    def logit(fun):
        @wraps(fun)
        def printlog(*a,**b):
            funtime=time.ctime()
            str=fun.__name__ + "被运行"+funtime+ "\n"

            with open(logfile,"a") as openfile:
                openfile.writelines(str)
            return fun(*a,**b)
        return printlog
    return logit

 #执行一个函数，这个函数被logit装饰，可以具有打印日志的功能
@loglevel("输出日志")
def add(x,y):
    z=x+y
    print(z)
@loglevel("输出日志1")
def maxscore(x,y):
    print(max(x,y))

add(4,5)
maxscore(4,6)
