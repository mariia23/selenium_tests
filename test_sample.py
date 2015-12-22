# -*- coding: utf-8 -*-

import random

import pytest
from selenium.webdriver import PhantomJS


def test_redirect_yandex_ua(phantom):
    assert phantom.current_url.startswith('https://www.yandex.ua/')


def test_yandex_title(phantom):
    assert phantom.title.startswith(u'Яндекс')


def test_refresh_yandex_ua(phantom):
    phantom.refresh()
    assert phantom.current_url.startswith('https://www.yandex.ua/')


@pytest.yield_fixture
def phantom(request):
    phantom = PhantomJS(service_args=['--ssl-protocol=any'])
    phantom.set_page_load_timeout(30)
    phantom.get('https://yandex.ru')

    yield phantom

    phantom.save_screenshot('phantom_{}.png'.format(request.node.name))
    phantom.quit()
