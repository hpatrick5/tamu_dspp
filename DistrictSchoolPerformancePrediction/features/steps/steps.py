from behave import *

use_step_matcher("re")

@given(u'I am on the "(?P<page>.*)" page')
def on_page(context, page):
    url = context.server_url + page.lower() +'/'
    context.browser.get(url)
    assert context.browser.current_url == url

@when(u'I enter my <(?P<username>.*)>, <(?P<password>.*)>')
def enter_login(context, username, password):
    user = context.browser.find_element_by_name('username')
    user.send_keys(context.table[0]['username'])
    pw = context.browser.find_element_by_name('password')
    pw.send_keys(context.table[0]['password'])

@when(u'I click "(?P<submit>.*)"')
def submit_form(context, submit):
     context.browser.find_element_by_class_name('form-group').submit()


@then(u'I should see "(?P<content>.*)"')
def i_see(context, content):
    html = context.browser.find_element_by_xpath(".//html")
    assert content in html.text


@then(u'I should not see "(?P<content>.*)"')
def step_impl(context, content):
    html = context.browser.find_element_by_xpath(".//html")
    assert content not in html.text


@when(u'I provide a <(?P<username>.*)>, <(?P<email>.*)>, <(?P<password1>.*)>, and <(?P<password2>.*)>')
def register(context, username, email, password1, password2):
    user = context.browser.find_element_by_name('username')
    user.send_keys(context.table[0]['username'])
    email = context.browser.find_element_by_name('email')
    email.send_keys(context.table[0]['email'])
    pw1 = context.browser.find_element_by_name('password1')
    pw1.send_keys(context.table[0][password1])
    pw2 = context.browser.find_element_by_name('password2')
    pw2.send_keys(context.table[0][password2])


@then(u'I should see the processed CSV data')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see the processed CSV data')


@then(u'I should download a CSV of ML predictions')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should download a CSV of ML predictions')


@when(u'I select a CSV to upload')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I select a CSV to upload')


@when(u'I click Upload')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click Upload')


@then(u'I should see a confirmation message that the upload was successful')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see a confirmation message that the upload was successful')