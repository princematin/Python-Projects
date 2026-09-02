from threading import Thread, Lock

def synchronized(func):

    locker = Lock()

    def wrapper(*args, **kwargs):
        locker.acquire()

        result = func(*args, **kwargs)

        locker.release()

        return result
    
    return wrapper