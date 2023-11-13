from selenium import webdriver  # Импортирование модуля webdriver из библиотеки selenium
from selenium.webdriver.common.keys import Keys  # Импортирование модуля Keys из библиотеки selenium для работы с клавишами
import time  # Импортирование модуля time для ожидания

driver = webdriver.Chrome()  # Создание экземпляра веб-драйвера Chrome
driver.get("https://google.com")  # Открытие страницы Google

search_box = driver.find_element("name", "q")
# Ищет элемент на веб-странице в соответствии с переданными аргументами.
# - "name": это способ поиска элемента по атрибуту "name".
# - "q": это конкретное значение атрибута "name", которое мы ищем.

search_box.send_keys("GeekBrains")  # Ввод текста "GeekBrains" в поле поиска
search_box.send_keys(Keys.RETURN)  # Нажатие клавиши "Enter" для выполнения поиска

time.sleep(10)  # Приостановка выполнения программы на 10 секунд для ожидания результатов поиска

driver.quit()  # Завершение работы веб-драйвера и закрытие браузера
