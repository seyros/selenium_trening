from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

"""
    Открыть страницу http://suninjuly.github.io/selects1.html
    Посчитать сумму заданных чисел
    Выбрать в выпадающем списке значение равное расчитанной сумме
    Нажать кнопку "Submit"
"""


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    # Открыть страницу http://suninjuly.github.io/selects1.html
    browser.get("http://suninjuly.github.io/selects2.html")

    # Посчитать сумму заданных чисел
    num1 = browser.find_element_by_css_selector("[id='num1']")
    num2 = browser.find_element_by_css_selector("[id='num2']")
    summa = str(int(num1.text) + int(num2.text))

    # Выбрать в выпадающем списке значение, равное расчитанной сумме
    select = Select(browser.find_element_by_tag_name("select"))
    answer = select.select_by_value(summa)  # ищем элемент с рассчитанной ранее суммой в значении
    # answer.click()

    # Отправляем заполненную форму
    # time.sleep(1)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
