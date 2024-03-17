import time

class Timer(): 
    def do_every(self, period,f,*args):
        def g_tick():
            t = time.time()
            while True:
                t += period
                yield max(t - time.time(),0)
        g = g_tick()
        while True:
            time.sleep(next(g))
            f(*args)

def printTime():
    print(time.ctime())

