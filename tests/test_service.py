from source import service  # <--- don't import the function directly

import pytest
from unittest import mock

@mock.patch("source.service.get_user_from_db")
def test_get_user_from_db(mock_get_user_from_db):
    mock_get_user_from_db.return_value = "Mocked Alice"
    
    # Call it via the module, so it gets the mocked version
    user_name = service.get_user_from_db(1)
    print(user_name)

    assert user_name == "Mocked Alice"
    
    
    
@mock.patch("source.service.get_key_from_db")
def test_get_key_from_db(mocked_key):
    mocked_key.return_value = 100
    user_key = service.get_key_from_db("Lalit")
    print(user_key)
    assert user_key==100


@mock.patch("requests.get")
def test_get_users_from_request(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {1:"Lalit","company":"Amazon"}
    mock_get.return_value=mock_response
    data = service.get_users_from_request()
    assert data=={1:"Lalit","company":"Amazon"}