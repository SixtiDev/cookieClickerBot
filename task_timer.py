import time


class TaskTimer:

    def __init__(self, upgrade_period, product_period, game_time):
        self.start_time = time.time()
        self.last_buy_upgrade_time = self.start_time
        self.last_buy_product_time = self.start_time
        self.upgrade_period = upgrade_period
        self.product_period = product_period
        self.game_time_period = game_time

    def is_time_for_upgrade(self):
        now = time.time()
        if now >= self.last_buy_upgrade_time + self.upgrade_period:
            self.last_buy_upgrade_time = now
            print("Buy upgrade time")
            return True

    def is_time_for_product(self):
        now = time.time()
        if now >= self.last_buy_product_time + self.product_period:
            self.last_buy_product_time = now
            print("Buy product time")
            return True

    def is_time_for_end_game(self):
        now = time.time()
        if now >= self.start_time + self.game_time_period:
            return True
