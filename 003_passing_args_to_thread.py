import threading
import time

def print_something(text):
    time.sleep(1)
    print(text)

def print_multiple(*args):
    time.sleep(1)
    for arg in args:
        print(arg)

# creating new threads and passing the function to call along with arguments
new_thread_1 = threading.Thread(target=print_something, args=("Arg to new thread 1!",))
new_thread_2 = threading.Thread(target=print_multiple, args=("Arg 1 to new thread 2!", "Arg 2 to new thread 2!"))

# starting new threads
new_thread_1.start()
new_thread_2.start()

print("Hello from main thread!")