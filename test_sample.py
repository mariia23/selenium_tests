# -*- coding: utf-8 -*-

import random

import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import PhantomJS



class MutantPhantom(PhantomJS):

    def get(self, url):
        try:
            super(MutantPhantom, self).get(url)
        except TimeoutException:
            pass

    def refresh(self):
        try:
            super(MutantPhantom, self).refresh()
        except TimeoutException:
            pass


def test_redirect_yandex_ua(phantom):
    assert phantom.current_url.startswith('https://www.yandex.ua/')


def test_yandex_title(phantom):
    assert phantom.title.startswith(u'Яндекс')


def test_refresh_yandex_ua(phantom):
    phantom.refresh()
    assert phantom.current_url.startswith('https://www.yandex.ua/')


@pytest.yield_fixture
def phantom(request):
    phantom = MutantPhantom(service_args=['--ssl-protocol=any'])
    phantom.set_page_load_timeout(30)
    phantom.get('https://yandex.ru')

    yield phantom

    phantom.save_screenshot('phantom_{}.png'.format(request.node.name))
    phantom.quit()
