from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    el1 = browser.find_element(By.ID, "num1")
    el2 = browser.find_element(By.ID, "num2")

    x_nmb = int(el1.text)
    y_nmb = int(el2.text)
    c = x_nmb + y_nmb

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(c))

    btn = browser.find_element(By.XPATH, "//button[text()='Submit']")
    btn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()