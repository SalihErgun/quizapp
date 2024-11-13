import time

class Timer:
    def _init_(self, time_limit):
        # Sınav için süre limiti (saniye cinsinden) belirlenir
        self.time_limit = time_limit
        self.start_time = None
        self.end_time = None
        self.is_running = False

    def start_timer(self):
        """Timer’ı başlatır ve sınav süresini başlatır."""
        self.start_time = time.time()  # Başlangıç zamanını kaydeder
        self.end_time = self.start_time + self.time_limit  # Bitiş zamanını hesaplar
        self.is_running = True
        print("Timer başladı.")

    def check_time(self):
        """Kalan süreyi kontrol eder. Süre dolmuşsa False, dolmamışsa True döner."""
        if not self.is_running:
            print("Timer çalışmıyor.")
            return False
        remaining_time = self.end_time - time.time()
        if remaining_time <= 0:
            self.is_running = False
            print("Süre doldu!")
            return False  # Süre dolmuş
        else:
            print(f"Kalan süre: {int(remaining_time)} saniye")
            return True  # Süre devam ediyor

    def stop_timer(self):
        """Timer’ı durdurur."""
        self.is_running = False
        print("Timer durdu.")