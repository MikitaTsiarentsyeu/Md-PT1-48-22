import time

def start():
    global st
    st = time.time()

def finish():
    return time.time() - st