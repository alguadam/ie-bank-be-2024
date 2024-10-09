from iebank_api import app
import pytest

# ==Test 1: Hello World route
def test_hello_world(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid and returns "Hello, World!"
    """
    response = testing_client.get('/')
    assert response.status_code == 200
    assert response.get_data(as_text=True) == 'Hello, World!'

# ==Test 2: Create Account (POST /accounts)
def test_create_account(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is posted to (POST)
    THEN check that the response is valid and the account is created
    """
    response = testing_client.post('/accounts', json={'name': 'Jane Doe', 'currency': '€', 'country': 'France'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == 'Jane Doe'
    assert data['currency'] == '€'
    assert data['country'] == 'France'
    assert 'id' in data

# ==Test 3: Get All Accounts (GET /accounts)
def test_get_accounts(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is requested (GET)
    THEN check the response is valid
    """
    response = testing_client.get('/accounts')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data['accounts']) > 0  # Ensure accounts are returned
    assert 'Test Account' in [account['name'] for account in data['accounts']]

# ==Test 4: Get Single Account (GET /accounts/<id>)
def test_get_account(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts/<id>' page is requested (GET)
    THEN check that the response is valid and contains the correct account data
    """
    # First, create an account
    response = testing_client.post('/accounts', json={'name': 'John Doe', 'currency': '€', 'country': 'Spain'})
    account_id = response.get_json()['id']

    # Now, fetch the account by ID
    response = testing_client.get(f'/accounts/{account_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['id'] == account_id
    assert data['name'] == 'John Doe'

# == Test 5 : Update Account (PUT /accounts/<id>)
def test_update_account(testing_client):
    """
    GIVEN a Flask application
    WHEN an existing account is updated (PUT)
    THEN check the response is valid and the account is updated
    """
    # First, fetch the account to update
    response = testing_client.get('/accounts')
    assert response.status_code == 200
    accounts = response.get_json()['accounts']
    account_id = accounts[0]['id']

    # Now, update the account
    update_response = testing_client.put(f'/accounts/{account_id}', json={'name': 'Updated Account'})
    assert update_response.status_code == 200
    updated_data = update_response.get_json()
    assert updated_data['name'] == 'Updated Account'  # Verify that the update was successful

#====Test 6 :  Delete Account (DELETE /accounts/<id>)
def test_delete_account(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts/<id>' page is requested (DELETE)
    THEN check that the account is deleted successfully without fetching it after deletion
    """
    # First, create an account
    response = testing_client.post('/accounts', json={'name': 'John Doe', 'currency': '€', 'country': 'Spain'})
    assert response.status_code == 200  # Ensure account creation was successful
    account_data = response.get_json()
    account_id = account_data['id']

    # Now, delete the account
    delete_response = testing_client.delete(f'/accounts/{account_id}')
    assert delete_response.status_code == 200  # Ensure the account was successfully deleted

    # Check the deletion by verifying the delete response data if available
    delete_data = delete_response.get_json()
    assert delete_data['id'] == account_id  # The response should still contain the deleted account's ID
    
#===Test 7: POST
def test_dummy_wrong_path():
    """
    GIVEN a Flask application
    WHEN the '/wrong_path' page is requested (GET)
    THEN check the response is valid
    """
    with app.test_client() as client:
        response = client.get('/wrong_path')
        assert response.status_code == 404

