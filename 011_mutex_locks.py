# ============================================================================
# MUTEX LOCKS IMPLEMENTATION - Thread-Safe Counter
# ============================================================================
# Demonstrates how to use RLock (Reentrant Lock) to protect shared data
# from race conditions. The counter will be incremented and decremented
# by two threads simultaneously while maintaining consistency.
# ============================================================================

import threading

class Counter:
    def __init__(self):
        self.val = 0
        # same lock object used by both threads to get access to the critical section
        # only one thread can acquire lock at a lock hence only one thread can get into critical section
        self.lock: threading.RLock = threading.RLock()

class Adder(threading.Thread):
    def __init__(self, counter: Counter, iterations: int):
        super().__init__()
        self.counter = counter
        self.iterations = iterations

    def run(self):
        for i in range(self.iterations):
            self.counter.lock.acquire()
            self.counter.val += 1 # critical section
            self.counter.lock.release()

class Subtracter(threading.Thread):
    def __init__(self, counter: Counter, iterations: int):
        super().__init__()
        self.counter = counter
        self.iterations = iterations

    def run(self):
        for i in range(self.iterations):
            self.counter.lock.acquire()
            self.counter.val -= 1 # critical section
            self.counter.lock.release()

if __name__ == "__main__":
    # number of iterations
    ITERATIONS = 1_000_000
    
    # initializing the counter (shared memory)
    counter = Counter()
    
    # initializing adder and subtracter threads
    adder = Adder(counter, ITERATIONS)
    subtracter = Subtracter(counter, ITERATIONS)

    # initial state of the counter
    print("Counter value before process: ", counter.val)

    # spinning up both threads simultaneously
    adder.start()
    subtracter.start()

    # waiting for threads to complete the execution
    adder.join()
    subtracter.join()

    # final state of the counter
    print("Counter value after process: ", counter.val)
