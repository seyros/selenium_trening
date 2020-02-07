
"""
    Открыть страницу http://suninjuly.github.io/alert_accept.html
    Нажать на кнопку
    Принять confirm
    На новой странице решить капчу для роботов, чтобы получить число с ответом

"""
from selenium import webdriver
import time

import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    # Открыть страницу http://suninjuly.github.io/alert_accept.html
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    # Нажать на кнопку
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Принять confirm
    alert = browser.switch_to.alert
    alert.accept()

    # Считать значение для переменной x
    x_value = browser.find_element_by_css_selector("[id='input_value']")
    x = x_value.text
    # Посчитать математическую функцию от x
    y = calc(x)

    # Ввести ответ в текстовое поле.
    answer = browser.find_element_by_css_selector("[id='answer']")
    answer.send_keys(y)

    # Отправляем заполненную форму
    time.sleep(1)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    assert True

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()