from selenium import webdriver
import os

# получаем путь к директории текущего исполняемого файла 
current_dir = os.path.abspath(os.path.dirname(__file__)) 
# добавляем к этому пути имя файла 
file_path = os.path.join(current_dir, 'test.txt')


link = " http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

name = browser.find_element_by_name("firstname")
name.send_keys("MyName")

lastname = browser.find_element_by_name("lastname")
lastname.send_keys("MyLastname")

email = browser.find_element_by_name("email")
email.send_keys("email@mail.com")

file = browser.find_element_by_id("file")
file.send_keys(file_path)


button = browser.find_element_by_tag_name("button")
button.click()