from threading import Thread, Lock
from datetime import datetime
import time



def zapis(k:int):
        file = open(f"example{k+1}.txt", "w")
        file.write(f"{k+1}")
        print
        file.close()
        time.sleep(1)


def failik(num:int):
    temp = datetime.now()
    for i in range(num):
        zapis(k=i)
    temp1 = datetime.now()
    print(f"Работа функции заняла {temp1 - temp} cекунд")

# failik(num=100)

def failik2(threads_count: int):
    temp = datetime.now()
    threads = [i for i in range(threads_count)]
    for i, obj in enumerate(threads):
        thread = Thread(target=zapis, kwargs={"k": i})
        thread.name = str(obj)
        thread.start()
    temp1 = datetime.now()
    print(f"Работа функции заняла {temp1 - temp} cекунд")

failik2(    threads_count=100)
