import threading
import time

def print_hello():
    time.sleep(1)
    print("Hello from new thread!")

# creating new thread and passing the function to call
new_thread = threading.Thread(target=print_hello)

# starting new thread
new_thread.start()

print("Hello from main thread!")