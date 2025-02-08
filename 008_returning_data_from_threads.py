import time
import threading
import concurrent.futures

def square(n):
    time.sleep(1)
    return f"{n} -> {n * n}, executed by {threading.current_thread().name}"

def print_squares_on_threads(
    num_squares: int = 10,
    num_threads: int = None
):
    numbers = [i for i in range(num_squares+1)]

    # initialises thread pool executor with `max_workers` number of threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = []

        # submitting tasks to be run on individual threads
        for number in numbers:
            square_future = executor.submit(square, number) # pass multiple arguments to the function as *args
            futures.append(square_future)

        # getting results from the threads
        for future in concurrent.futures.as_completed(futures):
            print(f'Result: {future.result()}')

    print("Main thread:", threading.current_thread().name)

if __name__ == "__main__":
    print_squares_on_threads(num_squares=10, num_threads=6)

# docs: https://docs.python.org/3/library/concurrent.futures.html