import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from sys import argv

script, daysstr, username, password = argv

days = int(argv[1])

print("Starter-Setter will set your active players for: " + daysstr + " days")
print("Logging in using:")
print("username: " + username)
print("password: " + password)

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path='/Library/Python/2.7/site-packages/selenium/webdriver/chrome/chromedriver', chrome_options=chrome_options)
driver.set_window_size(1920, 1080)
driver.maximize_window()

driver.get('https://login.yahoo.com/config/login?.src=spt&.intl=us&.done=http%3A%2F%2Fbasketball.fantasysports.yahoo.com%2Fnba')

driver.find_element_by_id('login-username').send_keys(username)	
driver.find_element_by_id('login-passwd').send_keys(password)
time.sleep(3)
driver.find_element_by_name('signin').click()
time.sleep(8)
driver.find_element_by_xpath("//a[text() = 'My Team ']").click()
time.sleep(4)

for x in range(0, days):

	driver.find_element_by_xpath("//a[text() = 'Start Active Players']").click()
	time.sleep(4)
	driver.find_element_by_xpath("//a[contains(@class, 'Js-next')]").click()
	time.sleep(4)

driver.quit()