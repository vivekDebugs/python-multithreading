# ============================================================================
# ADDER-SUBTRACTER PROBLEM: Demonstrating Race Conditions in Threading
# ============================================================================
# PROBLEM DESCRIPTION:
# This program demonstrates a classic race condition. Two threads (Adder and 
# Subtracter) simultaneously modify a shared Counter variable. Since they 
# execute in parallel without synchronization, their increments/decrements 
# can interfere with each other, resulting in an incorrect final value.
#
# EXPECTED RESULT: counter.val should be 0 (1M additions - 1M subtractions)
# ACTUAL RESULT: counter.val will be non-zero due to race condition
#
# SOLUTION: Use locks (threading.Lock()) to synchronize access to shared data
# ============================================================================

import threading

class Counter:
    def __init__(self):
        self.val = 0

class Adder(threading.Thread):
    def __init__(self, counter, iterations):
        super().__init__()
        self.counter = counter
        self.iterations = iterations

    def run(self):
        # increamenting counter
        for i in range(self.iterations):
            self.counter.val += 1

class Subtracter(threading.Thread):
    def __init__(self, counter, iterations):
        super().__init__()
        self.counter = counter
        self.iterations = iterations

    def run(self):
        # decrementing counter
        for i in range(self.iterations):
            self.counter.val -= 1

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
