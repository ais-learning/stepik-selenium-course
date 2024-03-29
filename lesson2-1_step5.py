from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))




link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)


x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

answer = browser.find_element_by_id("answer")
answer.send_keys(y)


option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
option1.click()

radio = browser.find_element_by_css_selector("[value='robots']")
radio.click()

button = browser.find_element_by_tag_name("button")
button.click()