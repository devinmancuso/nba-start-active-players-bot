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
def start_active_players(days, username, password, teamname):
	"""Simple python program that sets your active players for the next number DAYS."""
	print("Logging in as: " + username)

	DesiredCapabilities.PHANTOMJS['phantomjs.page.settings.userAgent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:16.0) Gecko/20121026 Firefox/16.0'

	driver = webdriver.PhantomJS(executable_path='/Users/devin.mancuso/node_modules/phantomjs/bin/phantomjs')


	driver.get('https://login.yahoo.com/config/login?.src=spt&.intl=us&.done=http%3A%2F%2Fbasketball.fantasysports.yahoo.com%2Fnba')
	
	#with open('jquery-2.1.3.min.js', 'r') as jquery_js: jquery = jquery_js.read() #read the jquery from a file
	#driver.execute_script(jquery) #active the jquery lib


	driver.find_element_by_id('login-username').send_keys(username)	
	driver.find_element_by_id('login-passwd').send_keys(password)
	time.sleep(8)
	driver.find_element_by_name('signin').submit()
	#form1 = driver.find_element_by_id('mbr-login-form')
	#form1.submit()
	driver.implicitly_wait(12) # 12 seconds
	driver.save_screenshot('screenshot.png')


	# hover to Fantasy Basketball to display the hidden dropdown menu 
	teams = driver.find_element_by_xpath("//li[@class = 'Navitem Navitem-main Navitem-fantasy Va-top Fl-start Topstart']")
	hov = ActionChains(driver).move_to_element(teams)
	hov.perform()
	time.sleep(1)

	driver.find_element_by_xpath("//a[text() = '"+ teamname +"']").click()
	time.sleep(2)

	for x in range(0, days):

		driver.find_element_by_xpath("//a[text() = 'Start Active Players']").click()
		driver.implicitly_wait(2) # 2 seconds
		date_text = driver.find_element_by_xpath("//span[@class='flyout-title']").text
		print("Starting active players for: " + date_text)
		driver.find_element_by_xpath("//a[contains(@class, 'Js-next')]").click()
		driver.implicitly_wait(2) # 2 seconds

	driver.quit()

if __name__ == '__main__':
	start_active_players()