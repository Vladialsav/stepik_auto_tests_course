from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import * 


def func(x):
    a = str(log(abs(12 * sin(int(x)))))
    return a

try:
    link = "http://suninjuly.github.io/explicit_wait2.html" 
    browser = webdriver.Chrome()
    browser.implicitly_wait(12)
    browser.get(link)

    price_wait = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    

    button = browser.find_element(By.ID, "book")
    button.click()


    
    x_element = browser.find_element(By.ID, "input_value")
    x_nmb = int(x_element.text)
    
    z = func(x_nmb)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(z)

    button2 = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
    