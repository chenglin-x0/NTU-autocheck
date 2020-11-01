from selenium import webdriver
import time
import random
import datetime
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')  
print("CheckIn Start :")
Time=random.randint(1,100)
print("Wait " + str(Time) +"  seconds")
time.sleep(Time)
driver=webdriver.Chrome("/home/local_Username/anaconda3/bin/chromedriver",options=chrome_options)
driver.get('https://my.ntu.edu.tw/attend/ssi.aspx?from=myNTU')
time.sleep(5)
loginmove=driver.find_element_by_link_text('登入')
loginmove.click()
userid=driver.find_element_by_name('user')
userpasswd=driver.find_element_by_name('pass')
userid.send_keys('User_name')
time.sleep(2)
userpasswd.send_keys('Password')
time.sleep(3)
loginsubmit=driver.find_element_by_name('Submit')
loginsubmit.click()
signout=driver.find_element_by_id('btSign')
time.sleep(5)
signout.click()
print("Now time is : " + str(datetime.datetime.now() ))
time.sleep(5)
driver.close()
print("CheckIn Success")
