
"""
В этом задании после нажатия кнопки страница откроется в новой вкладке,
нужно переключить WebDriver на новую вкладку и решить в ней задачу.

    Открыть страницу http://suninjuly.github.io/redirect_accept.html
    Нажать на кнопку
    Переключиться на новую вкладку
    Пройти капчу для робота и получить число-ответ
"""
from selenium import webdriver
import time

import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    # Открыть страницу http://suninjuly.github.io/redirect_accept.html
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    # Нажать на кнопку
    first_window = browser.window_handles[0]
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Переключиться на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # Пройти капчу для робота и получить число-ответ
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

