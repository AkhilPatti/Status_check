from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

# XPath selectors
NEW_CHAT_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/header[1]/div[2]/div[1]/span[1]/div[2]/div[1]/span[1]'
INPUT_TXT_BOX = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/span[1]/div[1]/span[1]/div[1]/div[1]/div[1]/label[1]/div[1]/div[2]'
ONLINE_STATUS_LABEL = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/div[1]/header[1]/div[2]/div[2]/span[1]'
NOT_FOUND='/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/span[1]/div[1]/span[1]/div[1]/div[2]/div[1]/div[1]/span[1]'
BACK_BTN='/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/span[1]/div[1]/span[1]/div[1]/header[1]/div[1]/div[1]/button[1]/span[1]'

TARGETS={}
no_of_input=int(input())
for i in range(no_of_input):
    contact=input("enter the name of the registered contact: ")
    TARGETS[contact]=contact
# Replace below path with the absolute path
browser = webdriver.Chrome(r'chromedriver_win32\chromedriver.exe')

# Load Whatsapp Web page
browser.get("https://web.whatsapp.com/")
wait = WebDriverWait(browser, 600)
current_no_of_contacts=len(TARGETS)
os.system('cls')
while current_no_of_contacts!=0:
    # Clear screen
                      
    # For each target
    for target in TARGETS.keys():
        if TARGETS[target]==0:
            continue
        tryAgain = True

        # Wait untill new chat button is visible
        new_chat_title = wait.until(EC.presence_of_element_located((By.XPATH, NEW_CHAT_BTN)))

        while (tryAgain):
            try:
                # Click on new chat button
                new_chat_title.click()
                
                # Wait untill input text box is visible
                input_box = wait.until(EC.presence_of_element_located((By.XPATH, INPUT_TXT_BOX)))

                time.sleep(0.5)

                # Write phone number
                
                input_box.send_keys(TARGETS[target])

                time.sleep(1)
                
                # Press enter to confirm the phone number
                input_box.send_keys(Keys.ENTER)

                time.sleep(5)
                tryAgain = False
                #if contact is not found
                try:
                    browser.find_element_by_xpath(NOT_FOUND)
                    print(target,'not found')
                    TARGETS[target]=0
                    #current contacts are reduced by 1
                    current_no_of_contacts-=1
                    #click back button
                    back = wait.until(EC.presence_of_element_located((By.XPATH, BACK_BTN)))
                    back.click()
                    time.sleep(3)
                    break
                except:
                    pass
                try:
                    browser.find_element_by_xpath(ONLINE_STATUS_LABEL)
                    t=time.time()
                    print(time.ctime(t),end="  ")
                    print(target,'is online')
                    TARGETS[target]=0
                    current_no_of_contacts-=1
                except:
                    pass
                time.sleep(1)

            except:
                new_chat_title = wait.until(EC.presence_of_element_located((By.XPATH, NEW_CHAT_BTN)))
                time.sleep(0.5)
