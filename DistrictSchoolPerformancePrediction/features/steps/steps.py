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
    user.send_keys(context.table[0][username])
    pw = context.browser.find_element_by_name('password')
    pw.send_keys(context.table[0][password])

@when(u'I click Login')
def step_impl(context):
     context.browser.find_element_by_class_name('form-group').submit()


@then(u'I should see "Upload File"')
def step_impl(context):
    html = context.browser.find_element_by_xpath(".//html")
    assert "Upload File" in html.text


@then(u'I should not see "Register"')
def step_impl(context):
    html = context.browser.find_element_by_xpath(".//html")
    assert "Register" not in html.text


@when(u'I provide a Username, Email, Password, and Confirmation')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I provide a Username, Email, Password, and Confirmation')


@when(u'I click Sign Up')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click Sign Up')


@then(u'I should see "Your account has been created! You can now Login"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see "Your account has been created! You can now Login"')


@given(u'I am on the Results page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I am on the Results page')


@then(u'I should see the processed CSV data')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see the processed CSV data')


@when(u'I click the Download CSV button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the Download CSV button')


@then(u'I should download a CSV of ML predictions')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should download a CSV of ML predictions')


@given(u'I am on the Upload File page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I am on the Upload File page')


@when(u'I click Choose File')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click Choose File')


@when(u'I select a CSV to upload')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I select a CSV to upload')


@when(u'I click Upload')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click Upload')


@then(u'I should see a confirmation message that the upload was successful')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see a confirmation message that the upload was successful')