#Getting set up for work - This will open all required apps for when im WFH
#Import Station
import pyautogui

#pyatuogui command - global settings needed for pyautogui
pyautogui.FAILSAFE = True                       #allows me to put mouse in top left of screen to stop the script
pyautogui.PAUSE = 1.75                          #gives a 1.5sec delay between each pyautogui command

#Open copilot
pyautogui.click(18, 1065)                       #clicks windows button
pyautogui.typewrite('copilot')                  #searches for copilot
pyautogui.press('enter')                        #opens cipilot
#Move copilot to other screen
pyautogui.doubleClick(1745, 17)                 #makes sure main window of copilot is selected
pyautogui.dragTo(2999, -153, duration=0.4)      #moves copilot to 3rd monitor
pyautogui.click(2739, -840, duration=0.05)      #focuses copilot 
pyautogui.dragTo(2999, -853, duration=0.4)      #drags to top right 1/4 of screen
pyautogui.click(2459, -263)                     #focuses copilot 
pyautogui.dragTo(1920, -283, duration=0.2)      #makes copilot fill top half of 3rd monitor 
#Sign in to copilot
pyautogui.click(861, 596, duration=0.1)         #clicks on password field
pyautogui.typewrite('**password**')   #enters password for copilot
pyautogui.click(952, 683)                       #clicks 'sign-in' button

#global for Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
#selenium command - global settings for selenium
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
#Open Teams
driver = webdriver.Chrome()                                                                                         #opens a chrome browser                                            
driver.get('https://teams.microsoft.com/_?culture=en-au&country=au#/conversations/19:3e9090edaece4ea7bc8804d28edf0227@thread.v2?ctx=chat') #Load MS Teams in the browser
#Sign into teams
driver.implicitly_wait(4)                                                                                           #setting a wait timer for 2 seconds
loginElements = driver.find_element(By.CSS_SELECTOR, '#mectrl_headerPicture')                                       #this is finding the login to account element
loginElements.click()                                                                                               #should click the login button
driver.find_element(By.ID, 'i0116').send_keys('**password**')                                 #Finding username bar and enterin username
driver.find_element(By.ID, 'i0116').send_keys(Keys.ENTER)                                                           #confirms username with ENTER key
driver.find_element(By.ID, 'i0118').send_keys('**password**')                                                  #locating password field and entering my password
SignInButton = driver.find_element(By.CSS_SELECTOR, '#idSIButton9')                                                 #Signin Button set variable 
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(SignInButton))                                           #getting code to wait
driver.find_element(By.ID, 'i0118').send_keys(Keys.ENTER)                                                           #confirm password
#TODO: Maybe move teams?


#Open Citrix Workspace
pyautogui.click(18, 1065)                       #clicks windows button
pyautogui.typewrite('citrix')                   #searches for citrix WS
pyautogui.press('enter')                        #opens citrix WS
pyautogui.click(1098, 145, duration=5)          #FILLER: should give citrix enough time to open
#Open VD-WIN10
pyautogui.click(1010, 192)                      #clicks on desktops in citrix WS
pyautogui.click(701, 507)                       #clicks dropdown box for WIN10VD
pyautogui.click(519, 634)                       #opens the VD
#Sign into Citrix Workspace
pyautogui.click(812, 539)
pyautogui.typewrite('**password**')
pyautogui.press('enter')