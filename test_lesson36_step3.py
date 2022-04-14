import time
import math
from telnetlib import EC

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


a = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]
d=''
@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(6)
    yield browser
    browser.quit()

@pytest.mark.parametrize('url', a)
def test_open_url(browser, url):
    browser.get(url)
    b = browser.find_element_by_class_name('ember-text-area')
    b.send_keys(math.log(int(time.time()+1.2)))
    button = browser.find_element_by_class_name("submit-submission")
    button.click()
    c = browser.find_element_by_class_name("smart-hints__hint").text
    assert c=='Correct!', c
print(d)