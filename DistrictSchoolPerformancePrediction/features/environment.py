from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def before_all(context):
	# PhantomJS is used there (headless browser - meaning we can execute tests in a command-line environment, which is what we want for use with SemaphoreCI
	# For debugging purposes, you can use the Firefox driver instead.
    chromedriver_path = '/home/ec2-user/.local/lib/python3.7/site-packages'
    os.chmod(chromedriver_path, 0o755)

    #System.setProperty("webdriver.chrome.driver", "/home/ec2-user/.local/lib/python3.7/site-packages")
    options = Options()
    options.headless = True
    #options.System.setProperty("webdriver.chrome.driver", "/home/ec2-user/.local/lib/python3.7/site-packages")
    context.browser = webdriver.Chrome(chromedriver_path, options=options)
    context.browser.implicitly_wait(1)
    context.server_url = 'http://localhost:8000'

def after_all(context):
	# Explicitly quits the browser, otherwise it won't once tests are done
	context.browser.quit()

def before_feature(context, feature):
	# Code to be executed each time a feature is going to be tested
	pass