from db_connection.db_connect import MockDB
import pytest

@pytest.fixture(scope='function')
def db_function():
    print("\nSetting up the DB connection for function scope")
    db = MockDB()
    yield db
    print("Disconnecting the DB for function scope")
    db.disconnect()

@pytest.fixture(scope='module')
def db_module():
    print("\nSetting up the DB connection for module scope")
    db = MockDB()
    yield db
    print("Disconnecting the DB for module scope")
    db.disconnect()

@pytest.fixture(scope='class')
def db_class():
    print("\nSetting up the DB connection for class scope")
    db = MockDB()
    yield db
    print("Disconnecting the DB for class scope")
    db.disconnect()

@pytest.fixture(scope='session')
def db_session():
    print("\nSetting up the DB connection for session scope")
    db = MockDB()
    yield db
    print("Disconnecting the DB for session scope")
    db.disconnect()
