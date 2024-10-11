import threading
import time

# Create two locks (resources)
lock1 = threading.Lock()
lock2 = threading.Lock()

# Function for the first thread
def thread1_routine():
    print("Thread 1: Trying to acquire Lock 1...")
    lock1.acquire()
    print("Thread 1: Acquired Lock 1, now waiting for Lock 2...")
    time.sleep(1)  # Simulating some processing time

    print("Thread 1: Trying to acquire Lock 2...")
    lock2.acquire()
    print("Thread 1: Acquired Lock 2!")

    # Release locks after work is done
    lock2.release()
    lock1.release()

    print("Thread 1: Released both locks.")

# Function for the second thread
def thread2_routine():
    print("Thread 2: Trying to acquire Lock 1...")  # Acquiring Lock 1 first to avoid deadlock
    lock1.acquire()
    print("Thread 2: Acquired Lock 1, now waiting for Lock 2...")
    time.sleep(1)  # Simulating some processing time

    print("Thread 2: Trying to acquire Lock 2...")
    lock2.acquire()
    print("Thread 2: Acquired Lock 2!")

    # Release locks after work is done
    lock2.release()
    lock1.release()

    print("Thread 2: Released both locks.")

# Create two threads
thread1 = threading.Thread(target=thread1_routine)
thread2 = threading.Thread(target=thread2_routine)

# Start both threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Both threads have finished execution.")
