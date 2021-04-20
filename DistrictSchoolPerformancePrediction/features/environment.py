from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def before_all(context):
    options = Options()
    options.headless = True

    context.browser = webdriver.Chrome(options=options)
    context.server_url = 'https://sp21-606-school-district-data.herokuapp.com/'
    context.browser.implicitly_wait(1)
    context.browser.get(context.server_url)
    assert "DSPP" in context.browser.title

def after_all(context):
	context.browser.quit()

def before_step(context, step):
   WebDriverWait(context.browser, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*')))