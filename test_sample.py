from selenium.webdriver import PhantomJS
from time import sleep


def test_phantom():
    phantom = PhantomJS(service_args=['--ssl-protocol=any'])
    phantom.get('https://yandex.ru')
    sleep(15)
    current_url = phantom.current_url
    phantom.save_screenshot('phantom.png')
    phantom.quit()
    assert current_url.startswith('https://www.yandex.ua/')