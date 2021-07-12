# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import time
import os


# %%
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


# %%
chromeoptions = webdriver.ChromeOptions()


# %%
## For Linux!

chromeoptions.add_argument('--user-data-dir=./User_Data')
chrome = webdriver.Chrome(chrome_options=chromeoptions)


# %%
## For Windows!

# chromeoptions.add_argument('--allow-profiles-outside-user-dir')             # Not neccessary but have it.
# chromeoptions.add_argument('--enable-profile-shortcut-manager')                # Not neccessary but have it.
# chromeoptions.add_argument("user-data-dir=" + os.path.abspath(r'.\User_Data'))    # Windows needs Absolute Path to be given
# chromeoptions.add_argument('--profile-directory=Profile 1')
# chrome = webdriver.Chrome( executable_path="C:\Drivers\chromedriver.exe", chrome_options=chromeoptions)   # chromedriver absolute path should be given


# %%
chrome.implicitly_wait(30)
chromeWait = WebDriverWait(chrome, 30)
chrome.maximize_window()


# %%
chrome.get("https://web.whatsapp.com")


# %%
# Searching for the contact

xpath = "//*[@id='side']/div[1]/div/label/div/div[2]"
SearchBar = chrome.find_element(By.XPATH, xpath)
SearchBar.click()
SearchBar.send_keys("Shobhan")
time.sleep(3)
SearchBar.send_keys(Keys.ENTER)
time.sleep(3)


# %%
messageBoxClass = "_33LGR"
MessageBox = chrome.find_element(By.CLASS_NAME, messageBoxClass)


# %%
# Scrolling and taking screenshots

for i in range(4, -1, -1):
    fileName = "ss_" + str(i+1) + ".png"
    MessageBox.screenshot(fileName)
    MessageBoxHeight = MessageBox.size['height']
    chrome.execute_script("arguments[0].scrollBy(0, arguments[1]);", MessageBox, -MessageBoxHeight)
    time.sleep(3)
    


# %%
chrome.get("https://web.telegram.org/?legacy=1#/im")
teleSeachXPath = "//*[@id='ng-app']/body/div//input[@type='search']"


# %%
teleSearchBar = chrome.find_element(By.XPATH, teleSeachXPath)


# %%
teleSearchBar.send_keys("RX 100")
time.sleep(2)
teleSearchBar.send_keys(Keys.ENTER)
time.sleep(2)


# %%
TeleInputFilecClass = "im_attach_input"


# %%
TeleFileInput = chrome.find_element(By.CLASS_NAME, TeleInputFilecClass)
time.sleep(2)


# %%
for i in range(5):
    TeleFileInput.send_keys(os.path.abspath("./ss_" + str(i+1) + ".png"))

time.sleep(60)


# %%
chrome.close()


# %%



