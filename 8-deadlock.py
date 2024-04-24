import time
import random
from threading import Thread, Lock

class DeadlockManager:
    def __init__(self):
        self.locks = [Lock(), Lock()]

    def acquire_locks(self, lock1, lock2):
        locks = sorted([self.locks[lock1], self.locks[lock2]], key=id)
        if all(lock.acquire(timeout=1) for lock in locks):
            return True
        for lock in locks:
            lock.release()
        return False

    def release_locks(self, lock1, lock2):
        for lock in (self.locks[lock1], self.locks[lock2]):
            lock.release()

def process_one(deadlock_manager):
    while True:
        print("Process One: Attempting to acquire Lock 1")
        if deadlock_manager.acquire_locks(0, 1):
            print("Process One: Acquired Locks 1 and 2")
            time.sleep(random.randint(1, 3))
            deadlock_manager.release_locks(0, 1)
            print("Process One: Released Locks 1 and 2")
            break
        else:
            print("Process One: Failed to acquire locks, retrying...")

def process_two(deadlock_manager):
    while True:
        print("Process Two: Attempting to acquire Lock 2")
        if deadlock_manager.acquire_locks(1, 0):
            print("Process Two: Acquired Locks 1 and 2")
            time.sleep(random.randint(1, 3))
            deadlock_manager.release_locks(1, 0)
            print("Process Two: Released Locks 1 and 2")
            break
        else:
            print("Process Two: Failed to acquire locks, retrying...")

if __name__ == "__main__":
    deadlock_manager = DeadlockManager()
    t1 = Thread(target=process_one, args=(deadlock_manager,))
    t2 = Thread(target=process_two, args=(deadlock_manager,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Main Thread: All processes completed successfully")