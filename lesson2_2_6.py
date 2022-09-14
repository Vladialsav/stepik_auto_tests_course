from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from math import *

def func(x):
    a = str(log(abs(12 * sin(int(x)))))
    return a

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x_nmb = int(x_element.text)
    z = func(x_nmb)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(z)

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    rdbtn = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", rdbtn)
    rdbtn.click()

    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()