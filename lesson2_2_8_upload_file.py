from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from math import *
import os 

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input_name = browser.find_element(By.NAME, "firstname")
    input_name.send_keys("Антон")
    input_lastname = browser.find_element(By.NAME, "lastname")
    input_lastname.send_keys("Иванов")
    input_email = browser.find_element(By.NAME, "email")
    input_email.send_keys("ochkojirafa123@mail.ru")


    current_dir = os.path.abspath(os.path.dirname(__file__)) # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'test_file.txt')   # добавляем к этому пути имя файла 


    input_file = browser.find_element(By.ID, "file")
    input_file.send_keys(file_path)

    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()