import webbrowser
import threading
import time
def notifier():
    for x in range(24):
        webbrowser.open(r"https://www.youtube.com/watch?v=8JnfIa84TnU&index=2&list=PLw-VjHDlEOgtCjYJB1r1EkZ-AKlYv6Ozj")
        time.sleep(3600)
ti=threading.Thread(target=notifier)
ti.start()