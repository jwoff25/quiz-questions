from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import keys
import bs4

# LOG IN TO CANVAS, ACCESS QUIZ PAGE
browser = webdriver.Firefox()
#browser.get("https://byuh.instructure.com/login/ldap")
browser.get("https://byuh.instructure.com/courses/1460354/quizzes/2328609")
username = browser.find_element_by_id("pseudonym_session_unique_id")
password = browser.find_element_by_id("pseudonym_session_password")
username.clear()
password.clear()
username.send_keys(keys.USER_NAME)
password.send_keys(keys.PASSWORD)
time.sleep(1)
#browser.find_element_by_class_name("Button Button--login").submit()
browser.find_element_by_css_selector("input").submit()

# START QUIZ
#browser.find_element_by_id("take_quiz_link").click()
soup = bs4.BeautifulSoup()
