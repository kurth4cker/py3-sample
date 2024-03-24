import time

class Timer:
    def __init__(self):
        self.start = time.time()

    @property
    def elapsed(self):
        return time.time() - self.start


if __name__ == '__main__':
    timer = Timer()
    while timer.elapsed < 2:
        print("2 saniyeyi geçmedi...")
        time.sleep(0.3)
