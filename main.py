from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import json
def wait(time_of_sleep):
    return  time.sleep(time_of_sleep)
def element(method,name):
    return  driver.find_element(method,name)

print("Welcome to bot twitch to start you must join the discord server you must enter the bot lounge link as well as the twitch channel bots are blocked at 50 every 5 minutes made in good use ;)")
link = "https://discord.com/channels/849720413537173534/849720413750820912"

if len(link) == 0:
    print("please enter a link or the program will close ;) ")
    link = input("the link of the discord room ;)")

else:
    chanel = input("le liens du salon ;)")
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.get(link)
    with open('infos.json') as json_data:
        data = json.load(json_data)
        element(By.NAME,"email").send_keys(data['email'])
        element(By.NAME,"password").send_keys(data['password'])
    element(By.CSS_SELECTOR,".contents-18-Yxp").click()
    wait(10)
    while True:
        message = element(By.CSS_SELECTOR,".markup-2BOw-j.slateTextArea-1Mkdgw.fontSize16Padding-3Wk7zP")
        message.send_keys("/tfollow " + chanel)
        wait(1)
        message.send_keys(Keys.ENTER)
        message.send_keys(Keys.ENTER)
        wait(120)
        continue




