# ============================================================================
# PRODUCER-CONSUMER PROBLEM
# ============================================================================
# Problem: Producer adds items, Consumer removes items from shared Store
# 
# Issue: Without synchronization, race conditions occur
# - Check and action are NOT atomic
# - Both threads access store simultaneously → unpredictable behavior
# ============================================================================

import threading


class Store:
    # shared buffer between producer and consumer
    def __init__(self, capacity):
        self.items = []
        self.capacity = capacity


class Producer(threading.Thread):
    def __init__(self, store: Store):
        super().__init__()
        self.store = store

    def run(self):
        # adds items to the store
        if len(self.store.items) < self.store.capacity:
            print('Producer adding..')
            self.store.items.append('X')


class Consumer(threading.Thread):
    def __init__(self, store: Store):
        super().__init__()
        self.store = store

    def run(self):
        # removes items from the store
        if len(self.store.items) > 0:
            print('Consumer removing..')
            self.store.items.pop(-1)


if __name__ == "__main__":
    # initializing store (shared memory)
    store = Store(5)
    
    print("Initial store: ", len(store.items))

    # creating and firing producer and consumer threads
    for i in range(1_000):
        producer = Producer(store)
        consumer = Consumer(store)
        
        producer.start()
        consumer.start()
    
    print("Final store: ", len(store.items))