import time

def f(x):
    x = str(x)
    c = 'this value is ' +  x + '.'
    time.sleep(1)
    print(c)


l = [1,2,3,4,5,6,7]

for v in l:
    f(v)
