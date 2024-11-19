import time

class Timer:
    def __init__(self, total_time):
        self.total_time = total_time
        self.time_left = total_time

    def start_timer(self):
        self.time_left = self.total_time
        while self.time_left > 0:
            time.sleep(1)
            self.time_left -= 1

    def stop_timer(self):
        self.time_left = 0

    def check_time_left(self):
        return self.time_left
