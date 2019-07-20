from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

x = (browser.find_element_by_id("num1")).text
y = (browser.find_element_by_id("num2")).text
answer = str(int(x) + int(y))

select = Select(browser.find_element_by_id("dropdown"))
select.select_by_value(answer) 

button = browser.find_element_by_tag_name("button")
button.click()