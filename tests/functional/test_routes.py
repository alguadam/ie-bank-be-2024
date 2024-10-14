from iebank_api import app
import pytest

def test_get_accounts(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is requested (GET)
    THEN check the response is valid
    """
    response = testing_client.get('/accounts')
    assert response.status_code == 200

def test_dummy_wrong_path():
    """
    GIVEN a Flask application
    WHEN the '/wrong_path' page is requested (GET)
    THEN check the response is valid
    """
    with app.test_client() as client:
        response = client.get('/wrong_path')
        assert response.status_code == 404

def test_create_account(testing_client):
    # Add the country field to the account creation request
    response = testing_client.post('/accounts', json={
        'name': 'John Doe',
        'currency': '€',
        'country': 'France'  # Include the country field
    })
    
    assert response.status_code == 201  # Expecting a 201 Created status
    data = response.get_json()
    
    # Ensure the response contains the correct account data
    assert data['name'] == 'John Doe'
    assert data['currency'] == '€'
    assert data['country'] == 'France'  # Ensure the country is correctly returned



