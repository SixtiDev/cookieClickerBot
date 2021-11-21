from cookie_webdriver import CookieWebdriver
from task_timer import TaskTimer

cookie_webdriver = CookieWebdriver()
timer = TaskTimer(10, 5, 600)

while not timer.is_time_for_end_game():

    cookie_webdriver.click_cookie()

    if timer.is_time_for_upgrade():
        cookie_webdriver.buy_upgrades()

    if timer.is_time_for_product():
        cookie_webdriver.buy_products()

cookie_webdriver.close_game()
