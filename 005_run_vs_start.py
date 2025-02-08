import threading
import time

def print_something(text):
    time.sleep(1)
    print(f"Printing '{text}' from {threading.current_thread().name}.")

# creating new threads
new_thread_1 = threading.Thread(target=print_something, args=("FOOBAR",))
new_thread_2 = threading.Thread(target=print_something, args=("FOOBARBAZ",))

# start() executes the function in the new thread
new_thread_1.start()

# run() executes the function in the current thread
new_thread_2.run()

print_something('NOTHING')