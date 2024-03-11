import pytest
from classes.lesson22_class_home_work import Image


def test_image():
    page = Image()
    assert page.get_image() == 200


def test_image_jpeg(my_uri='/jpeg'):
    page = Image()
    assert page.get_image(my_uri) == 200


def test_image_png(my_uri='/png'):
    page = Image()
    assert page.get_image(my_uri) == 200


def test_image_svg(my_uri='/svg'):
    page = Image()
    assert page.get_image(my_uri) == 200


def test_image_webp(my_uri='/webp'):
    page = Image()
    assert page.get_image(my_uri) == 200
