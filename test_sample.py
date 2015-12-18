# -*- coding: utf-8 -*-


from selenium.webdriver import PhantomJS
from time import sleep
import random 


def test_redirect_yandex_ua():
    current_url = get_property('current_url')
    assert current_url.startswith('https://www.yandex.ua/')


def test_yandex_title():
    title = get_property('title')
    assert title.startswith(u'Яндекс')


def get_property(property_name):
    phantom = PhantomJS(service_args=['--ssl-protocol=any'])
    phantom.get('https://yandex.ru')
    sleep(15)
    properti = getattr(phantom, property_name)
    phantom.save_screenshot('phantom-{}.png'.format(random.random()))
    phantom.quit()
    return properti