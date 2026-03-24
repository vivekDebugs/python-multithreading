# ============================================================================
# SEMAPHORES: Control how many threads can enter a critical section
# ============================================================================
# Semaphore(n) = At most n threads can acquire() simultaneously
#
# Example: Semaphore(5) means max 5 threads can pass through at once
# - Each acquire() decrements count (n=4,3,2,1,0)
# - When count reaches 0, next thread blocks
# - release() increments count, wakes up blocked thread
#
# In this problem:
# - producerSemaphore(5): Max 5 "add" operations simultaneously (buffer capacity)
# - consumerSemaphore(0): Max 0 "remove" operations initially (no items yet)
# ============================================================================

import threading

class Store:
    def __init__(self, capacity):
        self.items = []
        self.producerSemaphore = threading.Semaphore(capacity) # creating 'capacity' number of locks (semaphores) for producers
        self.consumerSemaphore = threading.Semaphore(0) # creating 0 locks for consumers

class Producer(threading.Thread):
    def __init__(self, store: Store):
        super().__init__()
        self.store = store

    def run(self):
        self.store.producerSemaphore.acquire() # deducting a producer lock
        print("Producer adding..")
        self.store.items.append('X')
        self.store.consumerSemaphore.release() # adding a consumer lock (sends signal to consumer thread)

class Consumer(threading.Thread):
    def __init__(self, store: Store):
        super().__init__()
        self.store = store

    def run(self):
        self.store.consumerSemaphore.acquire() # deducting a consumer lock
        print("Consumer removing..")
        self.store.items.pop(-1)
        self.store.producerSemaphore.release() # adding a producer lock (sends signal to producer thread)

if __name__ == "__main__":
    # initializing store (shared memory)
    store = Store(5)

    # creating and firing producer and consumer threads
    for i in range(10_000):
        producer = Producer(store)
        consumer = Consumer(store)

        producer.start()
        consumer.start()