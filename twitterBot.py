from cred import passw
from cred import username
import time

from selenium import webdriver

path = "/home/abhishek/chrome/chromedriver"

url = "https://twitter.com/"

tweet = "Hello World!! Its an automated tweeeet"

driver = webdriver.Chrome(path)

driver.get(url)
time.sleep(2)
login = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/div/div[2]/div/div/div[1]/a')
login.click()

user = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input')
user.send_keys(username)
pwd = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input')
pwd.send_keys(passw)
log = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[3]/div/div')
log.click()
time.sleep(2)

driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div/span/br').send_keys(tweet)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]/div/span/span').click()
time.sleep(2)

