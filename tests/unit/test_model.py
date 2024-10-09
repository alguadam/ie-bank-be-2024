from iebank_api.models import Account
import pytest

#====test 5
def test_create_account():
    """
    GIVEN a Account model
    WHEN a new Account is created
    THEN check the name, account_number, balance, currency, status and created_at fields are defined correctly
    """
    account = Account('John Doe', '€', "Spain")
    assert account.name == 'John Doe'
    assert account.currency == '€'
    assert account.country == "Spain" # country
    assert account.account_number != None
    assert account.balance == 0.0
    assert account.status == 'Active'

def test_account_default_values():
    """
    GIVEN an Account model
    WHEN a new Account is created
    THEN check the default values for balance and status
    """
    account = Account('Test Default', '€', 'Germany')
    assert account.balance == 0.0  # Default balance
    assert account.status == 'Active'  # Default status

def test_account_repr():
    """
    GIVEN an Account model
    WHEN __repr__ is called
    THEN check that the output is formatted correctly
    """
    account = Account(name='Alice', currency='€', country='Spain')
    assert repr(account) == f"<Event '{account.account_number}'>"
