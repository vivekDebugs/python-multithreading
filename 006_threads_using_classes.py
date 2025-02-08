import threading
import time

# inheriting Thread class
class NumberPrinter(threading.Thread):
    # overriding run() method
    def run(self) -> None:
        time.sleep(1)
        print(f"Printing from new thread: {threading.current_thread().name}")

number_printer = NumberPrinter()
number_printer.start()

print(f"Printing from main thread: {threading.current_thread().name}")