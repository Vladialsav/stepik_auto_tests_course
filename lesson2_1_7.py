from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    element1 = browser.find_element(By.ID, "treasure")
    el_x = element1.get_attribute("valuex")
    a = calc(el_x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(a)

    checkbox1 = browser.find_element(By.ID, "robotCheckbox")
    checkbox1.click()

    rdb = browser.find_element(By.ID, "robotsRule")
    rdb.click()

    btn = browser.find_element(By.XPATH, "//button[text()='Submit']")
    btn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
    

    

