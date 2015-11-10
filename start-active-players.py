#!/usr/bin/python

import time
from selenium import webdriver
from selenium.webdriver import PhantomJS
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from sys import argv
import click

@click.command()
@click.option('--days', type=int, prompt='Number of days to set active lineup', help='Number of days to set active lineup')
@click.option('--username', prompt='Your Yahoo username', help='Your Yahoo account username')
@click.option('--password', prompt='Your Yahoo password', help='Your Yahoo account password')
@click.option('--teamname', prompt='Which team do you want to set active lineup for? Enter teamname', help='Your Fantasy basketball teamname')
@click.option('--headless', type=bool, prompt='Do you want to run in headless mode? [True|False]', help='If True you won\'t see what\'s going on while it\'s running. If false you will see the browser render the steps.')
def start_active_players(days, username, password, teamname, headless):
	"""Simple python program that sets your active players for the next number DAYS."""
	print("Logging in as: " + username)

	if(headless):
		DesiredCapabilities.PHANTOMJS['phantomjs.page.settings.userAgent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:16.0) Gecko/20121026 Firefox/16.0'
		driver = webdriver.PhantomJS(executable_path='/Users/devin.mancuso/node_modules/phantomjs/bin/phantomjs')
	else:
		chrome_options = webdriver.ChromeOptions()
		driver = webdriver.Chrome(executable_path='/Library/Python/2.7/site-packages/selenium/webdriver/chrome/chromedriver', chrome_options=chrome_options)
		driver.set_window_size(1920, 1080)
		driver.maximize_window()

	driver.get('https://login.yahoo.com/config/login?.src=spt&.intl=us&.done=http%3A%2F%2Fbasketball.fantasysports.yahoo.com%2Fnba')

	driver.find_element_by_id('login-username').send_keys(username)	
	driver.find_element_by_id('login-passwd').send_keys(password)
	time.sleep(8)
	driver.find_element_by_name('signin').click()
	time.sleep(8)

	# hover to Fantasy Basketball to display the hidden dropdown menu 
	teams = driver.find_element_by_xpath("//li[@class = 'Navitem Navitem-main Navitem-fantasy Va-top Fl-start Topstart']")
	hov = ActionChains(driver).move_to_element(teams)
	hov.perform()
	time.sleep(1)

	driver.find_element_by_xpath("//a[text() = '"+ teamname +"']").click()
	time.sleep(2)

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