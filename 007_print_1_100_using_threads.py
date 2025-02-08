import threading
import time

class NumberPrinter(threading.Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number

    def run(self) -> None:
        time.sleep(1)
        print(f"Printing {self.number} from {threading.current_thread().name}.")

# driver code
if __name__ == "__main__":
    threads = []

    # Spinning up threads and adding it to the list
    for i in range(1, 101):
        new_thread = NumberPrinter(i)
        new_thread.start()
        threads.append(new_thread)

    # Waiting for all the threads to complete the execution (not needed though)
    for thread in threads:
        thread.join()

    print(f"Execution complete from {threading.current_thread().name}.")