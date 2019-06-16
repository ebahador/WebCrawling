# Digikala have been using AntiCrawler, so we need to change our technique a little
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

chromeBrowser = webdriver.Chrome()  # On Anaconda's root
checking = 'https://www.digikala.com/'
FLAG = True
while FLAG:
    link = input('Please put your Digikala link here: ')
    if checking in link:
        FLAG = False
    else:
        print('Your website either is not Digikala, or has not observed "HTTPS" legislation.')

chromeBrowser.get(link)
delay = 15  # 15 seconds for loading the page completely
element = WebDriverWait(chromeBrowser, delay).until(EC.presence_of_element_located((By.LINK_TEXT, 'نظرات کاربران')))

chromeBrowser.execute_script('arguments[0].scrollIntoView();', element)
time.sleep(2)
element.click()

# instead of using HTML signs, we need to gain access to the CSS part to see the tags without any classes or IDs
usersComments = chromeBrowser.find_elements_by_css_selector('.c-comments__list>li section .article p')
commentsTitle = chromeBrowser.find_elements_by_css_selector('.c-comments__list>li section .article .header>div')
usersIdentification = chromeBrowser.find_elements_by_css_selector('.c-comments__user-shopping>li .cell')
usersOrder = chromeBrowser.find_elements_by_css_selector('.c-comments__list>li section .aside .c-message-light')

content = ''
for i in range(len(usersComments)):
    content += '\n****** User comments[' + str(i + 1) + '] ******\n'
    content += commentsTitle[i].text + "\n"
    content += "- - - - \n"
    content += usersComments[i].text
    content += ' \n'
    if i < len(usersIdentification) - 1:
        content += '[' + usersIdentification[i].text + ' __ ' + usersIdentification[i + 1].text + '] | ' \
                   + '[' + usersOrder[i].text + ' __ ' + usersOrder[i + 1].text + '] | \n\n'

print(content)
file = open('C:\\Users\\yourName\\yourLocation\\Digi_Comments_Crawling.txt', 'w', encoding='utf-8')
file.write(content)
file.close()
