from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import keys
import bs4

# initialize my variables
questions = []
answers = []

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
time.sleep(5)

# START QUIZ
browser.find_element_by_id("take_quiz_link").click()
time.sleep(5)
browser.find_element_by_id("submit_quiz_button").click()
alert = browser.switch_to.alert
alert.accept()
time.sleep(5)

# PARSE QUIZ 
html = browser.page_source
soup = bs4.BeautifulSoup(html, "html.parser")
for div in soup.findAll("div", {"class": "question_text user_content enhanced"}):
    if div.find('p').text not in questions: 
        questions.append(div.find('p').text)
for div in soup.findAll("div", {"class": "answer answer_for_ correct_answer"}):
    if div.get("title") not in answers:
        answers.append(div.get("title"))

print questions
print answers
#print soup.prettify()
with open("data.csv", 'w') as f:
    for i in range(len(questions)):
        f.write((questions[i] + "," + answers[i].split(". ")[0]).strip().encode('utf-8'))
        f.write("\n")
#browser.close()