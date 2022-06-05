import threading

def show_message(text):
    print(text)

def calculate_bill(prices, show_func):
    res = sum(prices)
    text = f"It will be {res}"
    show_func(text)

calculate_bill([1123,4564,23,4567,224], show_message)

def show_warning():
    print("Warning!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

threading.Timer(3,show_warning).start()
for i in range(6000):
    print("I'm running")