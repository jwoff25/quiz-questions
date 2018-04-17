from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import keys
import bs4

#all questions and answers
all_questions = []

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

with open("data.csv", 'w') as f:
    for x in range(80):
        questions = []
        answers = []
        # START QUIZ
        print "--- TAKING QUIZ ---"
        browser.find_element_by_id("take_quiz_link").click()
        time.sleep(1)
        browser.find_element_by_id("submit_quiz_button").click()
        alert = browser.switch_to.alert
        alert.accept()
        time.sleep(10)

        # PARSE QUIZ 
        print "--- PARSING ANSWERS ---"
        html = browser.page_source
        soup = bs4.BeautifulSoup(html, "html.parser")
        flag = []
        flag_count = 0
        for div in soup.findAll("div", {"class": "question_text user_content enhanced"}):
            if div.find('p').text not in all_questions: 
                flag.append(1)
                all_questions.append(div.find('p').text)
                questions.append(div.find('p').text)
            else:
                flag.append(0)
        print flag
        print flag_count
        for div in soup.findAll("div", {"class": "answer answer_for_ correct_answer"}):
            if flag_count < 5:    
                if flag[flag_count] == 1:
                    answers.append(div.get("title"))
            flag_count+=1
        print "--- WRITING DATA ---"
        print questions
        print answers
        for i in range(len(questions)):
            f.write((questions[i] + ";" + answers[i].replace("This was the correct answer.", '').strip()).encode('utf-8'))
            f.write("\n")
        time.sleep(5)
        #print questions
        #print answers
        print "--- LOOP: " + str(x+1) + " OVER ---"
