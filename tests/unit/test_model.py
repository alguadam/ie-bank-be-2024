from iebank_api.models import Account
import pytest

def test_create_account():
    """
    GIVEN a Account model
    WHEN a new Account is created
    THEN check the name, account_number, balance, currency, status and created_at fields are defined correctly
    """
    account = Account('Zeid', '€', 'Jordan')
    assert account.name == 'Zeid'
    assert account.currency == '€'
    assert account.country == 'Jordan'
    assert account.account_number != None
    assert account.balance == 0.0
    assert account.status == 'Active'