from django.test import Client

def before_all(context):
    context.client = Client()

def django_ready(context):
    context.django = True