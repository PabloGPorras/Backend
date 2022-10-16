from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=chrome_options)

# Now you can start using Selenium
driver.get("https://www.walmart.com/account/login?vid=oaoh&tid=0&returnUrl=%2F")

#ENTER EMAIL
driver.find_element_by_xpath('//*[@id="email-split-screen"]').send_keys('pablamos.porras@gmail.com')

#SIGN IN AFTER EMAIL
driver.find_element_by_xpath('//*[@id="sign-in-with-email-validation"]/div[1]/div/button').click()

#USE PASSWORD RADIO BUTTON
driver.find_element_by_xpath('//*[@id="enterPwd"]').click()

#ENTER PASSWORD
driver.find_element_by_xpath('//*[@id="sign-in-password-change"]').send_keys('@Pablamos1725')

#CLICK SIGN IN 
driver.find_element_by_xpath('//*[@id="sign-in-with-pwd-form"]/div[5]/button').click()


#CONFIRM LOGGED IN 
test = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div/span/header/div[3]/a/div/div[1]').text
print(test)