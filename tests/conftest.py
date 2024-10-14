# import pytest
# from iebank_api.models import Account
# from iebank_api import db, app
# from config import TestConfig  # Import the TestConfig

# @pytest.fixture(scope='module')
# def testing_client():
#     # Set up the Flask app with the testing configuration
#     app.config.from_object(TestConfig)

#     with app.app_context():
#         db.create_all()  # Create the database tables for testing

#         # Add a sample account
#         account = Account('Test Account', '€', 'France')
#         db.session.add(account)
#         db.session.commit()

#         # Create a test client
#         with app.test_client() as testing_client:
#             yield testing_client  # Run the tests

#         # Tear down the database after the tests
#         with app.app_context():
#             db.drop_all()

import pytest
from iebank_api.models import Account
from iebank_api import db, app
from config import TestConfig

@pytest.fixture(scope='module')
def testing_client():
    # Force the app to use TestConfig for testing
    app.config.from_object(TestConfig)
    
    # Debugging: Print out the database URI to check if it's correctly set
    print(f"SQLALCHEMY_DATABASE_URI during tests: {app.config['SQLALCHEMY_DATABASE_URI']}")

    with app.app_context():
        db.create_all()

        account = Account('Test Account', '€', 'France')
        db.session.add(account)
        db.session.commit()

        with app.test_client() as testing_client:
            yield testing_client

        with app.app_context():
            db.drop_all()
