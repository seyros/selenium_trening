from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector('input[placeholder="Input your first name"].form-control.first')
    input1.send_keys("Test name")
    input2 = browser.find_element_by_css_selector('input[placeholder="Input your last name"].form-control.second')
    input2.send_keys("Last name")
    input3 = browser.find_element_by_css_selector('input[placeholder="Input your email"].form-control.third')
    input3.send_keys("test@mail.co")
    time.sleep(5)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    # welcome_text_elt = browser.find_element_by_class_name("container") или так
    welcome_text_elt = browser.find_element_by_tag_name("h1")

    welcome_text_elt = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text_elt

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()