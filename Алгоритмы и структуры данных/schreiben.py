from random import randint 
import time

def perebor(x):
    start = time.time()
    for i in range(upper+1):
        if i == x:
            break
    fin = time.time()
    print(f'Число отгадано и это {i} за {i} итераций')
    print(f'Времени ушло {fin-start}')

def random_guess(x):
    start = time.time()
    k = 1
    num = randint(0, upper)
    while x != num:
        num = randint(0, upper)
        k+=1
    fin = time.time()
    print(f'Число отгадано и это {num} за {k} итераций')




upper = 100
x = randint(0,100)
perebor(x)
random_guess(x)


