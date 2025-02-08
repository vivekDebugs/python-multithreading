import threading
import time

class NumberPrinterWithDelay(threading.Thread):
    def __init__(self, number, delay):
        super().__init__()
        self.number = number
        self.delay = delay
    
    def run(self):
        time.sleep(self.delay)
        print(f"Printing {self.number} from {threading.current_thread().name}")

if __name__ == "__main__":
    for i in range(1, 101):
        number_printer = NumberPrinterWithDelay(i, i)
        number_printer.start()
    print("Printing from", threading.current_thread().name)