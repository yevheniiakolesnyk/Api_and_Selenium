from api_reqiests import *

def test_get_returns_200():
    result = get_request()
    assert result == 200

def test_get_picture_returns_200():
    result = get_picture()
    print()
    assert result.status_code == 200