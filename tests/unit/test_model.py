from iebank_api.models import Account
import pytest

def test_create_account():

    account = Account('John Doe', '€', 'France')  # Include the country field in the Account initialization
    assert account.name == 'John Doe'
    assert account.currency == '€'
    assert account.account_number is not None
    assert account.balance == 0.0
    assert account.status == 'Active'
    assert account.country == 'France'  # Check if the country field is correctly set
