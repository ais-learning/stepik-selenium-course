from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

x = (browser.find_element_by_id("input_value")).text
y = calc(x)

answer = browser.find_element_by_id("answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
answer.send_keys(y)

option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
option1.click()

radio = browser.find_element_by_css_selector("[value='robots']")
browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
radio.click()



button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()