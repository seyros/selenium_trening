
"""Попробуем теперь написать программу, которая будет бронировать нам дом для отдыха по строго заданной цене. Более высокая цена нас не устраивает, а по более низкой цене объект успеет забронировать кто-то другой.

В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

    Открыть страницу http://suninjuly.github.io/explicit_wait2.html
    Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    Нажать на кнопку "Book"
    Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение

Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод text_to_be_present_in_element из библиотеки expected_conditions.

Если все сделано правильно и быстро, то вы увидите окно с числом. Отправьте его в качестве ответа на это задание."""

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import pyperclip


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")


    # говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
    # button = WebDriverWait(browser, 12).until(
    #         EC.element_to_be_clickable((By.ID, "book"))
    #     )
    button = browser.find_element_by_id("book")
    WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button.click()

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
    # time.sleep(1)
    submit_button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "solve"))
    )
    submit_button.click()
    assert True

    # Копирование числа из алерта в буфер обмена
    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()



