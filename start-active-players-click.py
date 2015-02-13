import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from sys import argv
import click

#script, daysstr, username, password = argv

#daysint = int(days)

@click.command()
@click.option('--days', type=int, prompt='Number of days to set active lineup', help='Number of days to set active lineup')
@click.option('--username', prompt='Your Yahoo username:', help='Your Yahoo account username')
@click.option('--password', prompt='Your Yahoo passwordname:', help='Your Yahoo account password')
def start_active_players(days, username, password):
	"""Simple python program that sets your active players for the next number DAYS."""
	print("Logging in as: " + username)

	#daysint = int(days)

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
		time.sleep(2)
		date_text = driver.find_element_by_xpath("//span[@class='flyout-title']").text
		print("Starting active players for: " + date_text)
		driver.find_element_by_xpath("//a[contains(@class, 'Js-next')]").click()
		time.sleep(2)

	driver.quit()






if __name__ == '__main__':
	start_active_players()
