from functions import f, g, h
from threading import Thread


def threadize() -> None:
    threads = []

    # f1, f2, f3, f4
    for i in range(4):
        t = Thread(target=f[i], name=str(i + 1))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    threads = []

    # g1, g2
    for i in range(2):
        t = Thread(target=g[i], name=str(i + 1))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


    # h
    t = Thread(target=h[0], name="1")
    t.start()
    t.join()

