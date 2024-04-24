import threading
import time

class MyThread(threading.Thread):
    def run(self):
        try:
            print(f"Thread {threading.get_ident()} is running")
            time.sleep(1)
            print(f"Thread {threading.get_ident()} has completed")
        except KeyboardInterrupt:
            print("Thread interrupted")

class MyRunnable:
    def run(self):
        try:
            print(f"Runnable Thread {threading.get_ident()} is running")
            time.sleep(1)
            print(f"Runnable Thread {threading.get_ident()} has completed")
        except KeyboardInterrupt:
            print("Runnable Thread interrupted")

def main():
    n = 5
    print("Using Thread class:")
    for _ in range(n):
        MyThread().start()

    print("\nUsing Runnable interface:")
    for _ in range(n):
        threading.Thread(target=MyRunnable().run).start()

if __name__ == "__main__":
    main()