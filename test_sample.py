# -*- coding: utf-8 -*-

import random
from time import sleep

import pytest
from selenium.webdriver import PhantomJS


def test_redirect_yandex_ua(phantom):
    assert phantom.current_url.startswith('https://www.yandex.ua/')


def test_yandex_title(phantom):
    assert phantom.title.startswith(u'Яндекс')


def test_refresh_yandex_ua(phantom):
    phantom.refresh()
    sleep(10)
    assert phantom.current_url.startswith('https://www.yandex.ua/')


@pytest.yield_fixture
def phantom():
    phantom = PhantomJS(service_args=['--ssl-protocol=any'])
    phantom.get('https://yandex.ru')
    sleep(15)

    yield phantom

    phantom.save_screenshot('phantom-{}.png'.format(random.random()))
    phantom.quit()
