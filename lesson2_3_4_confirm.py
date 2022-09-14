from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from math import * 


def func(x):
    a = str(log(abs(12 * sin(int(x)))))
    return a

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.XPATH, "//button[text()='I want to go on a magical journey!']")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()


    time.sleep(1)

    x_element = browser.find_element(By.ID, "input_value")
    x_nmb = int(x_element.text)
    z = func(x_nmb)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(z)

    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
    