import requests
from behave import *
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


@given('dada la URL')
def step_impl(context):
    context.URL = 'https://mtp.alejmans.dev/maas/proxy/test/suma'


@when('se hace request GET con los parametros A = 1 y B = 2')
def step_impl(context):
    data = {
       "a": 1,
       "b": 2
    }
    context.response = float(requests.get(context.URL, params=data).text)


@when('se hace request POST con los parametros A = 1 y B = 2')
def step_impl(context):
    data = {
       "a": 1,
       "b": 2
    }
    context.response = float(requests.post(context.URL, json=data).json()['result'])


@when('se hace request POST con los parametros A = (?P<a>.+) y B = (?P<b>.+')
def step_impl(context):
    data = {
       "a": a,
       "b": b
    }
    context.response = float(requests.post(context.URL, json=data).json()['result'])

@then('el resultado es (?P<c>.+')
def step_impl(context):
    print(context.response)
    assert context.response == float(c)


