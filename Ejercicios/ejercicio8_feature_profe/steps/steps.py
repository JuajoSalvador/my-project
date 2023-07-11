import requests
from behave import *
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


@given('una URL')
def step_impl(context):
    context.URL = 'https://mtp.alejmans.dev/maas/proxy/test/suma'


@when('se hace una request GET con los parametros A = 1 y B = 2')
def step_impl(context):
    data = {
       "a": 1,
       "b": 2
    }
    context.response = float(requests.get(context.URL, params=data).text)


@when('se hace una request POST con los parametros A = 1 y B = 2')
def step_impl(context):
    data = {
       "a": 1,
       "b": 2
    }
    context.response = float(requests.post(context.URL, json=data).json()['result'])


@then('el resultado es 3')
def step_impl(context):
    print(context.response)
    assert context.response == 3