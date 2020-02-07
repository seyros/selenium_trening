
"""
В этом задании в форме регистрации требуется загрузить текстовый файл.

Напишите скрипт, который будет выполнять следующий сценарий:

    Открыть страницу http://suninjuly.github.io/file_input.html
    Заполнить текстовые поля: имя, фамилия, email
    Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    Нажать кнопку "Submit"

Если все сделано правильно и быстро, вы увидите окно с числом. Отправьте полученное число в качестве ответа для этого задания.
"""
from selenium import webdriver
import time
import os


try:
    browser = webdriver.Chrome()
    # Открыть страницу http://suninjuly.github.io/file_input.html
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    # Заполнить текстовые поля: имя, фамилия, email.
    name = browser.find_element_by_css_selector("input[name='firstname']")
    lastname = browser.find_element_by_css_selector("input[name='lastname']")
    email = browser.find_element_by_css_selector("input[name='email']")
    for i in [name, lastname, email]:
        i.send_keys("Test")

    # Загрузить файл. Файл должен иметь расширение .txt и может быть пустым.
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    element = browser.find_element_by_css_selector("input[name='file']")
    element.send_keys(file_path)

    # Нажать кнопку "Submit"
    time.sleep(1)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    assert True


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()