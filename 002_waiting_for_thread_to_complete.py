import threading
import time

def print_hello():
    time.sleep(2)
    print("Hello from new thread!")

# creating new thread
new_thread = threading.Thread(target=print_hello)

# starting new thread
new_thread.start()

# waiting for new thread to complete the execution
new_thread.join()

print("Hello from main thread!")