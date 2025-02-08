import threading
import time

def print_hello():
    time.sleep(1)
    print("Hello from new thread! Name:", threading.current_thread().name, "ID:", threading.current_thread().ident)

# creating new threads
new_thread_1 = threading.Thread(target=print_hello)
new_thread_2 = threading.Thread(target=print_hello)

# starting new threads
new_thread_1.start()
new_thread_2.start()

print("Hello from main thread! Name:", threading.current_thread().name, "ID:", threading.current_thread().ident)