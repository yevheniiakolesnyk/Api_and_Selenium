import pytest
from classes.lesson21_class import MySelenium


@pytest.mark.parametrize('base_url', [('https://www.google.com.ua/')])
def test_base_url(base_url):
    page = MySelenium()
    page.get_page(base_url)
    assert page.get_current_url() == 'https://www.google.com.ua/'


@pytest.mark.parametrize('base_url, param', [('https://www.google.com.ua/', 'Hello, World!')])
def test_search_box(base_url, param):
    page = MySelenium()
    page.get_page(base_url)
    text_box = page.search_box(param)
    assert text_box == 'Hello, World!'


@pytest.mark.parametrize('base_url', [('https://www.google.com.ua/')])
def test_go_through_links(base_url):
    page = MySelenium()
    page.get_page(base_url)
    new_url = page.go_through_links()
    assert new_url == 'https://www.google.com.ua/'
