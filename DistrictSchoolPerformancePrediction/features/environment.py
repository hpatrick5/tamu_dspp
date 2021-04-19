from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def before_all(context):
    options = Options()
    options.headless = True

    context.browser = webdriver.Chrome(options=options)
    context.browser.implicitly_wait(1)
    context.server_url = 'http://localhost:8000'

def after_all(context):
	context.browser.quit()

def before_feature(context, feature):
	pass