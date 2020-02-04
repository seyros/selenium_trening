from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()

    # Открыть страницу http://suninjuly.github.io/math.html.
    browser.get("http://suninjuly.github.io/math.html")

    # Считать значение для переменной x.
    x_element = browser.find_element_by_css_selector("[id='input_value']")
    x = x_element.text

    # Посчитать математическую функцию от x
    y = calc(x)

    # Ввести ответ в текстовое поле.
    answer = browser.find_element_by_css_selector("[id='answer']")
    answer.send_keys(y)

    # Отметить checkbox "I'm the robot".
    checkbox = browser.find_element_by_css_selector("[id='robotCheckbox']")
    checkbox.click()

    # Проверка, что по дефолту уже отмечен чек-бокс "People rule"
    people_radio = browser.find_element_by_id("peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"

    # Проверка, что второй радиобаттон не выбран по дефолту
    robots_radio = browser.find_element_by_id("robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    assert robots_checked is None

    # Выбрать radiobutton "Robots rule!"
    radiobutton = browser.find_element_by_css_selector("[id='robotsRule']")
    radiobutton.click()

    # Отправляем заполненную форму
    time.sleep(1)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
