from behave import *
from django.urls import reverse
use_step_matcher("re")


@given(u'I am on the "(?P<page>.*)" page')
def on_page(context, page):
    page_mappings = {'Home' : 'login-home', 'About' : 'login-about', 'Upload': 'login-upload', 'Register' : 'register', 'Login' : 'main-login' } 
    page_name = str('login/' + page.lower() + '.html')
    response = context.client.get(reverse(page_mappings[page]))
    assert response.templates[0].name == page_name


@when(u'I enter my Username, Password')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter my Username, Password')


@when(u'I click Login')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click Login')


@then(u'I should see Upload File')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see Upload File')


@then(u'I should not see Register')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should not see Register')


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