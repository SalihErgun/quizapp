import time

class Timer:
    def __init__(self, time_limit):
        self.time_limit = time_limit
        self.start_time = None
        self.end_time = None
        self.is_running = False

    def start_timer(self):
        self.start_time = time.time()
        self.end_time = self.start_time + self.time_limit
        self.is_running = True
        print("Timer started.")

    def check_time(self):
        if not self.is_running:
            return False
        remaining_time = self.end_time - time.time()
        if remaining_time <= 0:
            self.is_running = False
            return False
        return True

    def stop_timer(self):
        self.is_running = False
